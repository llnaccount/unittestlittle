import unittest
import os
# from BeautifulReport import BeautifulReport

DIR = os.path.dirname(os.path.abspath(__file__))
ENVIRON = 'Online'  # 'Online' -> 线上环境， ‘Offline’-> 测试环境

if __name__ == '__main__':
    run_pattern = 'smoking'  # all 全量测试用例执行 /smoking 冒烟测试执行 / 指定执行文件
    if run_pattern == 'all':
        pattern = 'test_*.py'
    elif run_pattern == 'smoking':
        pattern = 'test_major*.py'
    else:
        run_pattern = run_pattern + '.py'
    suite = unittest.defaultTestLoader.discover(start_dir='./testcases', pattern=pattern)
    unittest.TextTestRunner().run(suite)
    # result = BeautifulReport(suite)
    # result.report(filename='report.html', description='测试报告', report_dir='./')
