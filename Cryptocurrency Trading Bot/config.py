import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# News scraper configurations
NEWS_REFRESH_INTERVAL = 60  # Check news every 60 seconds

BINANCE_API_KEY = os.environ.get('BINANCE_API_KEY')
BINANCE_API_SECRET = os.environ.get('BINANCE_API_SECRET')