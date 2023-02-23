from twitchio.ext import commands
import requests
import datetime
import random
from datetime import timezone, datetime
from stream_check import stream_ping
from apscheduler.schedulers.background import BackgroundScheduler
from playsound import playsound




from env import ACCESS_TOKEN
wow_num = 0
url = 'http://127.0.0.1:5000/bot'
global broCount
broCount = 0
class Bot(commands.Bot):

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

    async def event_message(self, ctx):
        dt = datetime.now(timezone.utc)
        ts = dt.strftime("%Y/%m/%d %H:%M:%S.%f")
        
        if 'wow' in ctx.content and ctx.tags['room-id'] == '622249091':
            rand = random.randint(1, 12)
            wow_num = rand
            print(wow_num)
            if wow_num == 10:
                playsound('kawaii_wow.mp3')
                wow_num=0
            elif wow_num == 11:
                playsound('wowEddy.mp3')
            elif wow_num == 12:
                playsound('wowOwen01.mp3')
            else:
                print('wow')
                playsound('wow.mp3')
                
        if 'bro' in ctx.content and not 'brood' in ctx.content and ctx.tags['room-id'] == '622249091' or 'brah' in ctx.content and ctx.tags['room-id'] == '622249091' or 'bruh' in ctx.content and ctx.tags['room-id'] == '622249091' or 'broodv1Brud' in ctx.content and ctx.tags['room-id'] == '622249091':
            
            rand = "%02d" % random.randint(1, 55)
            print(ctx.content)
            print(rand )
            playsound('./audio/bro-{rand}.mp3'.format(rand=rand))
            global broCount
            if broCount == 0 or broCount == None:
                print('bro')
                broCount = 1
            elif broCount == 1:
                print('brobro')
                broCount = 2
            elif broCount == 2:
                print('brobrobro')
                broCount = 3
            elif broCount == 3:
                print('brobro')
                broCount = 0
        
        if 'lol' in ctx.content and ctx.tags['room-id'] == '622249091' or 'LOL' in ctx.content and ctx.tags['room-id'] == '622249091' or 'LUL' in ctx.content and ctx.tags['room-id'] == '622249091' or 'KEKW' in ctx.content and ctx.tags['room-id'] == '622249091' or "haha" in ctx.content and ctx.tags['room-id'] == '622249091' or "lmao" in ctx.content and ctx.tags['room-id'] == '622249091' or "LMAO" in ctx.content and ctx.tags['room-id'] == '622249091' or "LMFAO" in ctx.content and ctx.tags['room-id'] == '622249091' or "lmfao" in ctx.content and ctx.tags['room-id'] == '622249091': 

            f = open("brood.txt", "a")
            f.write(str(ts))
            f.write(': ')
            f.write(ctx.author.name)
            f.write(': ')
            f.write(ctx.content)
            f.write('\n')

            
        if 'lol' in ctx.content and ctx.tags['room-id'] == '171270662' or 'LOL' in ctx.content and ctx.tags['room-id'] == '171270662' or 'LUL' in ctx.content and ctx.tags['room-id'] == '171270662' or 'KEKW' in ctx.content and ctx.tags['room-id'] == '171270662' or "haha" in ctx.content and ctx.tags['room-id'] == '171270662' or "lmao" in ctx.content and ctx.tags['room-id'] == '171270662' or "LMAO" in ctx.content and ctx.tags['room-id'] == '171270662' or "LMFAO" in ctx.content and ctx.tags['room-id'] == '171270662' or "lmfao" in ctx.content and ctx.tags['room-id'] == '171270662': 
            
            f = open("throgg.txt", "a")
            f.write(str(ts))
            f.write(': ')
            f.write(ctx.author.name)
            f.write(': ')
            f.write(ctx.content)
            f.write('\n')

        
        if 'lol' in ctx.content and ctx.tags['room-id'] == '30009229' or 'LOL' in ctx.content and ctx.tags['room-id'] == '30009229' or 'LUL' in ctx.content and ctx.tags['room-id'] == '30009229' or 'KEKW' in ctx.content and ctx.tags['room-id'] == '30009229' or "haha" in ctx.content and ctx.tags['room-id'] == '30009229' or "lmao" in ctx.content and ctx.tags['room-id'] == '30009229' or "LMAO" in ctx.content and ctx.tags['room-id'] == '30009229' or "LMFAO" in ctx.content and ctx.tags['room-id'] == '30009229' or "lmfao" in ctx.content and ctx.tags['room-id'] == '30009229': 
            
            f = open("zheal.txt", "a")
            f.write(str(ts))
            f.write(': ')
            f.write(ctx.author.name)
            f.write(': ')
            f.write(ctx.content)
            f.write('\n')

        
        if 'lol' in ctx.content and ctx.tags['room-id'] == '42144849' or 'LOL' in ctx.content and ctx.tags['room-id'] == '42144849' or 'LUL' in ctx.content and ctx.tags['room-id'] == '42144849' or 'KEKW' in ctx.content and ctx.tags['room-id'] == '42144849' or "haha" in ctx.content and ctx.tags['room-id'] == '42144849' or "lmao" in ctx.content and ctx.tags['room-id'] == '42144849' or "LMAO" in ctx.content and ctx.tags['room-id'] == '42144849' or "LMFAO" in ctx.content and ctx.tags['room-id'] == '42144849' or "lmfao" in ctx.content and ctx.tags['room-id'] == '42144849': 
            
            f = open("kaze.txt", "a")
            f.write(str(ts))
            f.write(': ')
            f.write(ctx.author.name)
            f.write(': ')
            f.write(ctx.content)
            f.write('\n')

            
        

scheduler = BackgroundScheduler()
scheduler.add_job(stream_ping, 'interval', seconds=180)
scheduler.start()

bot = Bot()
bot.run()
