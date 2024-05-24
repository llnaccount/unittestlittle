import time
from business.datacreate import CreateNote
import requests
import unittest
from business.apire import get, post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from common.logsmethod import case_log_init, class_case_log, info, error, step
from common.yamlread import YamlRead
from copy import deepcopy
from parameterized import parameterized


@class_case_log
class GetNotePageInput(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getNotePage']
    mustKey = dataConfig['mustKeys']  # 值为列表
    key = mustKey[0]['startindex']  # 从列表中取值
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
                "remindTime": 0,
                "remindType": 0,
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

    def testCase01_startindex(self):
        """ 获取首页便签，必填项校验: startindex为 空 """
        step("前置构建1条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        startindex = None
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(url=get_list_url, sid=self.sid1)
        self.assertEqual(500, res.status_code)

    def testCase02_rows(self):
        """ 获取首页便签，必填项校验: rows为 空 """
        step("前置构建1条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        startindex = 0
        rows = None
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(url=get_list_url, sid=self.sid1)
        self.assertEqual(500, res.status_code)

    def testCase03_userid(self):
        """ 获取首页便签，必填项校验: userid为 空 """
        step("前置构建1条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        startindex = 0
        rows = 10
        self.userid1 = ''
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(url=get_list_url, sid=self.sid1)
        self.assertEqual(404, res.status_code)

    def testCase04_sid(self):
        """ 获取首页便签，必填项校验: sid为 空 """
        step("前置构建1条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        startindex = 0
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        self.sid1 = ''
        res = get(url=get_list_url, sid=self.sid1)
        self.assertEqual(401, res.status_code)

    def testCase05_sid(self):
        """ 获取首页便签，必填项校验: sid错误 """
        step("前置构建1条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        startindex = 0
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        self.sid1 = '12312387468687'
        res = get(url=get_list_url, sid=self.sid1)
        self.assertEqual(401, res.status_code)

    @parameterized.expand(key)
    def testCase06_type(self, startindex):
        """ 获取首页便签，必填项类型校验: startindex为int类型 """
        step("前置构建1条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(url=get_list_url, sid=self.sid1)
        expect = deepcopy(self.expectBase)
        if isinstance(startindex, int) and startindex >= 0 and startindex < 214748364:
            self.assertEqual(200, res.status_code)
            expect['webNotes'][0]['noteId'] = data_msg[0]['noteId']
            expect['webNotes'][0]['title'] = data_msg[0]['title']
            expect['webNotes'][0]['summary'] = data_msg[0]['summary']
        else:
            self.assertEqual(500, res.status_code,
                             f"Expected status code 400 for invalid startindex {startindex},status_code为{res.status_code}")


# startindex 为’‘，返回代码为404