import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    n = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    currencies = o["bpi"]
    usd = currencies["USD"]
    rate = usd["rate_float"]
    amount = n * rate
    print(f"${amount:,.4f}")
except (requests.RequestException, ValueError):
    sys.exit("Command-line argument is not a number")
