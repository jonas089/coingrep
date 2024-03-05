# CoinGrep ~ Jonas P
CoinGrep is an easy to use Python scraper for CoinGecko that can be used to aggregate and store market related information of Crypto assets.

GeckoGrep is a simplistic starting point for development on top of the Coingecko API and it could be used to develop a Python DA service for token metrics tooling.

# URL Builder
The UrlBuilder is modular and new methods can easily be added:

```python
class UrlBuilder:
    def __init__(self, API_BASE, API_COINS, API_SIMPLE):
        self.API_BASE = API_BASE
        self.API_COINS = API_COINS
        self.API_SIMPLE = API_SIMPLE

    # Get the current asset price for a list of assets and fiat currencies
    def simple_price(self, ids, vs_currencies):
        return "{}/price?ids={}&vs_currencies={}".format(self.API_SIMPLE, ','.join(ids), ','.join(vs_currencies))

    # List all supported fiat currencies
    def simple_supported_vs_currencies(self):
        return "{}/supported_vs_currencies".format(self.API_SIMPLE)

    # List all supported coins id, name and symbol
    def coins_list(self):
        return "{}/list".format(self.API_COINS)
    
    # List all supported coins price, market cap, volume and market related data
    def coins_market(self):
        return "{}/markets".format(self.API_COINS)

    # Get historical market data for a single asset
    def coins_history(self, id):
        return "{}/{}/history".format(self.API_COINS, id)
```

The UrlBuilder can be found in `rest/urls.py`.

# Storage
Lists of historical market data can be stored using the Storage module:
```python
class MarketData:
    def __init__(self, id, timestamp, prices):
        self.id = id
        self.unix_timestamp = timestamp
        self.human_timestamp = unix_to_human(timestamp)
        self.prices = prices
    def build(self):
        return {
            "id": self.id,
            "unix_timestamp": self.unix_timestamp,
            "human_timestamp": self.human_timestamp,
            "prices": self.prices
        }
```

# Examples: Query Bitcoin Price
A simple example on how to query the Bitcoin price can be found in `./examples/bitcoin_price.py`