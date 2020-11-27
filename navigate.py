from selenium import webdriver
import time

url= 'https://www.milanuncios.com'
url2= 'https://www.milanuncios.com/publicar-anuncios-gratis/formulario?c=322'
chromeOpt=webdriver.ChromeOptions()
chromeOpt.add_argument('--disable-gpu')
dv=webdriver.Chrome(executable_path='D:\\chromedriver.exe',chrome_options=chromeOpt)
dv.get(url)
time.sleep(7)
dv.get(url2)

time.sleep(14)

