import time
import requests
from common.yamlread import YamlRead


class CreateNote:
    envConfig = YamlRead().env_config()
    host = envConfig['host']

    # 前置处理的封装：新建便签主体、新建便签内容
    def create_note(self, userid, sid, num):
        notes_list = []
        for i in range(num):
            # 前置
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f'wps_sid={sid}',
                'X-User-Key': str(userid)
            }
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id
            }
            res = requests.post(url=self.host + '/v3/notesvr/set/noteinfo', headers=headers, json=body)
            infoVersion = res.json()['infoVersion']
            data = {
                "noteId": note_id,
                "title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": infoVersion,
                "BodyType": 0

            }
            notes_list.append(data)
            requests.post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=data)
        return notes_list

    def calendar_note(self, userid, sid, num):
        notes_list = []
        for i in range(num):
            # 前置
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f'wps_sid={sid}',
                'X-User-Key': str(userid)
            }
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id,
                "remindTime":1714708259,
                "remindType":1
            }
            res = requests.post(url=self.host + '/v3/notesvr/set/noteinfo', headers=headers, json=body)
            infoVersion = res.json()['infoVersion']
            data = {
                "noteId": note_id,
                "title": "test2",
                "summary": "test2",
                "body": "test2",
                "localContentVersion": infoVersion,
                "BodyType": 0

            }
            notes_list.append(data)
            requests.post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=data)
        return notes_list
