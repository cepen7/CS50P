import sys
import requests
import json


def main():
    if len(sys.argv) == 2:
        try:
            n = sys.argv[1]
            float(n)
            get_bitcoin_price(n)
        except ValueError:
            sys.exit('Command/line argument is not a number')
            
    else:
        sys.exit('Missing command-line argument')


def get_bitcoin_price(x):
    try:
        bcValue = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response = bcValue.json()
        bcPriceUSD = response["bpi"]["USD"]["rate"]
        bcPriceUSD = bcPriceUSD.replace(",", "")
        result = float(bcPriceUSD) * float(x)
        print(f'${result:,.4f}')
    except requests.RequestException:
        print('fail')

if __name__ == "__main__":
    main()




