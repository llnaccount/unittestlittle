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


@class_case_log
class GetNotePageHandle(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['getNotePage']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    userid2 = envConfig['userid2']
    sid2 = envConfig['sid2']
    host = envConfig['host']
    headers = {
        'Cookie': f'wps_sid={sid1}',
        'X-User-Key': f'{userid1}'
    }

    expectBase = {
        "responseTime": int,
        "webNotes": [
            {
                "noteId": str,
                "createTime": int,
                "star": 0,
                "remindTime": 0,
                "remindType": int,
                "infoVersion": 1,
                "infoUpdateTime": int,
                "groupId": None,
                "title": str,
                "summary": str,
                "thumbnail": None,
                "contentVersion": 1,
                "contentUpdateTime": int
            },{
                "noteId": str,
                "createTime": int,
                "star": 0,
                "remindTime": 0,
                "remindType": int,
                "infoVersion": 1,
                "infoUpdateTime": int,
                "groupId": None,
                "title": str,
                "summary": str,
                "thumbnail": None,
                "contentVersion": 1,
                "contentUpdateTime": int
            }]
    }

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_startindex(self):
        """ 获取首页便签，startindex约束场景校验，存在2条便签数据，startindex的值为1"""
        step("前置构建2条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=2)
        step("获取首页便签")
        startindex = 1
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(get_list_url, headers=self.headers, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": str,
                    "createTime": int,
                    "star": 0,
                    "remindTime": 0,
                    "remindType": int,
                    "infoVersion": 1,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": str,
                    "summary": str,
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }]}
        CheckOutput().output_check(expect, res.json())

    def testCase02_startindex(self):
        """ 获取首页便签，startindex约束场景校验，存在2条便签数据，startindex的值为0"""
        step("前置构建2条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=2)
        step("获取首页便签")
        startindex = 0
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(get_list_url, headers=self.headers, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = deepcopy(self.expectBase)
        CheckOutput().output_check(expect, res.json())


    def testCase03_rows(self):
        """ 获取首页便签，rows约束场景校验，存在1条便签数据，rows的值为0"""
        step("前置构建1条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        startindex = 0
        rows = 0
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(get_list_url, headers=self.headers, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": str,
                    "createTime": int,
                    "star": 0,
                    "remindTime": 0,
                    "remindType": int,
                    "infoVersion": 1,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": str,
                    "summary": str,
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }]}
        CheckOutput().output_check(expect, res.json())

    def testCase04_rows(self):
        """ 获取首页便签，rows约束场景校验，存在2条便签数据，rows的值为1"""
        step("前置构建2条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=2)
        step("获取首页便签")
        startindex = 0
        rows = 1
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(get_list_url, headers=self.headers, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = {
            "responseTime": int,
            "webNotes": [
                {
                    "noteId": str,
                    "createTime": int,
                    "star": 0,
                    "remindTime": 0,
                    "remindType": int,
                    "infoVersion": 1,
                    "infoUpdateTime": int,
                    "groupId": None,
                    "title": str,
                    "summary": str,
                    "thumbnail": None,
                    "contentVersion": 1,
                    "contentUpdateTime": int
                }]}
        CheckOutput().output_check(expect, res.json())

    def testCase05_statuslimit(self):
        """ 状态限制：被清空的便签状态限制场景校验，清空便签数据后返回便签列表为空"""
        step("前置构建1条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=2)
        step("删除并清空回收站便签数据")
        data_result = DataClear().note_clear(user_id=self.userid1, sid=self.sid1)
        step("获取首页便签")
        startindex = 0
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(get_list_url, headers=self.headers, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = deepcopy(self.expectBase)
        expect['webNotes'] = []
        CheckOutput().output_check(expect, res.json())

    def testCase06_nums(self):
        """ 不同的处理数量校验：存在2条便签数据，则返回两条便签"""
        step("前置构建2条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=2)
        print(data_msg)
        step("获取首页便签")
        startindex = 0
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(get_list_url, headers=self.headers, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = deepcopy(self.expectBase)
        CheckOutput().output_check(expect, res.json())


    def testCase07_nums(self):
        """ 不同的处理数量校验：存在0条便签数据，则返回0条便签"""
        step("获取首页便签")
        startindex = 0
        rows = 10
        get_list_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(get_list_url,headers=self.headers, sid=self.sid1)
        self.assertEqual(200, res.status_code)
        expect = deepcopy(self.expectBase)
        expect['webNotes'] = []
        CheckOutput().output_check(expect, res.json())

    def testCase08_limits(self):
        """ 权限校验：未授权用户是否能够查看A用户的便签"""
        step("前置构建1条便签数据")
        data_msg1 = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        step("获取首页便签")
        startindex = 0
        rows = 10
        headers = {
            'Cookie': f'wps_sid={self.sid2}',
            'X-User-Key': f'{self.userid2}'
        }
        get_list_url2 = self.host + f'/v3/notesvr/user/{self.userid2}/home/startindex/{startindex}/rows/{rows}/notes'
        res = get(url=get_list_url2, headers=headers,sid=self.sid2)
        self.assertEqual(401, res.status_code)



