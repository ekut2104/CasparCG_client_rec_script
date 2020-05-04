import os
from shutil import disk_usage
from datetime import datetime, timedelta
import telegram_sender

path = 'H:\\media'
deleted_files = []

total, used, free = disk_usage("/")
if used / total > 0.1:
    d = f'{datetime.now() - timedelta(days=14):%Y%m%d}'
    if os.path.exists(path):
        if os.path.isdir(path):
            list_of_files1 = os.listdir(path=path)
            for i in list_of_files1:
                if int(d) > int(i[:8]):
                    os.remove(f'{path}\\{i}')
                    print(f'{path}\\{i} - removed')
                    deleted_files.append(i)

    telegram_sender.send_telegram(f'Видалені файли: {deleted_files}')
