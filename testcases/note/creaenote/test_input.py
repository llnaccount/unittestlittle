import time
import unittest
from parameterized import parameterized
from common.yamlread import YamlRead
from business.apire import get, post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from common.logsmethod import case_log_init, class_case_log, info, error, step
from business.datacreate import CreateNote


@class_case_log
class CreateNoteInput(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['createNote']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    mustKey = dataConfig['mustKeys']
    key = mustKey[0]['noteId']
    num = 1

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_empty_str(self):
        """ 新增便签内容，必填项校验noteid"""
        for i in range(self.num):
            step("前置新建便签主体")
            headers = {
                'Cookie': f'wps_sid={self.sid1}',
                'X-User-Key': f'{self.userid1}'
            }
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id
            }
            res = post(url=self.host + '/v3/notesvr/set/noteinfo', headers=headers, json=body, sid=self.sid1)
            step("新建便签内容")
            infoversion = res.json()['infoVersion']
            data = {
                "noteId": "",
                "title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": infoversion,
                "BodyType": 0

            }
            res = post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=data, sid=self.sid1)
            self.assertEqual(500, res.status_code)

    def testCase02_empty_str(self):
        """ 新增便签内容，必填项校验title"""
        for i in range(self.num):
            step("前置新建便签主体")
            headers = {
                'Cookie': f'wps_sid={self.sid1}',
                'X-User-Key': f'{self.userid1}'
            }
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id
            }
            res = post(url=self.host + '/v3/notesvr/set/noteinfo', headers=headers, json=body, sid=self.sid1)
            step("新建便签内容")
            infoversion = res.json()['infoVersion']
            data = {
                "noteId": note_id,
                "title": "",
                "summary": "test",
                "body": "test",
                "localContentVersion": infoversion,
                "BodyType": 0

            }
            res = post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=data, sid=self.sid1)
            self.assertEqual(500, res.status_code)

    def testCase03_empty_str(self):
        """ 新增便签内容，必填项校验summary"""
        for i in range(self.num):
            step("前置新建便签主体")
            headers = {
                'Cookie': f'wps_sid={self.sid1}',
                'X-User-Key': f'{self.userid1}'
            }
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id
            }
            res = post(url=self.host + '/v3/notesvr/set/noteinfo', headers=headers, json=body, sid=self.sid1)
            step("新建便签内容")
            infoversion = res.json()['infoVersion']
            data = {
                "noteId": note_id,
                "title": "test",
                "summary": "",
                "body": "test",
                "localContentVersion": infoversion,
                "BodyType": 0

            }
            res = post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=data, sid=self.sid1)
            self.assertEqual(500, res.status_code)

    @parameterized.expand(key)
    def testCase05_datatype(self, noteid):
        """ 新增便签内容，必填项数据类型校验noteid"""
        for i in range(self.num):
            step("前置新建便签主体")
            headers = {
                'Cookie': f'wps_sid={self.sid1}',
                'X-User-Key': f'{self.userid1}'
            }
            note_id = str(int(time.time() * 1000)) + '_noteId'
            body = {
                "noteId": note_id
            }
            res = post(url=self.host + '/v3/notesvr/set/noteinfo', headers=headers, json=body, sid=self.sid1)
            step("新建便签内容")
            infoversion = res.json()['infoVersion']
            data = {
                "noteId": noteid,
                "title": "test",
                "summary": "test",
                "body": "test",
                "localContentVersion": infoversion,
                "BodyType": 0

            }
            res = post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=data, sid=self.sid1)
            self.assertEqual(500, res.status_code)
