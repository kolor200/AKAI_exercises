import requests
import json
from pprint import pprint as pp
import datetime
import math
import sys


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


def get_data(cur1, cur2):
    """Gets data from currency ratios api and saves it in a json file."""
    cur1 = cur1.upper()
    cur2 = cur2.upper()

    params = {
        'symbols': f'{cur1}' + ',' + f'{cur2}'
    }
    # Requests data from api
    response = requests.get(url='https://api.exchangeratesapi.io/latest', params=params)
    print(response.json())
    if response.status_code == 200:
        response = response.json()
        dictionary = dict()
        dictionary['base_currency'] = cur1
        dictionary['target_currency'] = cur2
        dictionary['date_fetched'] = response['date']
        ratio = response['rates'][cur2]/response['rates'][cur1]
        dictionary['ratio'] = ratio

        try:
            with open('ratios.json', 'r') as outfile:
                data = json.load(outfile)

            data.append(dictionary)

            with open('ratios.json', 'w') as outfile:
                json.dump(data, outfile, indent=4, sort_keys=True)
        # If file doesn't exist
        except FileNotFoundError:
            a_list = list()
            a_list.append(dictionary)
            with open('ratios.json', 'w+') as outfile:
                json.dump(a_list, outfile, indent=4, sort_keys=True)
        # If file is corrupted.
        except json.decoder.JSONDecodeError:
            print("Error while opening ratios.json file. File is corrupted.")
    else:
        print("Error while requesting data from exchange_rate_api:")
        pp(response.json()['error'])
        print("Status_code: " + str(response.status_code))
        ratio = 0
    return ratio


def convert_currency(amount, cur1, cur2):
    """Converts currency"""
    with open('ratios.json', 'r') as outfile:  # Loading ratios.json file
        ratios = json.load(outfile)

    a_ratio = None
    for ratio in ratios:  # Checking if ratios were already downloaded for the day
        if ratio['date_fetched'] == datetime.date.today().strftime("%Y-%m-%d"):
            if ratio['base_currency'] == cur1 and ratio['target_currency'] == cur2:
                a_ratio = ratio['ratio']
                break

    if not a_ratio:
        a_ratio = get_data(cur1=cur1, cur2=cur2)
    if not a_ratio == 0:  # Converts currency
        amount_after_conversion = round_up(n=a_ratio * amount, decimals=2)
        print(str(amount) + f' {cur1} = ' + str(amount_after_conversion) + f' {cur2}')
    else:
        print("Error, ratio = 0")


if __name__ == '__main__':
    convert_currency(amount=float(sys.argv[1]), cur1=sys.argv[2], cur2=sys.argv[3])
