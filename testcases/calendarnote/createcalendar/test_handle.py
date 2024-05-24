import time

import unittest
from business.apire import get, post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from common.logsmethod import class_case_log, info, error, step
from common.yamlread import YamlRead


@class_case_log
class CreateCalendarHandle(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['createCalendar']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    num = 1
    userid2 = envConfig['userid2']
    sid2 = envConfig['sid2']
    headers = {
        'Cookie': f'wps_sid={sid1}',
        'X-User-Key': f'{userid1}'
    }

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_limit(self):
        """ 新建日历便签内容主流程 """
        for i in range(self.num):
            step("前置新建日历便签主体")
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id,
                "star": 0,
                "remindTime": 1714708259,
                "remindType": 1
            }
            res = post(url=self.host + '/v3/notesvr/set/noteinfo', headers=self.headers, json=body, sid=self.sid1)

            step("新建日历便签内容")
            headers = {
                'Cookie': f'wps_sid={self.sid2}',
                'X-User-Key': f'{self.userid2}'
            }
            infoversion = res.json()['infoVersion']
            data = {
                "noteId": note_id,
                "title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": infoversion,
                "BodyType": 0

            }
            res = post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=data, sid=self.sid2)
            self.assertEqual(401, res.status_code)
