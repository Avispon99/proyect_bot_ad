import os
import zipfile
import time
import random
from selenium import webdriver



class DriverBot():

	#login=False
	login=False

	def __init__(self, path=None):
		self.path = path
		self.driver = None
		

	def run(self,host, port, user=None, pasw=None, 
		     use_proxy=False, user_agent=None, play=True):
		
		print('start run..')


		manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

		background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
          },
          bypassList: ["localhost"]
        }
      };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (host, port, user, pasw)

		def get_chromedriver():
		    #path = os.path.dirname(os.path.abspath(__file__))
		    chrome_options = webdriver.ChromeOptions()

		    if use_proxy:
		        pluginfile = 'proxy_auth_plugin.zip'
		        with zipfile.ZipFile(pluginfile, 'w') as zp:
		            zp.writestr("manifest.json", manifest_json)
		            zp.writestr("background.js", background_js)
		        chrome_options.add_extension(pluginfile)

		    if user_agent:
		        chrome_options.add_argument('--user-agent=%s' % user_agent)
		    
		    #driver = webdriver.Chrome(os.path.join(path, 'chromedriver'),chrome_options=chrome_options)
		    chrome_options.add_argument('--disable-gpu')
		    driver = webdriver.Chrome(executable_path=self.path ,chrome_options=chrome_options)
    
		    return driver

		def main():
		    self.driver = get_chromedriver()
		    #driver.get('https://www.google.com/search?q=my+ip+address')
		    #self.driver.get(self.url)
		    time.sleep(1)#<<

		if play:
			main()


	def log(self, log_user, log_psw, url=None):
		DriverBot.login=True # uso de la variable de clase login
		print('start log ..')
		self.driver.get(url)
		self.driver.find_element_by_id('email').send_keys(log_user)
		self.driver.find_element_by_id('password').send_keys(log_psw)

		try: # En caso de alerta de cookies 
			self.driver.execute_script('''
			var cookies = document.querySelector('button[class="sui-AtomButton sui-AtomButton--primary "]');
			cookies.click()
				''')
		except:
			pass

		self.driver.execute_script('''
		var sub=document.querySelector('button[class="sui-AtomButton sui-AtomButton--primaryColor sui-AtomButton--solid sui-AtomButton--fullWidth ma-FormLogin-submitButton"][type="submit"]');	
		sub.click()
		'''	)


		time.sleep(9)		


	def automate(self,ti,de,na,tel,em, url=None):
		print('start automate..')
		self.driver.get(url)

		

			#Datos de tu anuncio

		title_b=self.driver.find_elements_by_xpath('//input[@id="title" and @name="title"]')[0]
		title_b.send_keys(ti)

		descript_b=self.driver.find_elements_by_xpath('//textarea[@id="description" and @name="description"]')[0]
		descript_b.send_keys(de)

		price_b=self.driver.find_elements_by_xpath('//input[@id="price" and @name="price"]')[0]
		price_b.send_keys("8")


		

			#Ubicacion del anuncio (menu desplegable de ciudades)
			
		ra=random.randint(0,51)

		js_script = '''

				var ul_base = document.querySelector('ul[class="sui-MoleculeDropdownList sui-MoleculeDropdownList--large is-hidden"][tabindex="0"]');
				var li_list = ul_base.querySelectorAll("li");
				li_list[%d].click();
										''' % (ra)
		self.driver.execute_script(js_script)

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
		"""								
		time.sleep(9)
		while(True):
			try:
				self.driver.execute_script(js_script_2)
				print('\n... ok')
				break
			except:
				pass	
		"""

		#Datos de contacto

			#nombre	

		name_b=self.driver.find_elements_by_xpath('//input[@id="name" and @name="name"]')[0] #buscar elemento

		try: val_att = name_b.get_attribute("value") # intentar obtener valor del "value" atributo
		except: pass

		if val_att == na: # nombre ya registrado(valor obtenido) es igual => ignorar
			print('if na')#<<
			pass
		elif val_att != '' and val_att != None: # si atributo obtenido no es nulo pero tampoco es igual => limpiar lo que encuentre y enviar el nuevo valor 
			self.driver.execute_script('''  var clean = document.getElementById("name"); 
										    clean.value=""; ''')
			name_b.send_keys(na)
			print('elif na')#<<

		else:  # de cualquier otro caso solo enviar el valor a escribir
			name_b.send_keys(na)
			print('else na')#<<
			print('val_ =', val_att)


			# mail

		if DriverBot.login != True:
			mail_b=self.driver.find_elements_by_xpath('//input[@id="email" and @name="email"]')[0]
			mail_b.send_keys(em)


			#Telefonos

		tel_b=self.driver.find_elements_by_xpath('//input[@id="mainPhone" and @name="mainPhone"]')[0] # buscar elemento
		#tel_b.send_keys(tel)#<<

		try: val_p1 = tel_b.get_attribute("value") # intentar obtener valor del "value" atributo
		except: pass

		if val_p1 == tel: # nombre ya registrado(valor obtenido) es igual => ignorar
			print('if na')#<<
			pass
		elif val_p1 != '' and val_p1 != None: # si atributo obtenido no es nulo pero tampoco es igual => limpiar lo que encuentre y enviar el nuevo valor 
			self.driver.execute_script('''  var clean = document.getElementById("mainPhone"); 
										    clean.value=""; ''')
			tel_b.send_keys(tel)
			print('elif na')#<<

		else:  # de cualquier otro caso solo enviar el valor a escribir
			tel_b.send_keys(tel)
			print('else na')#<<
			print('val_ =', val_p1)



		#tel2_b=dv.find_elements_by_xpath('//input[@id="secondaryPhone" and @name="secondaryPhone"]')[0]
		#tel2_b.send_keys('65456')

		
			#Terminos --NOTA: CAMBIAR EN BASE A VALUE Y NO A login !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
		a=self.driver.find_elements_by_css_selector('.sui-AtomCheckbox')[0]
		a.click()
		if DriverBot.login == True:
			a.click() # for any reason require two clicks when using log 


		
		# Ejecutar seleccion de localidad al final para eludir la influencia de las cookies en la sincronizacion del menu desplegable
		while(True):
			try:
				self.driver.execute_script(js_script_2)
				print('\n... ok')
				break
			except:
				pass


			
			#siguiente

		print('---o---')
		sig=self.driver.find_elements_by_xpath('//button[@class="sui-AtomButton sui-AtomButton--primaryColor sui-AtomButton--solid "]')[0]	
		sig.click()	
		print('---x---\n')

		#time.sleep(5)#temporal

		#up img 
		while 1:
			try: # hasta que encuente la imagen en la siguiente pagina

				pic=self.driver.find_elements_by_xpath('//input[@accept="image/jpeg, image/png, image/gif"]')[0]
				pic.send_keys(r'D:\git_up\job_milanuncios\jura.jpg')
				break
			except: pass

		#interactuando con el panel de carga de img para que envie la img
		while 1:
			try:
				self.driver.execute_script('''var rot= document.querySelectorAll('div[class="sui-MoleculePhotoUploader-thumbCard-button"]')[1];
					rot.click();
					rot.click();
					rot.click();
					rot.click();	''')
				break
			except: pass


		#Publicar 
		
		while 1: #Nota: Controlar esto con busqueda 
			try:	
				self.driver.execute_script('''
				var pu= document.querySelector('button[class="ma-ButtonBasic ma-ButtonBasic--primary ma-ButtonBasic--medium"][type="button"]');
				pu.click()
											''')
				break	
			except: pass

		 



		"""	
		self.driver.execute_script('''
		var pu= document.querySelector('button[class="ma-ButtonBasic ma-ButtonBasic--primary ma-ButtonBasic--medium"][type="button"]');
		pu.click()
									''')		
		"""#<<

		
		

		print('FINAL...')

		"""
		while True:
			pass
		"""


if __name__ == '__main__':

	url= 'https://www.milanuncios.com/publicar-anuncios-gratis/formulario?c=323'
	#url = 'https://www.myip.com/'
	#path = 'D:\\c_driver\\chromedriver.exe'
	path = 'D:\\chromedriver.exe'
	PROXY_HOST = '193.26.152.81'  # rotating proxy
	PROXY_PORT = 58542
	PROXY_USER = 'gv4sL1Nwga'
	PROXY_PASS = 'c0bY1fQVNY'



	titulo ='elaboracion del tfg /tfm y tesis doctoral'
	
	#descripcion='aaaaaaaaaassssssssssssssssssddddddddddddddddddddffffffffffff'
	descripcion='''te ayudamos con los problemas academicos que tengas sobre el proyecto final de grado podemos asesorarte con clases particulares
para la elaboracion del guion final del tfg o tfm y tesis doctoral en todas las ramas y todas las universidades tales como:
Ade, Marketinng, Derecho, Economia, Planes de viabilidad o de empresa/negocio, analisis del TIR y BAN, analisis estadistico SPSS,
psicologia, educacion, administracion, ingieneria, informatica entre otros.SPSS, psicologia, educacion, administracion, ingieneria,
informatica entre otros. no dudes de contactar atraves de mesjaes privado correo o WhatsApp sin compromiso.'''
	nombre='javier martines'
	telefono= '692875247'
	email='jhonatan.trabajo99@gmail.com'

	print('\n  :D')
	ob=DriverBot(url, path)
	ob.run(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS, use_proxy=True)
	ob.automate(titulo, descripcion, nombre, telefono, email)