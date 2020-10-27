from selenium import webdriver
import random
import time
#import requests

titulo ='elaboracion del tfg /tfm y tesis doctoral'
descripcion='''
te ayudamos con los problemas academicos que tengas sobre el proyecto final de grado podemos asesorarte con clases particulares
para la elaboracion del guion final del tfg o tfm y tesis doctoral en todas las ramas y todas las universidades tales como:
Ade, Marketinng, Derecho, Economia, Planes de viabilidad o de empresa/negocio, analisis del TIR y BAN, analisis estadistico SPSS,
psicologia, educacion, administracion, ingieneria, informatica entre otros.SPSS, psicologia, educacion, administracion, ingieneria,
informatica entre otros. no dudes de contactar atraves de mesjaes privado correo o WhatsApp sin compromiso.
'''
nombre='javier martines'
telefono= '692875247'
email='jhonatan.trabajo99@gmail.com'




url= 'https://www.milanuncios.com/publicar-anuncios-gratis/formulario?c=322'
chromeOpt=webdriver.ChromeOptions()
chromeOpt.add_argument('--disable-gpu')
dv=webdriver.Chrome(executable_path='D:\\chromedriver.exe',chrome_options=chromeOpt)
dv.get(url)



print('''
	1-Formacion y libros

	''')



	#Datos de tu anuncio

title_b=dv.find_elements_by_xpath('//input[@id="title" and @name="title"]')[0]
title_b.send_keys(titulo)

descript_b=dv.find_elements_by_xpath('//textarea[@id="description" and @name="description"]')[0]
descript_b.send_keys(descripcion)

price_b=dv.find_elements_by_xpath('//input[@id="price" and @name="price"]')[0]
price_b.send_keys("8")


	#Ubicacion del anuncio
	
ra=random.randint(0,51)

js_script = '''

		var ul_base = document.querySelector('ul[class="sui-MoleculeDropdownList sui-MoleculeDropdownList--large is-hidden"][tabindex="0"]');
		var li_list = ul_base.querySelectorAll("li");
		li_list[%d].click();

		//var fu = function getRanint(min, max){
 		//return Math.floor(Math.random() * (max-min)) + min; 
 		//}

 		//list_ul = document.getElementsByTagName('ul');
 		//ul_found = list_ul[2];
 		//li_loc = ul_found.querySelectorAll('li');
 		//const len = li_loc.length
 		//random_loc = fu(0, li_loc.length + 1);
 		//li_loc[random_loc].click();

								''' % (ra)
dv.execute_script(js_script)

#time.sleep(0.1)

js_script_2='''

		var fu = function getRanint(min, max){
 		return Math.floor(Math.random() * (max-min)) + min; 
 		}

 		list_ul = document.getElementsByTagName('ul');
 		ul_found = list_ul[2];
 		li_loc = ul_found.querySelectorAll('li');
 		const len = li_loc.length
 		random_loc = fu(0, len + 1);
 		li_loc[random_loc].click();	

								'''
while(True):
	try:
		dv.execute_script(js_script_2)
		print('\n... ok')
		break
	except:
		pass	




#lis_lu=dv.find_elements_by_xpath('/descendant::ul[@class="sui-MoleculeDropdownList sui-MoleculeDropdownList--large is-hidden"][2]')[0]
#lis_lu=dv.find_elements_by_css_selector('.sui-MoleculeDropdownList sui-MoleculeDropdownList--large is-hidden')
#lis_lu=dv.find_elements_by_xpath('//ul[@class="sui-MoleculeDropdownList sui-MoleculeDropdownList--large is-hidden" and @tabindex="0"]')[0]	
#lis_lu=dv.find_elements_by_xpath('//ul')[1]
#lis_lu=dv.find_elements_by_xpath('//ul[@class="sui-MoleculeDropdownList sui-MoleculeDropdownList--large is-hidden"]')[0]
#print('print lu:',lis_lu,'\n')
#print('type lu:',type(lis_lu),'\n')
##print(len(lis_lu),'\n')


#lis_li=dv.find_elements_by_xpath('//span[@class="sui-MoleculeDropdownOption-text sui-MoleculeDropdownOption-text--noWrap"]')[0].click()

#print('\n','Print li:',lis_li)
#print('\n','Type li:',type(lis_li))
#print(len(lis_li))


#lis_li[0].click()


	#Datos de contacto

name_b=dv.find_elements_by_xpath('//input[@id="name" and @name="name"]')[0]
name_b.send_keys(nombre)

mail_b=dv.find_elements_by_xpath('//input[@id="email" and @name="email"]')[0]
mail_b.send_keys(email)

tel_b=dv.find_elements_by_xpath('//input[@id="mainPhone" and @name="mainPhone"]')[0]
tel_b.send_keys(telefono)

#tel2_b=dv.find_elements_by_xpath('//input[@id="secondaryPhone" and @name="secondaryPhone"]')[0]
#tel2_b.send_keys('65456')




	#Terminos

a=dv.find_elements_by_css_selector('.sui-AtomCheckbox')[0]
a.click()



		#siguiente

#dv.execute_script('document.getElementsByTagName("button")[5].click()')
print('---o---')
sig=dv.find_elements_by_xpath('//button[@class="sui-AtomButton sui-AtomButton--primaryColor sui-AtomButton--solid "]')[0]	
sig.click()	
print('---x---\n')

time.sleep(5)

pic=dv.find_elements_by_xpath('//input[@accept="image/jpeg, image/png, image/gif"]')[0]
pic.send_keys(r'D:\git_up\job_milanuncios\jura.jpg')


	