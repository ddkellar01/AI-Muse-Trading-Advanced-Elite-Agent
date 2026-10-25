import sys
from agents.executor import CoinbaseExecutor

def run_health_check():
    print("Running system health check...")
    executor = CoinbaseExecutor()
    balance = executor.fetch_balance()
    
    if "error" in balance:
        print(f"❌ Coinbase API Connectivity Failed: {balance['error']}")
        sys.exit(1)
    else:
        print("✅ Coinbase API Connection Successful!")
        sys.exit(0)

if __name__ == "__main__":
    run_health_check()
