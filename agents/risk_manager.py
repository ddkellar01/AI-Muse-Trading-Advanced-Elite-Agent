class RiskManager:
    def __init__(self, max_drawdown_pct: float = 10.0, max_allocation_pct: float = 50.0):
        self.max_drawdown_pct = max_drawdown_pct
        self.max_allocation_pct = max_allocation_pct

    def validate_trade(self, current_balance: float, proposed_trade_amount: float, asset_allocation: float) -> tuple[bool, str]:
        if proposed_trade_amount > (current_balance * (self.max_allocation_pct / 100.0)):
            return False, "Trade violates maximum single-asset allocation limit."
        
        if asset_allocation > self.max_allocation_pct:
            return False, "Asset portfolio weight exceeds allowed risk threshold."
            
        return True, "Trade approved."
