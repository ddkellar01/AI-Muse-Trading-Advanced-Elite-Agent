class StrategyEngine:
    def __init__(self, target_allocation: dict):
        # Example: {"BTC/USD": 0.80, "ETH/USD": 0.20}
        self.target_allocation = target_allocation

    def calculate_rebalance(self, current_portfolio_values: dict, total_value: float) -> list:
        instructions = []
        for asset, target_pct in self.target_allocation.items():
            current_val = current_portfolio_values.get(asset, 0.0)
            current_pct = current_val / total_value if total_value > 0 else 0.0
            diff = target_pct - current_pct
            
            if abs(diff) > 0.02:  # Rebalance threshold threshold (2%)
                action = "BUY" if diff > 0 else "SELL"
                target_amount = abs(diff) * total_value
                instructions.append({"asset": asset, "action": action, "amount": target_amount})
                
        return instructions
