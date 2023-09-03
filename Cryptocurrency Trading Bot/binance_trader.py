from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET
from database_manager import insert_trade_action

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def trade_on_news():
    news_headlines = get_latest_news()
    sentiments = [analyze_sentiment(headline) for headline in news_headlines]
    
    positive_count = sentiments.count("positive")
    negative_count = sentiments.count("negative")
    
    # Check current balance
    balance = client.get_asset_balance(asset='USDT')
    available_balance = float(balance['free'])
    
    if positive_count > negative_count and available_balance > 10:  # Assuming a minimum of 10 USDT to place an order
        # Buy logic
        order = client.order_market_buy(
            symbol='DOGEUSDT',
            quantity=available_balance
        )
        insert_trade_action("BUY", "Positive news sentiment")
    elif negative_count > positive_count:
        # Sell logic
        doge_balance = client.get_asset_balance(asset='DOGE')
        available_doge = float(doge_balance['free'])
        if available_doge > 10:  # Assuming a minimum of 10 DOGE to sell
            order = client.order_market_sell(
                symbol='DOGEUSDT',
                quantity=available_doge
            )
            insert_trade_action("SELL", "Negative news sentiment")
