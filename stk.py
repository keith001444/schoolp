from flask import Flask, request, jsonify, render_template
import requests
import json
from requests.auth import HTTPBasicAuth
import datetime

app = Flask(__name__)

# Replace with your credentials
CONSUMER_KEY = 'twd2Fk9toBVjeGi67JCCfEqh0uB7OJPXNiA63g44ek3dpskP'
CONSUMER_SECRET = '9lXIcf6er5THdG7DAZWpv8sGeiXyEziH13RuTmuFVGAWhAJxB6LqPWMHUbrWFnx2'
SHORTCODE = '174379'
PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
LIPA_NA_MPESA_ONLINE_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

def get_access_token():
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRET))
    
    # Log the response status and content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    
    if response.status_code == 200:
        return json.loads(response.text)['access_token']
    else:
        raise Exception(f"Failed to get access token: {response.status_code}, {response.text}")


@app.route('/pay_fees/<admission_no>', methods=['GET', 'POST'])
def pay_fees(admission_no):
    if request.method == 'POST':
        amount = request.form['amount']
        phone_number = request.form['phone_number']

        access_token = get_access_token()
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }

        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        password = f"{SHORTCODE}{PASSKEY}{timestamp}".encode('utf-8')
        password = password.hex()

        payload = {
            'BusinessShortCode': SHORTCODE,
            'Password': password,
            'Timestamp': timestamp,
            'TransactionType': 'CustomerPayBillOnline',
            'Amount': amount,
            'PartyA': phone_number,
            'PartyB': SHORTCODE,
            'PhoneNumber': phone_number,
            'CallBackURL': 'https://example.com',
            'AccountReference': admission_no,
            'TransactionDesc': 'Fee payment',
        }

        response = requests.post(LIPA_NA_MPESA_ONLINE_URL, headers=headers, json=payload)
        return response.json()

    return render_template('pay_fees.html', admission_no=admission_no)

@app.route('/mpesa_callback', methods=['POST'])
def mpesa_callback():
    data = request.json
    # Example of how to extract data
    if data['Body']['stkCallback']['ResultCode'] == 0:
        amount_paid = data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        return render_template('payment_success.html', amount=amount_paid)
    else:
        print("Payment Failed!!")
        return "Payment failed", 400

if __name__ == '__main__':
    app.run(debug=True)
