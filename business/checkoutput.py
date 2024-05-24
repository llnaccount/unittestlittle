import unittest

class CheckOutput(unittest.TestCase):
    def output_check(self,expect,actual):

        self.assertEqual(len(expect.keys()),len(actual.keys()),msg = "keys len error!")
        for k,v in expect.items():
            self.assertIn(k,actual.keys(),msg=f'expect key:【{k}】 not in response!')
            if isinstance(v,type):
                self.assertEqual(v,type(actual[k]),msg= f'key:【{k}】type error!')
            elif isinstance(v,dict):
                self.output_check(v,actual[k])
            elif isinstance(v,list):
                self.assertEqual(len(v),len(actual[k]),msg= f'key:【{k}】len error!')
                for i in range(len(v)):
                    if isinstance(v[i],type):
                        self.assertEqual(v[i],type(actual[k][i]),msg= f'key:【{v[i]}】type error!')
                    elif isinstance(v[i],dict):
                        self.output_check(v[i],actual[k][i])
                    else:
                        self.assertEqual(v[i],actual[k][i],msg=f'list value:【{v[i]}】value error!')
            else:
                self.assertEqual(v,actual[k],msg=f'key:【{k}】value error!')

    """
        通用的断言方法
        :param expect: 描述断言的期望值
        :param actual: 描述断言的实际结果
        :return:
     """
















