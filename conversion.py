from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Clé API ExchangeRate (inscris-toi pour obtenir une clé gratuite)
API_KEY = 'votre_api_key'
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

@app.route('/convert', methods=['GET'])
def convert_currency():
    amount = float(request.args.get('amount'))
    from_currency = request.args.get('from_currency')
    to_currency = request.args.get('to_currency')
    
    # Appel à l'API des taux de change
    response = requests.get(API_URL + from_currency)
    exchange_rates = response.json().get('conversion_rates')
    
    if to_currency in exchange_rates:
        converted_amount = amount * exchange_rates[to_currency]
        return jsonify({
            'amount': amount,
            'from_currency': from_currency,
            'to_currency': to_currency,
            'converted_amount': converted_amount
        })
    else:
        return jsonify({'error': 'Invalid currency'}), 400

if __name__ == '__main__':
    app.run(debug=True)
