import unittest
from agents.risk_manager import RiskManager

class TestRiskManager(unittest.TestCase):
    def test_trade_approval_within_limits(self):
        rm = RiskManager(max_drawdown_pct=10.0, max_allocation_pct=50.0)
        approved, msg = rm.validate_trade(current_balance=10000.0, proposed_trade_amount=1000.0, asset_allocation=30.0)
        self.assertTrue(approved)

    def test_trade_rejection_over_allocation(self):
        rm = RiskManager(max_drawdown_pct=10.0, max_allocation_pct=50.0)
        approved, msg = rm.validate_trade(current_balance=10000.0, proposed_trade_amount=6000.0, asset_allocation=60.0)
        self.assertFalse(approved)

if __name__ == "__main__":
    unittest.main()
