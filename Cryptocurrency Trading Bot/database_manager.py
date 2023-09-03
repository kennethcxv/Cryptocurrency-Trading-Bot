import sqlite3

DB_NAME = 'crypto_bot.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS news_headlines (
            id INTEGER PRIMARY KEY,
            headline TEXT,
            sentiment TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)
        conn.execute("""
        CREATE TABLE IF NOT EXISTS trade_actions (
            id INTEGER PRIMARY KEY,
            action TEXT,
            reason TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

def insert_headline(headline, sentiment):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO news_headlines (headline, sentiment) VALUES (?, ?)", (headline, sentiment))

def insert_trade_action(action, reason):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("INSERT INTO trade_actions (action, reason) VALUES (?, ?)", (action, reason))
