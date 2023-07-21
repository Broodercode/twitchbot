from twitchio.ext import commands
import requests
import datetime
import random
from datetime import timezone, datetime
from stream_check import stream_ping 
from apscheduler.schedulers.background import BackgroundScheduler
from playsound import playsound

from env import ACCESS_TOKEN 

class Bot(commands.Bot):
    wow_num = 0
    broCount = 0

    def __init__(self):
        super().__init__(token=ACCESS_TOKEN, prefix='', initial_channels=[
            'zheal',
            'yogidamonk',
            'broodvx',
            'kazenone'
        ])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, ctx):
        self.log_message(ctx)
        self.handle_wow(ctx)
        self.handle_bro(ctx)
        self.handle_broodv1Brud(ctx)
        self.log_lol(ctx)

    def log_message(self, ctx):
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

        try:
            # Replace with your own url
            url = 'http://127.0.0.1:5000/bot'
            requests.post(url, json=data)
        except Exception as e:
            print(f"Failed to post message data: {e}")

        print(f'{ctx.author.name}: {ctx.content}')

    def handle_wow(self, ctx):
        if 'wow' in ctx.content and ctx.tags['room-id'] == '622249091':
            rand = random.randint(1, 12)
            self.wow_num = rand
            print(self.wow_num)

            if self.wow_num == 10:
                playsound('kawaii_wow.mp3')
                self.wow_num=0
            elif self.wow_num == 11:
                playsound('wowEddy.mp3')
            elif self.wow_num == 12:
                playsound('wowOwen01.mp3')
            else:
                print('wow')
                playsound('wow.mp3')

    def handle_bro(self, ctx):
        if ('bro' in ctx.content and not 'brood' in ctx.content and ctx.tags['room-id'] == '622249091') or \
           ('brah' in ctx.content and ctx.tags['room-id'] == '622249091') or \
           ('bruh' in ctx.content and ctx.tags['room-id'] == '622249091') or \
           ('breh' in ctx.content and ctx.tags['room-id'] == '622249091') or \
           ('bruv' in ctx.content and ctx.tags['room-id'] == '622249091'):

            rand = "%02d" % random.randint(1, 55)
            print(ctx.content)
            print(rand)


            playsound(f'./audio/bro-{rand}.mp3')

            if self.broCount == 0 or self.broCount is None:
                print('bro')
                self.broCount = 1
            elif self.broCount == 1:
                print('brobro')
                self.broCount = 2
            elif self.broCount == 2:
                print('brobrobro')
                self.broCount = 3
            elif self.broCount == 3:
                print('brobro')
                self.broCount = 0

    def handle_broodv1Brud(self, ctx):
        if 'broodv1Brud' in ctx.content and ctx.tags['room-id'] == '622249091':
            print(ctx.content)

            playsound('./audio/broodDerp.mp3')

    def log_lol(self, ctx):
        lol_keywords = ['lol', 'LOL', 'LUL', 'KEKW', 'haha', 'lmao', 'LMAO', 'LMFAO', 'lmfao']
        room_ids = ['622249091', '171270662', '30009229', '42144849']
        filenames = ['brood.txt', 'throgg.txt', 'zheal.txt', 'kaze.txt']

        for keyword, room_id, filename in zip(lol_keywords, room_ids, filenames):
            if keyword in ctx.content and ctx.tags['room-id'] == room_id:
                dt = datetime.now(timezone.utc)
                ts = dt.strftime("%Y/%m/%d %H:%M:%S.%f")

                with open(filename, "a") as f:
                    f.write(f"{ts}: {ctx.author.name}: {ctx.content}\n")

scheduler = BackgroundScheduler() 
scheduler.add_job(stream_ping, 'interval', seconds=180) 
scheduler.start()

bot = Bot()
bot.run()
