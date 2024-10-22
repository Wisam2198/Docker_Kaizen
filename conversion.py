from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Clé API ExchangeRate (inscris-toi pour obtenir une clé gratuite)
API_KEY = '8ee253fe250b85d49fba1b0d'
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_currency():
    amount = float(request.form.get('amount'))
    from_currency = request.form.get('from_currency')
    to_currency = request.form.get('to_currency')
    
    # Appel à l'API des taux de change
    response = requests.get(API_URL + from_currency)
    exchange_rates = response.json().get('conversion_rates')
    
    if to_currency in exchange_rates:
        converted_amount = amount * exchange_rates[to_currency]
        # Formater le montant converti à deux décimales
        converted_amount = round(converted_amount, 2)
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
