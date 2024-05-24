import requests
import unittest
from business.apire import get, post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from business.readfile import ReadFile
from business.datacreate import CreateNote
from common.logsmethod import case_log_init, class_case_log, info, error, step
from common.yamlread import YamlRead


@class_case_log
class GetNoteContentHandle(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getNoteContent']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    userid2 = envConfig['userid2']
    sid2 = envConfig['sid2']
    host = envConfig['host']
    headers = {
        'Cookie': f'wps_sid={sid1}',
        'X-User-Key': f'{userid1}'
    }

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)


    def testCase01_major(self):
        """ 权限校验：未授权用户是否能够查看A用户的便签内容"""
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)

        step("前置获取用户下的所有便签数据")
        get_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        get_res = get(url=get_url, headers=self.headers, sid=self.sid1)
        note_ids = []
        for item in get_res.json()['webNotes']:
            note_ids.append(item['noteId'])

        step("获取用户下的所有便签内容")
        headers = {
            'Cookie': f'wps_sid={self.sid2}',
            'X-User-Key': f'{self.userid2}'
        }
        get_body_url = self.host + '/v3/notesvr/get/notebody'
        data = {
            "noteIds": note_ids
        }
        res = post(url=get_body_url, headers=headers, sid=self.sid2, json=data)
        self.assertEqual(401, res.status_code)

        # CheckOutput().output_check(expect, res.json())