from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

voc = '您你好吗我很呢马马虎虎再见忙累饿渴不李莉约翰请问叫什么名字姓贵是老师工程师她们你们秘书学生介绍一下他的朋友王刚邓小明认识高兴我们也先生这名片谢谢英国和法国那西班牙意大利中国在这儿德国那儿美国日本哪儿奥地利瑞士谁同学哪国人德国人会说汉语一点儿日语从来伦敦哪里北京大学学习柏林上海大众公司工作零一二三四五六七八九十现在几点钟半对不起请再遍中午分钟不客气有事情今天下午刻种咖啡馆等跟约会着急还时间明天号星期年月日知道要看日历晚上一起去电影想漂亮女人但是上午没有没关系吧人民币千百欧元元块角毛分空房间要单双还是间住两天多少钱个这么能便宜可以以上行填表格卡楼付钱了一共用宾馆刷卡换附近银行对面自动取款机取'

driver = webdriver.Chrome()
for x in voc:
    print(x)
    driver.get(f'http://www.strokeorder.info/mandarin.php?q={x}')
    time.sleep(1)
    img = driver.find_element(By.XPATH, "/html/body/div[1]/img")
    src = img.get_attribute('src')
    #print(src)

    r = requests.get(src)
    if r.ok:
        time.sleep(5)
        with open(f'images/{x}.gif', 'wb') as outfile:
            outfile.write(r.content)
    else:
        print(r)
driver.close()

