import ccxt
from config.settings import settings

class CoinbaseExecutor:
    def __init__(self):
        self.exchange = ccxt.coinbaseadvanced({
            'apiKey': settings.COINBASE_API_KEY,
            'secret': settings.COINBASE_API_SECRET,
            'enableRateLimit': True,
        })

    def fetch_balance(self):
        try:
            return self.exchange.fetch_balance()
        except Exception as e:
            return {"error": str(e)}

    def execute_market_order(self, symbol: str, side: str, amount: float):
        try:
            order = self.exchange.create_market_order(symbol, side, amount)
            return {"status": "success", "order": order}
        except Exception as e:
            return {"status": "error", "message": str(e)}
