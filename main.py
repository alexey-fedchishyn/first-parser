import requests
import json
import csv
from datetime import datetime as dt


JSON_FILE_NAME = 'crypto_live.json'
RESULT_FILE_NAME = 'crypto_live.csv'


def get_json(url):
    response = requests.get(url)
    with open(JSON_FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def write_csv(crypto_dict):
    with open(RESULT_FILE_NAME, 'w') as file:
        writer = csv.writer(file)
        headers = ['Currency', 'Date', 'Time', 'Volume', 'Price']
        writer.writerow(headers)
        for item in crypto_dict:
            row = get_row(item)
            writer.writerow(row)


def get_row(item):
    crypto_name = item['name']
    date = dt.now().strftime('%H/%m/%Y')
    time = dt.now().strftime('%H:%M:%S')
    crypto_volume = item['volume']
    crypto_price = item['price']
    return crypto_name, date, time, crypto_volume, crypto_price


def get_dict_from_json():
    with open(JSON_FILE_NAME) as f:
        page_data = json.load(f)
        crypto_dict = page_data['data']
        return crypto_dict


def main():
    get_json('https://www.binance.com/bapi/composite/v1/public/marketing/symbol/list')
    crypto_dict = get_dict_from_json()
    write_csv(crypto_dict)


if __name__ == '__main__':
    main()
