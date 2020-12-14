import os
from shutil import disk_usage
from datetime import datetime, timedelta

from telegram_sender import send_telegram

path = 'H:\\media'

total, used, free = disk_usage(path)

if free / total < 0.1:
    delta_time = f'{datetime.now() - timedelta(days=12):%Y%m%d}'
    """delta_time: - время хранения файлов ос сегоднешнего дня"""
    if os.path.exists(path):
        if os.path.isdir(path):
            for file in os.listdir(path=path):
                if int(delta_time) > int((datetime.fromtimestamp((os.path.getctime(path+'\\'+file))).strftime('%Y%m%d'))):
                    os.remove(f'{path}\\{file}')
    send_telegram(f"Files created before {delta_time} - are deleted")


