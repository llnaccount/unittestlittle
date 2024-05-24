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
from copy import deepcopy
from parameterized import parameterized


@class_case_log
class GetCalendarInput(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getCalendarNote']
    mustKey = dataConfig['mustKeys']  # 值为列表
    key = mustKey[0]['remindStartTime']  # 从列表中取值
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    expectBase = {
        "responseTime": int,
        "webNotes": [
            {
                "noteId": int,
                "createTime": int,
                "star": 0,
                "remindTime": int,
                "remindType": int,
                "infoVersion": 1,
                "infoUpdateTime": int,
                "groupId": None,
                "title": str,
                "summary": str,
                "thumbnail": None,
                "contentVersion": 1,
                "contentUpdateTime": int
            }

        ]
    }

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_starttime(self):
        """ 查看日历下便签，必填项校验: remindstarttime为 空 """
        step("前置构建1条日历便签数据")
        data_msg = CreateNote().calendar_note(userid=self.userid1, sid=self.sid1, num=1)

        step("查看日历下便签")
        get_url = self.host + '/v3/notesvr/web/getnotes/remind'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }
        data = {
            "remindStartTime": None,
            "remindEndTime": 1714967459,
            "startIndex": 0,
            "rows": 10
        }
        res = post(url=get_url, headers=headers, json=data, sid=self.sid1)
        self.assertEqual(412, res.status_code)
        self.assertIn("errorCode", res.json())
        self.assertIn("errorMsg", res.json())
        self.assertIn("remindTime Requested!", res.json()['errorMsg'])



    def testCase02_endtime(self):
        """ 查看日历下便签，必填项校验: remindendtime为 空 """
        step("前置构建1条日历便签数据")
        data_msg = CreateNote().calendar_note(userid=self.userid1, sid=self.sid1, num=1)

        step("查看日历下便签")
        get_url = self.host + '/v3/notesvr/web/getnotes/remind'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }
        data = {
            "remindStartTime": 1714535459,
            "remindEndTime": None,
            "startIndex": 0,
            "rows": 10
        }
        res = post(url=get_url, headers=headers, json=data,sid=self.sid1)
        self.assertIn("errorCode", res.json())
        self.assertIn("errorMsg", res.json())

    def testCase03_startindex(self):
        """ 查看日历下便签，必填项校验: startindex为 空 """
        step("前置构建1条日历便签数据")
        data_msg = CreateNote().calendar_note(userid=self.userid1, sid=self.sid1, num=1)

        step("查看日历下便签")
        get_url = self.host + '/v3/notesvr/web/getnotes/remind'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }
        data = {
            "remindStartTime": 1714535459,
            "remindEndTime": 1714967459,
            "startIndex": None,
            "rows": 10
        }
        res = post(url=get_url, headers=headers, json=data,sid=self.sid1)
        self.assertIn("errorCode", res.json())
        self.assertIn("errorMsg", res.json())

    def testCase04_row(self):
        """ 查看日历下便签，必填项校验: rows为 空 """
        step("前置构建1条日历便签数据")
        data_msg = CreateNote().calendar_note(userid=self.userid1, sid=self.sid1, num=1)

        step("查看日历下便签")
        get_url = self.host + '/v3/notesvr/web/getnotes/remind'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }
        data = {
            "remindStartTime": 1714535459,
            "remindEndTime": 1714967459,
            "startIndex": 0,
            "rows": None
        }
        res = post(url=get_url, headers=headers, json=data,sid=self.sid1)
        self.assertIn("errorCode", res.json())
        self.assertIn("errorMsg", res.json())





if __name__ == '__main__':
    pass
    # "remindStartTime": 1714535459,
    # "remindEndTime": 1714967459,