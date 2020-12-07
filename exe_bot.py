import os
import zipfile
import time
import random
from selenium import webdriver


#bug_1=False
cont=0
t=1
c_bug=0

# is necesary send "self" of the class as argument (and here is receiv as the argument 'objeto') for can use self variables outside of the class, too "js_script_2" as js2
def bug_municip(objeto, js2): 
	try:
		objeto.driver.find_elements_by_xpath('//input[@id="municipality"]')[0]
		objeto.driver.execute_script(js2)
		time.sleep(t)
		print('^time ^^^^^^^^^^^^^^^^^^^^',t)
		objeto.driver.find_elements_by_xpath('//button[@class="sui-AtomButton sui-AtomButton--primaryColor sui-AtomButton--solid "]')[0].click()
		
		int('[cont] esta en el valor de:--->',cont)
	except Exception as e:
		print('bug- Exception:--------:', e)
		pass


"""
def bug_municip():
	try:
		print('.... intentando resolver bug de municipio ++')
		if bug_1== False:
			print('BUG-AAAAAAA IF VARIABLE')
			#validar si input de municipio esta vacio
			municip=self.driver.find_elements_by_xpath('//input[@id="municipality"]')[0]
			print('BUG-XXXXXXX IF VARIABLE')
			val_mun = municip.get_attribute("value")

			if val_mun == '' or val_mun == None:
				#elegir municipipo
				self.driver.execute_script(js_script_2)
				#sigueinte
				self.driver.find_elements_by_xpath('//button[@class="sui-AtomButton sui-AtomButton--primaryColor sui-AtomButton--solid "]')[0].click()
				print('BUG before------------------°|° ', bug_1)
				bug_1=True
				print('BUG after------------------°|° ', bug_1)
	except Exception as e:
		print('bug- Exception::', e)
		pass
"""
		




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
		print('before -log')
		time.sleep(25)	
		#l=self.driver.find_elements_by_xpath('//a[@class="ma-NavigationTopNav-accountInfo-logoutLn"]')[0].text#<<
		cn=0
		while 1:
			if cn ==10000: # if after 10000 tries it no achieved get loguin, send "False" and restart the proces
				
				return False
			try:
				l=self.driver.find_elements_by_css_selector('a[class="ma-NavigationTopNav-accountInfo-logoutLn"]')[0].text #<<
				print('l:',l, len(l))
			except: pass

			if l=='Cerrar sesión': # if found a text that say 'cerrar sesion', it means that already is logued
				print('OK LOGUIN')
				cn=0 # just for if anything :v
				return True # Before to start automate in routine file, first ensure that the login was succesfull
			cn+=1
			print('try login No:',cn)

		#	print('foloww')#<< 
		#self.driver.execute_script('document.querySelector(\'p[class="m"]\');')
		#print('l:',l, len(l))
		#print('after -log--')	
		#time.sleep(999999)



	def automate(self,ti,de,na,tel,em, tel2=False, url=None):

		print('*Set requested vars::')

		#Global variables to manage bugs

		global c_bug
		global cont
		global t


		# Variables of JavaScript to choose randon option in ubication deployed menus

		ra = random.randint(0,51)

		js_script = '''

				var ul_base = document.querySelector('ul[class="sui-MoleculeDropdownList sui-MoleculeDropdownList--large is-hidden"][tabindex="0"]');
				var li_list = ul_base.querySelectorAll("li");
				li_list[%d].click();
										''' % (ra)

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

		def solve_bug():
			print('.....start process ongoing') 

			self.driver.get(url)

			print('... [Get-URL IN AUTOMATE] ...')
			
				#Datos de tu anuncio
			while 1:
				try:
					title_b=self.driver.find_elements_by_xpath('//input[@id="title" and @name="title"]')[0]
					title_b.send_keys(ti)
					print('... SUCCES PLACED TITLE...')
					c_bug=0
					break
				except:
					c_bug+=1
					if c_bug == 200:
						print('Try get url again >:v')
						self.driver.get(url)
						c_bug=0	
					pass 

			print('-[0]-')		
			descript_b=self.driver.find_elements_by_xpath('//textarea[@id="description" and @name="description"]')[0]
			descript_b.send_keys(de)

			price_b=self.driver.find_elements_by_xpath('//input[@id="price" and @name="price"]')[0]
			price_b.send_keys("8")


			print('-[1]-')		

				#Ubicacion del anuncio (menu desplegable de ciudades)
				

			self.driver.execute_script(js_script)

			#time.sleep(0.1)



		print('                               > Start Automate <')

		solve_bug()								

		print('-[2]-')										
		#time.sleep(9)
		while(True):
			try:
				print(' ------------                        TRY js_script_2')
				self.driver.execute_script(js_script_2)
				print('\n... js_script_2')
				c_bug=0
				break
			except Exception as e:
				print('-[2]- exept: ', e)
				c_bug+=1
				if c_bug==200:
					print('                        =======> Badly is necesary use solve_bug for restart automate >.>')
					solve_bug() # As despair mean in case to stalemate for eternal error "Cannot click in undefined element"
					c_bug=0					
				pass	
		
		print('-[3]-')			
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


		print('-[4]-')			
			# mail

		mail_b=self.driver.find_elements_by_xpath('//input[@id="email" and @name="email"]')[0]
		try: val_m = mail_b.get_attribute("value") # intentar obtener valor del "value" atributo
		except: pass

		print('val_b->_',val_m)
		if val_m != '' and val_m != None:
			print('[[ pass val_m] ]') 
			pass
		elif val_m == '' or val_m == None:
			print('[[ send keys val_m] ]')
			mail_b.send_keys(em)


		print('-[5]-')	

			#Telefonos

		#Tel 1	
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

		print('-[6]-')	
			
		#Tel 2
		if tel2!=False:
			print('°°°°tel2°°°°')
			tel2_b=self.driver.find_elements_by_xpath('//input[@id="secondaryPhone" and @name="secondaryPhone"]')[0]

			try: val_p2 = tel2_b.get_attribute("value") # intentar obtener valor del "value" atributo
			except: pass

			if val_p2 == tel2: # nombre ya registrado(valor obtenido) es igual => ignorar
				print('IF of tel2')#<<
				pass
			elif val_p2 != '' and val_p2 != None: # si atributo obtenido no es nulo pero tampoco es igual => limpiar lo que encuentre y enviar el nuevo valor 
				self.driver.execute_script('''  var clean = document.getElementById("mainPhone"); 
											    clean.value=""; ''')
				tel2_b.send_keys(tel2)
				print('ELIF of tel2')#<<

			else:  # de cualquier otro caso solo enviar el valor a escribir
				tel2_b.send_keys(tel2)
				print('ELSE of tel2')#<<
				print('val_2 =', val_p2)			



		print('-[7]-')		

		
		print('await for click terms...[[')#<<
		#time.sleep(9)
			#Terminos --NOTA: CAMBIAR EN BASE A VALUE Y NO A login !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		term=self.driver.find_elements_by_css_selector('#terms')[0] # find by "ID" but is "#"  if were by class would be with "." instead
		val_term = term.get_attribute("value") # intentar obtener valor del "value" atributo
		print('value of term---:',val_term)

		if val_term=='true':
			print('term TRUE')
			pass
		else:
			print('term FALSE')
			self.driver.find_elements_by_css_selector('.sui-AtomCheckbox')[0].click() # when is "false" only can found and click the element the element external instead of input element 
	

		print('-[8]-')


			#siguiente

		print('---o---')
		sig=self.driver.find_elements_by_xpath('//button[@class="sui-AtomButton sui-AtomButton--primaryColor sui-AtomButton--solid "]')[0]	
		sig.click()	
		print('---x---\n')



		#up img 
		while 1:
			try: # hasta que encuente la imagen en la siguiente pagina

				pic=self.driver.find_elements_by_xpath('//input[@accept="image/jpeg, image/png, image/gif"]')[0]
				pic.send_keys(r'D:\git_up\job_milanuncios\jura.jpg')
				cont=0
				t=1
				break
			except Exception as e:

				print(cont,'°°°°°°°°°°°°°°°°°°°°°°',e)
				# Bugs potenciales
				if cont==70:
					cont=0
					bug_municip(self, js_script_2)
					if t < 8:
						t+=1
					else: 
						t=1
				cont+=1
				pass

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

	def close_bot(self):
		self.driver.close()


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