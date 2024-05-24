import string
import unittest
from common.yamlread import YamlRead
from parameterized import parameterized
from business.apire import get,post
from business.dataclear import DataClear
from business.checkoutput import CheckOutput
from common.logsmethod import case_log_init, class_case_log, info, error, step
from business.datacreate import CreateNote


@class_case_log
class DeleteNoteInput(unittest.TestCase):
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['deleteNote']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    path = '/v3/notesvr/delete'
    mustKey = dataConfig['mustKeys']
    key = mustKey[0]['noteId']

    def setUp(self):
        DataClear().note_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_empty_str(self):
        """ 删除便签，必填项校验：noteId为空 """
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        get_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        del_url = self.host + '/v3/notesvr/delete'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }
        # 获取用户下的所有便签数据
        step("前置获取用户下的所有便签数据")
        get_res = get(url=get_url, headers=headers, sid=self.sid1)
        note_ids = []
        for item in get_res.json()['webNotes']:
            note_ids.append(item['noteId'])

        step("删除所有便签数据")
        for noteId in note_ids:
            body = {
                'noteId': ""
            }
            res = post(url=del_url, headers=headers, json=body, sid=self.sid1)
            self.assertEqual(500, res.status_code)


    @parameterized.expand(key)
    def testCase02_str_type(self,noteid):
        """ 删除便签，数据类型校验 """
        step("前置构建一条便签数据")
        data_msg = CreateNote().create_note(userid=self.userid1, sid=self.sid1, num=1)
        get_url = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/0/rows/99/notes'
        del_url = self.host + '/v3/notesvr/delete'
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'wps_sid={self.sid1}',
            'X-User-Key': f'{self.userid1}'
        }
        # 获取用户下的所有便签数据
        step("前置获取用户下的所有便签数据")
        get_res = get(url=get_url, headers=headers, sid=self.sid1)
        note_ids = []
        for item in get_res.json()['webNotes']:
            note_ids.append(item['noteId'])

        step("删除所有便签数据")
        for noteId in note_ids:
            body = {
                'noteId': noteid
            }
            res = post(url=del_url, headers=headers, json=body, sid=self.sid1)
            self.assertEqual(500, res.status_code)



