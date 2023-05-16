# name:abetterweb3 招聘求职 #startupjobs ids:-1001572924402
# name:Elon Tweet Alert ids:-1001192924820
# name:方程式新闻 ids:-1001279597711
# name:ChatGPT工作室 ids:-1001576246806
from telethon import TelegramClient, events

from scraper_utils import analysis_musk, analysis_news, analysis_job

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = ''
api_hash = ''


client = TelegramClient('CryptBigBang', api_id, api_hash)
'''
channle_list = [
    -1001572924402,  # abetterweb3
    -1001192924820,  # Elon Tweet Alert
    -1001279597711,  # 方程式新闻
    -1001576246806   # ChatGPT工作室
]
'''


@client.on(events.NewMessage(chats = [-1001572924402]))
async def job_event_handler(event):
    analysis_job(event.text)
    print(event, event.text)


@client.on(events.NewMessage(chats = [-1001192924820]))
async def musk_event_handler(event):
    analysis_musk(event.text)
    print(event, event.text)


@client.on(events.NewMessage(chats = [-1001279597711]))
async def news_event_handler(event):
    analysis_news(event.text)
    print(event, event.text)


@client.on(events.NewMessage(chats = [-1001576246806]))
async def test_event_handler(event):
    print(event, event.text)


client.start()
client.run_until_disconnected()

