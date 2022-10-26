from forex_python.converter import (CurrencyRates, CurrencyCodes, RatesNotAvailableError)
from flask import flash
from decimal import Decimal

currencies = {'ZAR', 'PHP', 'PLN', 'BRL', 'CZK', 
            'MXN', 'INR', 'RUB', 'NOK', 'USD', 
            'THB', 'NZD', 'HRK', 'TRY', 'CNY', 
            'KRW', 'CHF', 'AUD', 'HKD', 'SGD', 
            'SEK', 'MYR', 'RON', 'HUF', 'JPY', 'EUR'} 

def check_if_valid_currency_code(currency_from, currency_to): 
    if (RatesNotAvailableError):
        if currency_from not in currencies:
            flash(f'Not valid code: {currency_from}.', 'error')
        if currency_to not in currencies:
            flash(f'Not valid code: {currency_to}.', 'error')  

def calculate_conversion_and_check_amount(currency_from, currency_to, amount, symbol):
    c = CurrencyRates()
    symbol = CurrencyCodes()
    symbol = symbol.get_symbol(currency_to)
    if (currency_from in currencies) and (currency_to in currencies):
        try: 
            conversion_result = round(c.convert(currency_from, currency_to, Decimal(amount)), 2)
            flash(f'The result is {symbol}{conversion_result}', 'success')
        except:  
            flash('Not valid amount', 'error')