import requests
from env import BEARER, CLIENT_ID, STREAM_DATA_URL
from datetime import timezone, datetime

print('app scheduler reached')
stream_dataset = None
stream_temp = []
stream_online = []
stream_offline = []
stream_data_url = STREAM_DATA_URL


def stream_ping():
    print('tick')
    url = 'https://api.twitch.tv/helix/streams?user_login=jay_cee&user_login=lackattack&user_login=theretrorunner&user_login=pojodin1&user_login=solarcell007&user_login=liftedsenses&user_login=eatitup_86&user_login=zheal&user_login=broodvx&user_login=ultrosgambini&user_login=throggtv&user_login=yogidamonk&user_login=dyne_nuitari&user_login=bdudegames&user_login=kazenone&user_login=keddril&user_login=broodvx&user_login=overswarm&user_login=antfoolish'
    headers = {'Authorization': BEARER, 'Client-Id': CLIENT_ID}
    res = requests.get(url=url, headers=headers).json()
    data = res['data']
    print(len(data))
    print(data)
    global stream_dataset
    global stream_temp
    global stream_offline
    global stream_online
    if stream_dataset == None:
        print('stream data updated')
        stream_dataset = data[:]

    if len(stream_temp) != 0:
        stream_temp = []
        print(stream_temp)
    for i in stream_dataset:

        for j in data:
            if i['user_login'] == j['user_login']:
                print(f'{i["user_login"]} is still logged in')
                stream_data = {
                    'started_at': i['started_at'],
                    'stream_id': i['id'],
                    'user_id': i['user_id'],
                    'viewer_count': i['viewer_count'],
                    'user_login': i['user_login'],
                }

                stream_temp.append(stream_data)

    requests.post(stream_data_url, json=stream_temp)

    if stream_temp != stream_online:
        for i in stream_online:
            if i not in stream_temp:

                dt = datetime.now(timezone.utc)
                ts = dt.strftime("%Y/%m/%d %H:%M:%S.%f")
                end_data = {
                    'room_id': i['user_id'],
                    'stream_id': i['stream_id'],
                    'started_at': i['started_at'],
                    'ended_at': ts,
                }
                requests.patch(stream_data_url, json=stream_temp)
                stream_offline.append(end_data)
                print(f'{i} has logged off')

        stream_online = stream_temp
    stream_dataset = data[:]
