import requests
from bs4 import BeautifulSoup
Headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__f_=1532489554186; _ntes_nnid=95de30d811e42b60f7d953bb51d3f382,1532489549780; _ntes_nuid=95de30d811e42b60f7d953bb51d3f382; nts_mail_user=zhaocimuge@163.com:-1:1; Province=021; City=021; NNSSPID=474aabea0304418e89283e9490d7df74; NTES_hp_textlink1=old; neteaseAD11889channelcookies11464794221533785394179155=2; s_n_f_l_n3=d7c5a631e5fa91961533879790798; vjuids=94411bfd6.165225c5948.0.f11d78e980486; vjlast=1533879802.1533879802.30; NTES_PASSPORT=oesHRurY2_Z5lTFJtOL70EbL8qlRIG4wRx6xHxR2IR8IceKDcQzbiWIE085yfnxj09CxxXUiNpT5loC0MBInRAbr4H75tKqEuyeCyIOqsCJysQi.HOBt0Xz9bhBLsleE_leDcuH4oMUJH.AhrR4hGuo80bL62O1eVzlPcR7dgRhlL; mail_psc_fingerprint=64d771817380e9a73db4fb0ea2c7fe97; n_ht_s=1; cm_newmsg=user%3Dzhaocimuge%40163.com%26new%3D0%26total%3D1; NTES_SESS=_Ux1SJuoOd4tiU2CKVD.o0rMmPWhMTSZo4G6EJnI4aA95EnP5.MfeYdUH20oTVQsH0QRhpQr6OFf1cSBtNK03xPUOBLNkxMYkSHEJMIhPN2ZE4iWDm6mj7sMTpDyeBzksb3rulGvodfnsIvsadiPjLz9GirFIY9Jl6Kl6eK8wfG7_XIMbjo6hBZS5onzRxkWt; S_INFO=1533880778|0|2&70##|zhaocimuge; P_INFO=zhaocimuge@163.com|1533880778|0|urs|00&99|shh&1533880447&163#shh&null#10#0#0|&0|163|zhaocimuge@163.com; __utma=187553192.979881931.1533880775.1533880775.1533880775.1; __utmc=187553192; __utmz=187553192.1533880775.1.1.utmcsr=reg.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/Main.do; __utmb=187553192.2.10.1533880775; ne_analysis_trace_id=1533880847268; neteaseAD118810channelcookies11464794221533785394179155=9; vinfo_n_f_l_n3=d7c5a631e5fa9196.1.1.1533800700598.1533801089630.1533880849788',
    'Host': 'news.163.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
result = requests.get("https://www.163.com/")
news = BeautifulSoup(result.text, 'lxml').find('div', class_='mod_top_news')
all_li = BeautifulSoup(news, 'lxml').find_all('li')
print(all_li)