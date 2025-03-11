import requests
from requests.auth import HTTPBasicAuth
import base64
from datetime import datetime
from flask import Flask, request, jsonify, redirect, url_for
import os
import logging
import time

app = Flask(__name__)

# Set up logging
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
    else:
        logger.error(f"Error generating token: {response.text}")
        return None

# Function to initiate STK Push
from flask import render_template

@app.route('/pay_fees/<admission_no>', methods=['GET', 'POST'])
def initiate_stk_push(admission_no):
    if request.method == 'POST':
        # If the form is submitted via POST, capture the data
        amount = request.form.get('amount')
        phone_number = request.form.get('phone_number')

        # Validate that we received the necessary data
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
            "CallBackURL": "https://279a-197-136-183-18.ngrok-free.app/mpesa/callback",  # Correct callback URL
            "AccountReference": admission_no,
            "TransactionDesc": "Fee Payment",
            "Amount": amount
        }
    
        endpoint = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        response = requests.post(endpoint, json=data, headers=headers)
    
        logger.info(f"Response Status Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        if response.status_code == 200:
            return redirect(url_for('mpesa_callback'), code=307)# Or render success message on the template
        else:
            logger.error(f"Failed to initiate STK Push: {response.json()}")
            return jsonify({"status": "error", "message": "Failed to initiate payment"}), 500
    
    # If it's a GET request, just render the template and pass the admission_no
    return render_template('pay_fees.html', admission_no=admission_no)


# Callback listener to handle the result from Safaricom
@app.route('/mpesa/callback', methods=['POST'])
def mpesa_callback():
    response_data = request.get_json()
    
    logger.info(f"Callback Response: {response_data}")
    
    result_code = response_data['Body']['stkCallback']['ResultCode']
    result_desc = response_data['Body']['stkCallback']['ResultDesc']
    
    if result_code == 0:
        logger.info(f"Payment Successful: {result_desc}")
        print("success")
        return jsonify({"status": "success", "message": "Payment completed successfully!"}), 200
    elif result_code == 1032:
        logger.info(f"Payment Canceled: {result_desc}")
        print("cancelled")
        return jsonify({"status": "cancelled", "message": "Payment was canceled by the user."}), 200
    else:
        logger.error(f"Error: {result_desc}")
        print("Error")
        return jsonify({"status": "error", "message": result_desc}), 200

# Start the Flask server to listen for the callback
if __name__ == '__main__':
    app.run(debug=True, port=5000)
