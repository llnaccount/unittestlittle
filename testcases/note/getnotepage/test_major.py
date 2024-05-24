import time
from business.datacreate import CreateNote
import requests
import unittest
from business.apire import get, post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from common.logsmethod import case_log_init, class_case_log, info, error, step
from common.yamlread import YamlRead


@class_case_log
class GetNotePageMajor(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getNotePage']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_major(self):
        """ 获取首页便签，主流程 """
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        headers = {
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }

        res = get(url=get_list_url, headers=headers, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": data_msg[0]['noteId'],
                    "createTime": int,
                    "star": 0,
                    "remindTime": 0,
                    "remindType": 0,
                    "infoVersion": 1,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": data_msg[0]['title'],
                    "summary": data_msg[0]['summary'],
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }

            ]
        }
        CheckOutput().output_check(expect, res.json())
