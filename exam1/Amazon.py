from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(r'--user-data-dir=C:\Users\DELL\AppData\Local\Google\Chrome\User Data') # 设置用户文件夹，可免登陆
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)    # Chrome浏览器
w = 'https://www.baidu.com/'
driver.get(w)
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(30)