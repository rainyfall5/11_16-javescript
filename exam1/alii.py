from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r'--user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\User Data') # 设置用户文件夹，可免登陆
chrome_options.add_argument('--no-sandbox')
s = Service(r"D:\BaiduSyncdisk\py_proje\9_21_amazon\chromedriver.exe")

driver = webdriver.Chrome(service=s,options=chrome_options)
w = 'https://yc.alibaba.com/?spm=a213gs.26037848.0.0.42817a86EwxAjC#/report/picture?protectIds=11174506624&ownerIds=3255953547'
#w ='https://www.baidu.com'
driver.get(w)
time.sleep(10)
