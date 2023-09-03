import shutil
import datetime

def backup_database():
    date_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"backup_{date_str}.db"
    shutil.copy('crypto_bot.db', backup_name)
