import time
import schedule
import logging
from agents.executor import CoinbaseExecutor
from agents.strategy import StrategyEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("CronScheduler")

def scheduled_portfolio_audit():
    logger.info("Running scheduled periodic portfolio check...")
    executor = CoinbaseExecutor()
    balance = executor.fetch_balance()
    if "error" in balance:
        logger.error(f"Scheduled audit failed to fetch balance: {balance['error']}")
    else:
        logger.info("Portfolio audit successful. Assets synced with Coinbase Advanced.")

def setup_scheduler():
    schedule.every(1).hours.do(scheduled_portfolio_audit)
    logger.info("Cron scheduler initialized. Waiting for tasks...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    setup_scheduler()
