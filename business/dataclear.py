import requests
from common.yamlread import YamlRead


class DataClear:
    envConfig = YamlRead().env_config()
    host = envConfig['host']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']

    # def group_clear(self, sid, user_id):
    #     # 获取当前用户所有的有效分组
    #     url = self.host + '/v3/notesvr/get/notegroup'
    #     headers = {
    #         'Cookie': f'wps_sid={sid}',
    #         'X-User-Key': f'{user_id}'
    #     }
    #     data = {"excludeInvalid": True}
    #     get_res = requests.post(url, headers=headers, json=data)
    #     for group in get_res.json()['noteGroups']:
    #         group_id = group['groupId']
    #         del_url = ''
    #         data = {
    #             'groupId': group_id
    #         }
    #         del_res = requests.post(url=del_url, headers=headers, json=data)
    #         print(del_res.status_code)
    #         if del_res.status_code != 200:
    #             return False
    #     return True

    def note_clear(self, sid, user_id):
        get_note_url = self.host + f'/v3/notesvr/user/{user_id}/home/startindex/0/rows/99/notes'
        del_note_url = self.host + '/v3/notesvr/delete'
        clear_note_url = self.host + '/v3/notesvr/cleanrecyclebin'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'wps_sid={sid}',
            'X-User-Key': str(user_id)
        }
        # 获取用户下的所有便签数据
        get_note_res = requests.get(url=get_note_url, headers=headers)
        note_ids = []
        for item in get_note_res.json()['webNotes']:
            note_ids.append(item['noteId'])

        # 删除便签
        for noteId in note_ids:
            body = {
                'noteId': noteId
            }
            del_note_res = requests.post(url=del_note_url, headers=headers, json=body)
            assert del_note_res.status_code == 200
            print(del_note_res.json(),del_note_res.status_code)

        clear_body = {
            'noteIds': ['-1']
        }
        clear_res = requests.post(url=clear_note_url, headers=headers, json=clear_body)
        assert clear_res.status_code == 200
        print(clear_res.json())

# if __name__ == '__main__':
#     DataClear().note_clear(DataClear().sid1,DataClear().userid1)