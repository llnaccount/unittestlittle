import time
from business.datacreate import CreateNote
import requests
import unittest
from business.apire import get, post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from business.readfile import ReadFile
from common.logsmethod import case_log_init, class_case_log, info, error, step
from common.yamlread import YamlRead


@class_case_log
class GetNoteContentMajor(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getNoteContent']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_major(self):
        """ 获取便签内容，主流程 """
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
            "noteIds": note_ids
        }
        res = post(url=get_body_url, headers=headers, sid=self.sid1, json=data)
        self.assertEqual(200, res.status_code)
        expect = {
            "responseTime": int,
            "noteBodies": [
                {
                    "summary": data_msg[0]['summary'],
                    "noteId": data_msg[0]['noteId'],
                    "infoNoteId":data_msg[0]['noteId'],
                    "bodyType": 0,
                    "body": data_msg[0]['body'],
                    "contentVersion": 1,
                    "contentUpdateTime": int,
                    "title": data_msg[0]['title'],
                    "valid": 1
                }

            ]
        }
        CheckOutput().output_check(expect, res.json())
