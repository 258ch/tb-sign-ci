# coding: utf-8

from tbops import *
import os.path
import time

def main():
    # 读取 Cookie
    if not os.path.exists('cookie'):
        print('Cookie 不存在')
        return
    with open('cookie') as f:
        cookie = f.read()
    # 检查是否掉线
    if not test_login(cookie):
        print('Cookie 已掉线')
        return
    # 读取贴吧列表
    res = get_tb_list(cookie)
    if(res['errno'] != '0'):
        print('读取贴吧列表失败：' + res['errmsg'])
        return
    li = res['list']
    # 签到
    for tb in li:
        res = tb_sign(cookie, tb)
        if res['error_code'] != '0':
            print(tb + '吧签到失败：' + res['error_msg'])
        else:
            print(tb + '吧签到成功')
        
        time.sleep(1)

if __name__ == '__main__':
    main()