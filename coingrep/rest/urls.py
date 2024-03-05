'''
The UrlBuilder class is used to construct routes for the coingecko V3 Api
'''

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
        
'''test    
url_builder = UrlBuilder()
print(url_builder.simple_price(['bitcoin','cardano'], ['usd', 'chf']))
'''