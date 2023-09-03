def adaptive_trade_on_news():
    # Get the last 30 days' performance
    _, return_percentage = backtest_strategy("30 days ago", "today")
    
    if return_percentage > 0:
        # If the strategy was profitable in the last 30 days, continue using it
        trade_on_news()
    else:
        # If the strategy was not profitable, hold and don't make any trades
        logger.info("Strategy was not profitable in the last 30 days. Holding.")
