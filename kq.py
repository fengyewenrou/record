import requests
import os
from PIL import Image
import pytesseract
import datetime as datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from wxpy import *
import time


scheduler = BlockingScheduler(daemonic = False)


def sendMail(msg,msg_to):
    msg_from = '240258108@qq.com'  # 发送方邮箱
    passwd = 'urtnrloxhsslbjej'  # 填入发送方邮箱的授权码
    msg_to = msg_to  # 收件人邮箱

    subject = "大人！忘记打卡啦"  # 主题
    msg = MIMEText(msg)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    s.quit()
def imageCode(today):
    imageCode = Image.open(os.getcwd() + "/code" + today + ".png")
    vcode = pytesseract.image_to_string(imageCode)
    print(vcode)
    return vcode
def login(data):
    today = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    url = "http://kq2.qk365.com/login"
    result = requests.get(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Referer': 'http://kq2.qk365.com/login'
    }
    imgUrl = "http://kq2.qk365.com/login/code"
    name = 'code' + today
    img = requests.get(imgUrl, cookies=result.cookies)
    f = open(name + '.png', 'ab')
    f.write(img.content)
    f.close()
    data['validateCode'] = imageCode(today);
    page = requests.post(url, data=data, headers=headers, cookies=result.cookies)
    return page
def getPage(page,msg_to,bot):
    user_number = BeautifulSoup(page.text, 'lxml').find('div', class_='page-header')
    user_info = user_number.text
    print(user_info)
    all_td = BeautifulSoup(page.text, 'lxml').find('table', class_='table').find_all('td')
    clock = []
    for td in all_td:
        tdContent = td.text
        clock.append(tdContent)
    start_date = datetime.datetime.strptime(clock[-1], "%Y-%m-%d %H:%M:%S")  # 考勤已有的打卡时间
    today2 = datetime.datetime.now().strftime("%Y-%m-%d")  # 格式化今天
    today2 += ' 18:00:00'  # 拼接晚上6点 如果打卡时间小于晚上6点则证明没有打卡
    end_date = datetime.datetime.strptime(today2, "%Y-%m-%d %H:%M:%S")  # 格式化时间

    friend = bot.friends().search('诗酒趁年华')[0]
    if (start_date < end_date):
        print("你没打卡！")
        friend.send(user_info+'大人，你好像忘记打卡了')
        sendMail(user_info + '大人，你好像忘记打卡了',msg_to);
    else:
        print("你打卡了！")
        friend.send(user_info+'大人，你打卡了')


@scheduler.scheduled_job("cron",minute=1)
def main():

     data = {}
     while True:
         data['username'] = 'fanfuchen'
         data['password'] = 'Qingke365'
         page = login(data);
         bot = Bot(cache_path=True,console_qr=2)
         user_number = BeautifulSoup(page.text, 'lxml').find('div', class_='page-header')
         if user_number is not None:
             getPage(page,'fanfuchen@qk365.com',bot)
             break
         else:
             time.sleep(2)
             pass


try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
