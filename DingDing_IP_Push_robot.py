# 2021年11月1日
# By：M0x1n
# Project Name: DingDing_IP_Push_robot
# 项目名： 钉钉公网推送机器人
import json
from urllib.request import urlopen
from json import load
from urllib import parse, request
from time import strftime, localtime
# from datetime import datetime
import time


# 取公网IP
def get_ip_a():
    my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
    # print('api.ipify.org', my_ip)
    print("Date >> 当前公网IP ", my_ip, "\n")
    return my_ip


def main_request(api_url, requests_data):
    req = request.Request(url=api_url, data=requests_data)
    req.add_header('Content-Type', 'application/json')
    r = request.urlopen(req)
    r_data = r.read().decode('utf-8')
    return r_data


# 启动提醒
def tips():
    IP_A = get_ip_a()
    Time_A = strftime("%Y-%m-%d %H:%M:%S", localtime())
    # 2021年11月1日
    # By：M0x1n
    # Project Name: DingDing_IP_Push_robot
    # 项目名： 钉钉公网推送机器人
    print(" 2021年11月1日\n",
          "By：M0x1n\n",
          "Project Name: DingDing_IP_Push_robot\n",
          "项目名： 钉钉公网推送机器人")
    api_url = "https://oapi.dingtalk.com/robot/send?access_token="
    requests_data = json.dumps({
        "msgtype": "markdown",
        "markdown": {
            "title": "IP定时通知测试",
            "text": "#### 启动监控服务： \n > 公网IP：" + IP_A + "\n > \n > 系统时间：" + Time_A + " \n > \n > ![screenshot](https://bbs.moxinwangluo.cn/logo1.png)\n > ###### M0x1n本地服务器 [机器人](https://pan.moxinwangluo.cn) \n"
        }
        # "at": {
        #   "atMobiles": [
        #      "150XXXXXXXX"
        # ],
        # "atUserIds": [
        #    "user123"
        # ],
        # "isAtAll": 'false'
        # }
    }).encode('utf-8')
    main_request(api_url, requests_data)
    print("Date >> 启动成功\n")


# 启动
def cycle_main():
    # 2021年11月1日
    # By：M0x1n
    # Project Name: DingDing_IP_Push_robot
    # 项目名： 钉钉公网推送机器人
    IP_A = get_ip_a()
    Time_A = strftime("%Y-%m-%d %H:%M:%S", localtime())

    api_url = "https://oapi.dingtalk.com/robot/send?access_token="
    requests_data = json.dumps({
        "msgtype": "markdown",
        "markdown": {
            "title": "IP定时通知测试",
            "text": "#### IP定时通知： \n > 公网IP：" + IP_A + "\n > \n > 系统时间：" + Time_A + " \n > \n > ![screenshot](https://bbs.moxinwangluo.cn/logo1.png)\n > ###### M0x1n本地服务器 [机器人](https://pan.moxinwangluo.cn) \n"
        }
        # "at": {
        #   "atMobiles": [
        #      "150XXXXXXXX"
        # ],
        # "atUserIds": [
        #    "user123"
        # ],
        # "isAtAll": 'false'
        # }
    }).encode('utf-8')
    main_request(api_url, requests_data)
    print("Date >> 发送成功\n")


# 循环监控时间
def timer(n):
    iftime = strftime("%M", localtime())
    if iftime == "00" or iftime == "30":
        cycle_main()
    time.sleep(n)  # 循环单位为秒


tips()
cycle_time = 60
while 1 == 1:
    print("Date >> 循环秒数", str(cycle_time), "\n")
    timer(cycle_time)  # 60秒循环（可以防止一分钟发两次）

