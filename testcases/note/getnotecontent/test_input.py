from parameterized import parameterized
from business.datacreate import CreateNote
import unittest
from business.apire import get, post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from common.logsmethod import case_log_init, class_case_log, info, error, step
from common.yamlread import YamlRead


@class_case_log
class GetNoteContentInput(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getNoteContent']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    mustKey = dataConfig['mustKeys']  # 值为列表
    key = mustKey[0]['noteIds']  # 从列表中取值
    headers = {
        'Cookie': f'wps_sid={sid1}',
        'X-User-Key': f'{userid1}'
    }


    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_empty_list(self):
        """ 获取便签内容，必填字段校验, noteids 为 [''] """
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        headers = {
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }

        step("前置获取用户下的所有便签数据")
        get_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        get_res = get(url=get_url, headers=headers, sid=self.sid1)
        note_ids = []
        for item in get_res.json()['webNotes']:
            note_ids.append(item['noteId'])

        step("获取用户下的所有便签内容")
        get_body_url = self.host + '/v3/notesvr/get/notebody'
        data = {
            "noteIds": ['']
        }
        res = post(url=get_body_url, headers=headers, sid=self.sid1, json=data)
        self.assertEqual(200, res.status_code)

    def testCase02_empty_dict(self):
        """ 获取便签内容，必填字段校验, noteids 为 [''] """
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        headers = {
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }

        step("前置获取用户下的所有便签数据")
        get_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        get_res = get(url=get_url, headers=headers, sid=self.sid1)
        note_ids = []
        for item in get_res.json()['webNotes']:
            note_ids.append(item['noteId'])

        step("获取用户下的所有便签内容")
        get_body_url = self.host + '/v3/notesvr/get/notebody'
        data = {
            "noteIds": {}
        }
        res = post(url=get_body_url, headers=headers, sid=self.sid1, json=data)
        self.assertEqual(500, res.status_code)

    def testCase03_empty_list(self):
        """ 获取便签内容，必填字段校验, noteids 为 [''] """
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        headers = {
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }

        step("前置获取用户下的所有便签数据")
        get_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        get_res = get(url=get_url, headers=headers, sid=self.sid1)
        note_ids = []
        for item in get_res.json()['webNotes']:
            note_ids.append(item['noteId'])

        step("获取用户下的所有便签内容")
        get_body_url = self.host + '/v3/notesvr/get/notebody'
        data = {
            "noteIds": []
        }
        res = post(url=get_body_url, headers=headers, sid=self.sid1, json=data)
        self.assertEqual(500, res.status_code)

    def testCase04_list(self):
        """ 获取便签内容，必填字段校验, noteids 为 [''] """
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        headers = {
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }

        step("前置获取用户下的所有便签数据")
        get_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        get_res = get(url=get_url, headers=headers, sid=self.sid1)
        note_ids = []
        for item in get_res.json()['webNotes']:
            note_ids.append(item['noteId'])

        step("获取用户下的所有便签内容")
        get_body_url = self.host + '/v3/notesvr/get/notebody'
        data = {
            "noteIds": [234, [123, 123]]
        }
        res = post(url=get_body_url, headers=headers, sid=self.sid1, json=data)
        self.assertEqual(500, res.status_code)



    @parameterized.expand(key)
    def testCase05_list_type(self, noteids):
        """ 获取便签内容，数据类型校验 """
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        headers = {
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }

        step("前置获取用户下的所有便签数据")
        get_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        get_res = get(url=get_url, headers=headers, sid=self.sid1)
        note_ids = []
        for item in get_res.json()['webNotes']:
            note_ids.append(item['noteId'])


        step("获取用户下的所有便签内容")
        get_body_url = self.host + '/v3/notesvr/get/notebody'
        data = {
            "noteIds": noteids
        }
        res = post(url=get_body_url, headers=headers, sid=self.sid1, json=data)

        self.assertEqual(500, res.status_code)





