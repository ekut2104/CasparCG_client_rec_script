import requests
import os


def send_telegram(text: str):
    token = os.getenv("TOKEN")
    url = "https://api.telegram.org/bot"
    channel_id = "@VC2_rss"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")


if __name__ == '__main__':
    send_telegram("Тестова розсилка")
