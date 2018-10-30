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
    hdr = default_hdr.copy()
    hdr['Cookie'] = cookie

    res_str = requests.get("http://tieba.baidu.com/dc/common/tbs", headers=hdr).text
    j = json.loads(res_str)
    if j['is_login'] == 0:
        return None
    return j['tbs']
    
def test_login(cookie):
    return get_tbs(cookie) is not None
    
def get_fid(tb_name):

    url = "http://tieba.baidu.com/f/commit/share/fnameShareApi?fname=" \
        + urlencode(tb_name) + "&ie=utf-8"
    res_str = requests.get(url).text
    j = json.loads(res_str)
    return str(j["data"]["fid"])

def get_tb_list(cookie):
    
    post_str = cookie + "&_client_id=&_client_type=2&_client_version=5.7.0" \
        + "&_phone_imei=000000000000000&from=tieba"
    sign = md5(post_str.replace("&", "") + "tiebaclient!!!")
    post_str += "&sign=" + sign
    
    res_str = requests.post("http://c.tieba.baidu.com/c/f/forum/like", data=post_str).text
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
    hdr = default_hdr.copy()
    hdr['Cookie'] = cookie
    
    res_str = requests.get('http://tieba.baidu.com/i/sys/user_json', headers=hdr).content.decode('gbk')
    
    if res_str == "":
        return None
        
    j = json.loads(res_str)
    return j['raw_name']
    
def tb_sign(cookie, tb_name):
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
    res_str = requests.post('http://c.tieba.baidu.com/c/c/forum/sign', data=post_str).text
    j = json.loads(res_str)
    return j
