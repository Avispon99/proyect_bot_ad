from selenium import webdriver
import time

url= 'https://www.milanuncios.com/mis-anuncios'
chromeOpt=webdriver.ChromeOptions()
chromeOpt.add_argument('--disable-gpu')
dv=webdriver.Chrome(executable_path='D:\\chromedriver.exe',chrome_options=chromeOpt)
dv.get(url)

mail='testmaster1255aa@gmail.com'
psw='master1255aa'
dv.find_element_by_id('email').send_keys(mail)
dv.find_element_by_id('password').send_keys(psw)
dv.execute_script('''
var sub=document.querySelector('button[class="sui-AtomButton sui-AtomButton--primaryColor sui-AtomButton--solid sui-AtomButton--fullWidth ma-FormLogin-submitButton"][type="submit"]');	
sub.click()
'''	)



"""
#butt=dv.find_elements_by_xpath('//button')
#print(len(butt))
print('\nWait..2')
time.sleep(4)
dv.find_elements_by_xpath('//button')[2].click()
print('\nwait..3')
time.sleep(9)
dv.find_elements_by_xpath('//button')[3].click()

for i in range(len(dv.find_elements_by_xpath('//button'))):
	try:
		b=dv.find_elements_by_xpath('//button')[i].click()
		print(i)
	except:
		pass
	#time.sleep(15)

"""
