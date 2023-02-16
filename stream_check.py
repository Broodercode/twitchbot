import requests
from env import BEARER, CLIENT_ID, STREAM_DATA_URL
from datetime import timezone, datetime

print('app scheduler reached')
stream_dataset = None
stream_temp = []
stream_online = []
stream_offline = []
online_check = []
end_data = {}
stream_data_url = STREAM_DATA_URL


def stream_ping():
    print('tick')
    url = 'https://api.twitch.tv/helix/streams?user_login=yogidamonk&user_login=eatitup_86&user_login=zheal&user_login=broodvx&user_login=throggtv'
    headers = {'Authorization': BEARER, 'Client-Id': CLIENT_ID}
    res = requests.get(url=url, headers=headers).json()
    data = res['data']
    print(len(data))
    print(data)
    global stream_dataset
    global stream_temp
    global stream_offline
    global stream_online
    global online_check
    global end_data
    if stream_dataset == None:
        print('stream data updated')
        stream_dataset = data[:]

    if len(stream_temp) != 0:
        stream_temp = []
        print(stream_temp)
    if len(online_check) != 0:
        online_check = []
    for i in stream_dataset:

        for j in data:
            if i['user_login'] == j['user_login']:
                print(f'{i["user_login"]} is still logged in')
                dt = datetime.now(timezone.utc)
                ts = dt.strftime("%Y/%m/%d %H:%M:%S.%f")
                stream_data = {
                    'started_at': i['started_at'],
                    'stream_id': i['id'],
                    'user_id': i['user_id'],
                    'viewer_count': i['viewer_count'],
                    'user_login': i['user_login'],
                    'log_time': ts
                }
                online_data = {
                    'stream_id': i['id'],
                    'user_id': i['user_id'],
                    
                }

                stream_temp.append(stream_data)
                online_check.append(online_data)
    print('post request')
    requests.post(stream_data_url, json=stream_temp)

    if online_check != stream_online:
        for i in stream_online:
            if i not in online_check:
                curCT = datetime.now(timezone.utc)
                curTS = curCT.strftime("%Y/%m/%d %H:%M:%S.%f")
                end_data = {
                    'room_id': i['user_id'],
                    'stream_id': i['stream_id'],
                    'ended_at': curTS,
                }
                requests.patch(stream_data_url, json=end_data)

                print(end_data)

    stream_online = online_check
    stream_dataset = data[:]