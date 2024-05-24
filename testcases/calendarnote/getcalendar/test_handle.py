from business.datacreate import CreateNote
import requests
import unittest
from business.apire import get,post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from common.logsmethod import  class_case_log, info, error, step
from common.yamlread import YamlRead

@class_case_log
class GetCalendarHandle(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getCalendarNote']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    userid2 = envConfig['userid2']
    sid2 = envConfig['sid2']
    headers = {
        'Cookie': f'wps_sid={sid1}',
        'X-User-Key': f'{userid1}'
    }

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_limit(self):
        """ 权限校验：未授权用户是否能够删除A用户的便签"""
        step("前置构建一条日历便签")
        data_msg = CreateNote().calendar_note(userid = self.userid1,sid = self.sid1,num =1)
        step("查看日历下便签")
        get_url = self.host + '/v3/notesvr/web/getnotes/remind'
        headers = {
            'Cookie': f'wps_sid={self.sid2}',
            'X-User-Key': f'{self.userid2}'
        }
        data = {
            "remindStartTime": 1714535459,
            "remindEndTime": 1714967459,
            "startIndex": 0,
            "rows": 10
        }
        res = post(url=get_url, headers=headers, json=data,sid=self.sid2)
        self.assertEqual(401, res.status_code)























