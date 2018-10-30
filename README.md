# 贴吧签到机 - CI 版

* 由百度非著名用户飞龙开发，开放给全部吧友进行使用。  
* 无缝对接 Travis CI，全自动全天候无人值守，智能监控，拒绝漏签。
* 模拟客户端签到，首签+6，连续+8。
* 永久开源，协议宽松。

## 用法

### 命令行

```
pip install -r requirement.txt
echo "你的 BDUSS" > cookie
python main.py
```

### Travis CI

（待补充）

## 获取Cookie（Chrome）

1. 首先在百度贴吧页面上登录你的账号。
2. 地址栏中输入`chrome://settings/cookies`。
3. 弹出的窗口右上角文本框中输入`tieba.com`。
4. 找到网站为`tieba.com`的项目，点击，再找到`BDUSS`标签，点击。
5. `内容`处就是需要的字符串，连同`BDUSS=`一起输入到页面上的文本框中。

![cookie](http://ww4.sinaimg.cn/large/841aea59gw1eirbls65ryj20k20ew759.jpg)

## 维护

由于百度贴吧可能频繁升级其接口，本程序的贴吧操作部分，即`tbops.py`中的所有贴吧操作函数均已添加文档字符串，有一定 Python 基础的用户可自行修改。

> 但事实证明，从我开始玩贴吧的 2012 年到现在，这些接口从来没有失效。

## 反馈

任何反馈请提交到 ISSUE。
