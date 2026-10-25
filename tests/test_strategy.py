import unittest
from agents.strategy import StrategyEngine

class TestStrategyEngine(unittest.TestCase):
    def test_rebalance_calculation(self):
        target = {"BTC/USD": 0.80, "ETH/USD": 0.20}
        current_holdings = {"BTC/USD": 500.0, "ETH/USD": 500.0}
        total_value = 1000.0
        
        engine = StrategyEngine(target)
        actions = engine.calculate_rebalance(current_holdings, total_value)
        
        # Expected: BTC needs more funds (BUY), ETH has too much (SELL)
        self.assertTrue(any(a["asset"] == "BTC/USD" and a["action"] == "BUY" for a in actions))
        self.assertTrue(any(a["asset"] == "ETH/USD" and a["action"] == "SELL" for a in actions))

if __name__ == "__main__":
    unittest.main()
