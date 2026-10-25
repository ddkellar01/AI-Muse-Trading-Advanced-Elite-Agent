from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from agents.strategy import StrategyEngine
from agents.executor import CoinbaseExecutor
from agents.risk_manager import RiskManager

app = FastAPI(title="AI Muse Trading Elite Agent", version="1.0")

class AgentPromptRequest(BaseModel):
    action: str
    target_allocations: dict | None = None

executor = CoinbaseExecutor()
risk_manager = RiskManager()

@app.post("/api/v1/agent/prompt")
async def handle_muse_prompt(request: AgentPromptRequest):
    if request.action == "get_portfolio":
        balance = executor.fetch_balance()
        return {"status": "success", "data": balance}
        
    elif request.action == "rebalance" and request.target_allocations:
        balance = executor.fetch_balance()
        if "error" in balance:
            raise HTTPException(status_code=400, detail=balance["error"])
            
        total_val = balance.get("total", {}.get("USD", 1000.0))
        strategy = StrategyEngine(request.target_allocations)
        rebalance_actions = strategy.calculate_rebalance(balance.get("free", {}), total_val)
        
        executed_trades = []
        for act in rebalance_actions:
            is_valid, msg = risk_manager.validate_trade(total_val, act["amount"], request.target_allocations[act["asset"]])
            if is_valid:
                res = executor.execute_market_order(act["asset"], act["action"].lower(), act["amount"])
                executed_trades.append({"asset": act["asset"], "result": res})
            else:
                executed_trades.append({"asset": act["asset"], "skipped": msg})
                
        return {"status": "success", "trades": executed_trades}
        
    raise HTTPException(status_code=400, detail="Invalid command or missing payload.")
