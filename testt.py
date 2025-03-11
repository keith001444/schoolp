import logging  # Import Python's built-in logging module
import requests
from requests.auth import HTTPBasicAuth
import base64
from datetime import datetime
from flask import Flask, request, jsonify, render_template, redirect, url_for
import os

app = Flask(__name__)

# Set up logging correctly
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Function to get access token
def get_access_token():
    consumer_key = "twd2Fk9toBVjeGi67JCCfEqh0uB7OJPXNiA63g44ek3dpskP"
    consumer_secret = "9lXIcf6er5THdG7DAZWpv8sGeiXyEziH13RuTmuFVGAWhAJxB6LqPWMHUbrWFnx2"
    endpoint = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    response = requests.get(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    if response.status_code == 200:
        return response.json().get("access_token")
    
    logger.error(f"Error generating token: {response.text}")
    return None

# Route to initiate STK push

@app.route('/pay_fees/<admission_no>', methods=['GET', 'POST'])
def initiate_stk_push(admission_no):
    if request.method == 'POST':
        amount = request.form.get('amount')
        phone_number = request.form.get('phone_number')

        if not amount or not phone_number:
            logger.error("Missing amount or phone number")
            return jsonify({"status": "error", "message": "Amount and Phone number are required."}), 400

        access_token = get_access_token()
        if not access_token:
            logger.error("Error: Could not get access token.")
            return jsonify({"status": "error", "message": "Could not get access token"}), 500

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        business_short_code = "174379"
        passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password_str = business_short_code + passkey + timestamp
        password = base64.b64encode(password_str.encode('utf-8')).decode('utf-8')

        data = {
            "BusinessShortCode": business_short_code,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "PartyA": phone_number,
            "PartyB": business_short_code,
            "PhoneNumber": phone_number,
            "CallBackURL": "https://279a-197-136-183-18.ngrok-free.app/mpesa/callback",
            "AccountReference": admission_no,
            "TransactionDesc": "Fee Payment",
            "Amount": amount
        }

        endpoint = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        response = requests.post(endpoint, json=data, headers=headers)

        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")

        if response.status_code == 200:
            # ✅ Redirect to a waiting page where we check the callback
            return redirect(url_for('wait_for_callback', admission_no=admission_no))  
        else:
            logger.error(f"Failed to initiate STK Push: {response.json()}")
            return jsonify({"status": "error", "message": "Failed to initiate payment"}), 500
    
    return render_template('pay_fees.html', admission_no=admission_no)

@app.route('/wait_for_callback/<admission_no>')
def wait_for_callback(admission_no):
    return render_template('waiting.html', admission_no=admission_no)


# Callback listener to handle the result from Safaricom
transaction_status = {"status": "pending"}  # Store transaction status

@app.route('/mpesa/callback', methods=['POST'])
def mpesa_callback():
    global transaction_status  # Store result

    response_data = request.get_json()
    logger.info(f"Callback Response: {response_data}")

    result_code = response_data['Body']['stkCallback']['ResultCode']
    result_desc = response_data['Body']['stkCallback']['ResultDesc']

    if result_code == 0:
        logger.info(f"Payment Successful: {result_desc}")
        transaction_status = {"status": "success", "message": "Payment completed successfully!"}
    elif result_code == 1032:
        logger.info(f"Payment Canceled: {result_desc}")
        transaction_status = {"status": "error", "message": "Payment was canceled by the user."}
    else:
        logger.error(f"Error: {result_desc}")
        transaction_status = {"status": "error", "message": result_desc}

    return jsonify(transaction_status), 200
@app.route('/check_payment_status')
def check_payment_status():
    return jsonify(transaction_status)
@app.route('/payment_success')
def payment_success():
    return "<h1>Payment Successful!</h1><p>Your transaction was completed successfully.</p>"

@app.route('/payment_failed')
def payment_failed():
    return "<h1>Payment Failed!</h1><p>Your transaction could not be completed.</p>"



# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True, port=5000)
