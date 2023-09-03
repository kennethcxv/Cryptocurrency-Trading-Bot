def backtest_strategy(start_date, end_date):
    historical_data = get_historical_news(start_date, end_date)
    initial_balance = 1000  # USDT
    balance = initial_balance
    
    for data_point in historical_data:
        sentiment = analyze_sentiment(data_point['headline'])
        if sentiment == "positive":
            # Simulate buying DOGE with all available balance
            balance *= 1.05  # Assuming a 5% increase
        elif sentiment == "negative":
            # Simulate selling DOGE
            balance *= 0.95  # Assuming a 5% decrease
    
    return_balance = balance - initial_balance
    return_percentage = (return_balance / initial_balance) * 100
    return return_balance, return_percentage
