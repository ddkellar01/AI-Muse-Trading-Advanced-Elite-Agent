import sys
import os
import logging
from sqlalchemy import create_engine, text

# Ensure the root directory is in the python path for absolute imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import settings
from agents.executor import CoinbaseExecutor

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("HealthCheck")

def check_environment_variables() -> bool:
    logger.info("Checking critical environment variables...")
    missing = []
    if not settings.COINBASE_API_KEY:
        missing.append("COINBASE_API_KEY")
    if not settings.COINBASE_API_SECRET:
        missing.append("COINBASE_API_SECRET")
        
    if missing:
        logger.error(f"❌ Missing required environment variables: {', '.join(missing)}")
        return False
    logger.info("✅ Environment variables configuration verified.")
    return True

def check_database_connection() -> bool:
    logger.info(f"Checking database connectivity ({settings.DATABASE_URL})...")
    try:
        engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("✅ Database connection successful.")
        return True
    except Exception as e:
        logger.error(f"❌ Database connection failed: {str(e)}")
        return False

def check_coinbase_api() -> bool:
    logger.info("Verifying Coinbase Advanced API connectivity...")
    try:
        executor = CoinbaseExecutor()
        balance = executor.fetch_balance()
        
        if "error" in balance:
            logger.error(f"❌ Coinbase API returned an error: {balance['error']}")
            return False
            
        logger.info("✅ Coinbase Advanced API connection and authentication successful.")
        return True
    except Exception as e:
        logger.error(f"❌ Coinbase API connectivity exception: {str(e)}")
        return False

def run_health_check():
    logger.info("=== Starting AI Muse Trading Elite Agent Health Check ===")
    
    env_ok = check_environment_variables()
    db_ok = check_database_connection()
    api_ok = check_coinbase_api()
    
    if env_ok and db_ok and api_ok:
        logger.info("=== All health checks passed successfully! Agent is operational. ===")
        sys.exit(0)
    else:
        logger.error("=== Health check failed. Please review the errors above. ===")
        sys.exit(1)

if __name__ == "__main__":
    run_health_check()
