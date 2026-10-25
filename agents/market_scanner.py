from agents.executor import CoinbaseExecutor
import logging

logger = logging.getLogger("MarketScanner")

class MarketScanner:
    def __init__(self):
        self.executor = CoinbaseExecutor()

    def get_market_prices(self, symbols: list[str]) -> dict:
        prices = {}
        try:
            tickers = self.executor.exchange.fetch_tickers(symbols)
            for symbol, data in tickers.items():
                prices[symbol] = data.get('last')
        except Exception as e:
            logger.error(f"Failed to fetch market prices: {str(e)}")
        return prices
