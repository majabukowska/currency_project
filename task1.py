from flask import Flask
import requests
import logging
import datetime
import sys

task1 = Flask(__name__)

date = sys.argv[1]
currency = sys.argv[2]
date_format = '%Y-%m-%d'
if date is None:
    raise Exception("Date is not set")
else:
    try:
        dateObject = datetime.datetime.strptime(date, date_format)
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")

if currency is None:
    raise Exception("Currency is not set")

@task1.route('/')
def start():
    return 'start'
@task1.route('/avg_rate')
def avg_currency_rate():

    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}/'
    response = requests.get(url)

    if response.status_code != 200:
        logging.warning(f'Wrong status code - {response.status.code}')
    else:
        data = response.json()
        avg_currency_rate = data['rates'][0]['mid']
        return f"Average {currency} rate for {date} is {avg_currency_rate}"


if __name__ == '__main__':
    task1.run(debug=True)