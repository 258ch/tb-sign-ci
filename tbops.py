# coding: utf-8

import requests
import json
import hashlib

default_hdr = {
    "Accept": "*/*",
    "Accept-Language": "zh-cn",
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cache-Control": "no-cache"
}

def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest().upper()

def urlencode(s):
    bts = s.encode('utf-8')
    res = []
    for b in bts:
        res.append('%' + hex(b)[2:])
    return ''.join(res).upper()

def get_tbs(cookie):
    '''
    参数
    ----
    cookie: str
        贴吧 Cookie，格式为 BDUSS.{192}。
    
    返回值
    ------
    out: str 或 None
        成功时为 tbs，失败时为 None。
    '''
    hdr = default_hdr.copy()
    hdr['Cookie'] = cookie

    res_str = requests.get("http://tieba.baidu.com/dc/common/tbs", headers=hdr).text
    j = json.loads(res_str)
    if j['is_login'] == 0:
        return None
    return j['tbs']
    
def test_login(cookie):
    '''
    参数
    ----
    cookie: str
        贴吧 Cookie，格式为 BDUSS.{192}。
    
    返回值
    ------
    out: bool
        是否已登录。
    '''
    return get_tbs(cookie) is not None
    
def get_fid(tb_name):
    '''
    参数
    ----
    tb_name: str
        贴吧名称。
    
    返回值
    ------
    out: str
        贴吧 FID。
    '''
    url = "http://tieba.baidu.com/f/commit/share/fnameShareApi?fname=" \
        + urlencode(tb_name) + "&ie=utf-8"
    res_str = requests.get(url, headers=default_hdr).text
    j = json.loads(res_str)
    return str(j["data"]["fid"])

def get_tb_list(cookie):
    '''
    参数
    ----
    cookie: str
        贴吧 Cookie，格式为 BDUSS.{192}。
    
    返回值
    ------
    out: dict
    out['errno']: str
        表示是否成功，"0" 为成功，其余为不成功。
    out['list']: list, 可选
        贴吧列表，成功时出现。
    out['errmsg']: str, 可选
        错误信息，不成功时出现。
    '''
    post_str = cookie + "&_client_id=&_client_type=2&_client_version=5.7.0" \
        + "&_phone_imei=000000000000000&from=tieba"
    sign = md5(post_str.replace("&", "") + "tiebaclient!!!")
    post_str += "&sign=" + sign
    
    res_str = requests.post("http://c.tieba.baidu.com/c/f/forum/like", \
        data=post_str, headers=default_hdr).text
    j = json.loads(res_str)
    
    errno = j["error_code"]
    if errno != "0":
        return {"errno": errno, \
                "errmsg": j["error_msg"]}
    if not j['forum_list']:
        return {"errno": "1", "errmsg": "用户未登录或已掉线"}
    
    li = []
    for elem in j['forum_list']['non-gconforum']:
        li.append(elem['name'])
    for elem in j['forum_list']['gconforum']:
        li.append(elem['name'])
    return {"errno": "0", "list": li}
    
def get_un(cookie):
    '''
    参数
    ----
    cookie: str
        贴吧 Cookie，格式为 BDUSS.{192}。
    
    返回值
    ------
    out: str 或 None
        成功时为用户名，不成功时为 None。
    '''
    hdr = default_hdr.copy()
    hdr['Cookie'] = cookie
    
    res_str = requests.get('http://tieba.baidu.com/i/sys/user_json', headers=hdr) \
        .content.decode('gbk')
    
    if res_str == "":
        return None
        
    j = json.loads(res_str)
    return j['raw_name']
    
def tb_sign(cookie, tb_name):
    '''
    参数
    ----
    cookie: str
        贴吧 Cookie，格式为 BDUSS.{192}。
    tb_name: str
        贴吧名称。
    
    返回值
    ------
    out: dict
    out['error_code']: str
        表示是否成功，0 为成功，其余为不成功。
    out['error_msg']: str, 可选
        错误信息，不成功时出现。
    '''
    tbs = get_tbs(cookie)
    fid = get_fid(tb_name)
    
    post_str = cookie + "_client_id=_client_type=2_client_version=2.5.1" \
        + "_phone_imei=000000000000000fid=" \
        + fid + "from=tiebakw=" \
        + tb_name + "net_type=1tbs=" + tbs + "tiebaclient!!!"
    sign = md5(post_str)
    
    post_str = cookie + "&_client_id=&_client_type=2&_client_version=2.5.1" \
        + "&_phone_imei=000000000000000&fid=" \
        + fid + "&from=tieba&kw=" \
        + urlencode(tb_name) + "&net_type=1&tbs=" + tbs \
        + "&sign=" + sign
    res_str = requests.post('http://c.tieba.baidu.com/c/c/forum/sign', \
        data=post_str, headers=default_hdr).text
    j = json.loads(res_str)
    return j
