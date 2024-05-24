from business.datacreate import CreateNote
import requests
import unittest
from business.apire import get,post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from common.logsmethod import  class_case_log, info, error, step
from common.yamlread import YamlRead

@class_case_log
class GetCalendarMajor(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getCalendarNote']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_major(self):
        """ 查看日历下便签主流程 """
        step("前置构建一条日历便签")
        data_msg = CreateNote().calendar_note(userid = self.userid1,sid = self.sid1,num =1)
        step("查看日历下便签")
        get_url = self.host + '/v3/notesvr/web/getnotes/remind'
        headers = {
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }
        data = {
            "remindStartTime": 1714535459,
            "remindEndTime": 1714967459,
            "startIndex": 0,
            "rows": 10
        }
        res = post(url=get_url, headers=headers, json=data,sid=self.sid1)
        print(res.json())
        self.assertEqual(200, res.status_code)
        expect = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": data_msg[0]['noteId'],
                    "createTime": int,
                    "star": 0,
                    "remindTime": "None",
                    "remindType": None,
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
        # CheckOutput().output_check(expect, res.json())























