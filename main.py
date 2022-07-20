from twitchio.ext import commands
import requests
import datetime
from datetime import timezone, datetime
from stream_check import stream_ping
from apscheduler.schedulers.background import BackgroundScheduler

from env import ACCESS_TOKEN

url = 'http://127.0.0.1:5000/bot'


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix='', initial_channels=[
            'zheal',
            'throggtv',
            'yogidamonk',
            'broodvx',
            'dyne_nuitari',
            'overswarm',
            'bdudegames',
            'antfoolish',
            'eatitup_86',
            'kazenone',
            'keddril',
            'solarcell007',
            'pojodin1',
            'theretrorunner',
        ])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, ctx):
        dt = datetime.now(timezone.utc)
        ts = dt.strftime("%Y/%m/%d %H:%M:%S.%f")

        user_id = str(ctx.author.id)
        user_handle = str(ctx.author.name)
        content = str(ctx.content)
        msg_id = str(ctx.tags['id'])
        room_id = str(ctx.tags['room-id'])
        created_at = str(ts)
        data = {"user_id": user_id, "content": content, "msg_id": msg_id,
                "room_id": room_id, "created_at": created_at, "user_handle": user_handle}
        requests.post(url, json=data)
        print(f'{ctx.author.name}: {ctx.content}')


scheduler = BackgroundScheduler()
scheduler.add_job(stream_ping, 'interval', seconds=180)
scheduler.start()

bot = Bot()
bot.run()
