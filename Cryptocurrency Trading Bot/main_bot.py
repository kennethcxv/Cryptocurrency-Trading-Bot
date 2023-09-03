from config import logger, NEWS_REFRESH_INTERVAL
import time
import logging

MAX_RETRIES = 3

if __name__ == "__main__":
    logger.info("Starting the Crypto Trading Bot based on News Sentiment...")
    
    retries = 0
    while True:
        try:
            trade_on_news()
            retries = 0  # Reset retries after successful execution
            time.sleep(NEWS_REFRESH_INTERVAL)
        except Exception as e:
            retries += 1
            logger.error(f"Error occurred: {e}. Retry {retries}/{MAX_RETRIES}")
            if retries >= MAX_RETRIES:
                logger.error("Max retries reached. Exiting.")
                break
            
logging.basicConfig(filename='crypto_bot.log', level=logging.INFO)

def main():
    try:
        adaptive_trade_on_news()
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        send_email("Bot Error", f"An error occurred: {str(e)}")  # Using the send_email function from monitoring.py
