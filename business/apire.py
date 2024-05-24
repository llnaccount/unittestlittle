import requests
from common.logsmethod import case_log_init, class_case_log, info, error, step


# 对请求方法的封装

def get(url, sid, headers=None):
    if headers is None:
        headers = {
            'Cookie': f'wps_sid={sid}'
        }
    info(f'【requests】url:{url}')
    info(f'【requests】headers:{headers}')
    try:
        res = requests.get(url=url, headers=headers, timeout=30)
    except TimeoutError:
        error('requests timeout!')
        return "requests timeout!"
    info(f'【response】code:{res.status_code}')
    info(f'【response】body:{res.text}')
    return res

def post(url, sid,headers = None, **kwargs):
    if headers is None:
        headers = {
            'Cookie': f'wps_sid={sid}'
        }
    info(f'【requests】url:{url}')
    info(f'【requests】headers:{headers}')
    body = kwargs.get('json', None)
    if body:
        # 将body转换为字符串并打印
        body_str = str(body)
        info(f'【requests】body:{body_str}')
    try:
        res = requests.post(url=url, headers=headers, **kwargs, timeout=30)
    except TimeoutError:
        error('requests timeout!')
        return "requests timeout!"
    info(f'【response】code:{res.status_code}')
    info(f'【response】body:{res.text}')
    return res