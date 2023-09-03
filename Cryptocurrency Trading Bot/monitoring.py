import smtplib

SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_password"

def send_email(subject, body):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(SMTP_USERNAME, "recipient@example.com", message)

def monitor_bot_health():
    # Check if the bot is running and if there were any trades in the last 24 hours
    last_trade = get_last_trade_time()  # Assuming a function that gets the timestamp of the last trade
    if not last_trade or (current_time() - last_trade) > 24*60*60:
        send_email("Bot Alert", "No trades were made in the last 24 hours. Please check the bot.")
