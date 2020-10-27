import exe_bot



url= 'https://www.milanuncios.com/publicar-anuncios-gratis/formulario?c=323'
#url = 'https://www.myip.com/'
#path = 'D:\\c_driver\\chromedriver.exe'
path = 'D:\\chromedriver.exe'
PROXY_HOST = '193.26.152.81'  # rotating proxy
PROXY_PORT = 58542
PROXY_USER = 'gv4sL1Nwga'
PROXY_PASS = 'c0bY1fQVNY'



titulo ='elaboracion del tfg /tfm y tesis doctoral'
descripcion='''te ayudamos con los problemas academicos que tengas sobre el proyecto final de grado podemos asesorarte con clases particulares
para la elaboracion del guion final del tfg o tfm y tesis doctoral en todas las ramas y todas las universidades tales como:
Ade, Marketinng, Derecho, Economia, Planes de viabilidad o de empresa/negocio, analisis del TIR y BAN, analisis estadistico SPSS,
psicologia, educacion, administracion, ingieneria, informatica entre otros.SPSS, psicologia, educacion, administracion, ingieneria,
informatica entre otros. no dudes de contactar atraves de mesjaes privado correo o WhatsApp sin compromiso.
'''
nombre='javier martines'
telefono= '692875247'
email='jhonatan.trabajo99@gmail.com'

print('\n  rutine >:v')


bot = exe_bot.DriverBot(url, path)
bot.run(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS, use_proxy=True)
bot.automate(titulo, descripcion, nombre, telefono, email)


