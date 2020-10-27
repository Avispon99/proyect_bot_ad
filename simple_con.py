from selenium import webdriver

url= 'https://www.myip.com/'
chromeOpt=webdriver.ChromeOptions()
chromeOpt.add_argument('--disable-gpu')
dv=webdriver.Chrome(executable_path='D:\\c_driver\\chromedriver.exe',chrome_options=chromeOpt)
dv.get(url)

import time
time.sleep(20)