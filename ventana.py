from tkinter import *

#Window base
root=Tk()

def button_run():
	print(descript_box.get('0.0', END))
	print(user_var.get())

root.title('Milanuncios APP')

#Login Vars
user_var=StringVar()
psw_var=StringVar()

#Proxy Vars
host_var=StringVar()
port_var=IntVar() # i don't know still if it is correct.
px_us_var=StringVar()
px_pw_var=StringVar()

#Form Vars
tit_var=StringVar()
name_var=StringVar()
phone_var=StringVar()
phone2_var=StringVar()
mail_var=StringVar()

#url vars
url_var=StringVar()
url_var.set('https://www.milanuncios.com/')
f_url_var=StringVar()


#Window Frames config
	#Frame Login
frame1 = Frame(root)
frame1.grid(row = 0, column = 0, padx= 20, pady= 5)

	#Frame Proxy
frame2 = Frame(root)
frame2.grid(row = 0, column = 1, padx= 20, pady= 5)

	#Frames Add Form
frame3 = Frame(root)
frame3.grid(row = 1, column = 0, padx= 20, pady= 20)

frame4 = Frame(root)
frame4.grid(row = 1, column = 1 , padx= 20, pady= 20)

frame5 = Frame(root)
frame5.grid(row = 2, columnspan=2 , padx= 20, pady= 20)

	#Frame Buttons
frame6 = Frame(root)
frame6.grid(row = 3, columnspan=2 , padx= 20, pady= 1)



#Login Form
title_log = Label(frame1, text ='LOGIN', font=(16))
title_log.grid(row = 0, column = 0, padx= 10, pady= 5)

user_text = Label(frame1, text ='User', font=(16))
user_text.grid(row = 1, column = 0, padx= 10, pady= 5)

user_box=Entry(frame1, textvariable=user_var)
user_box.grid(row = 1, column = 1, padx= 10, pady= 5)

psw_text = Label(frame1, text ='Password', font=(16))
psw_text.grid(row = 2, column = 0, padx= 10, pady= 5)

psw_box=Entry(frame1, textvariable=psw_var)
psw_box.grid(row = 2, column = 1, padx= 10, pady= 5)


#Proxy Form
title_prox = Label(frame2, text ='SET PROXY', font=(16))
title_prox.grid(row = 0, column = 0, padx= 10, pady= 5)

host_text = Label(frame2, text ='Host', font=(16))
host_text.grid(row = 1, column = 0, padx= 10, pady= 5)

host_box=Entry(frame2, textvariable=host_var)
host_box.grid(row = 1, column = 1, padx= 10, pady= 5)

port_text = Label(frame2, text ='Port', font=(16))
port_text.grid(row = 2, column = 0, padx= 10, pady= 5)

port_box=Entry(frame2, textvariable=port_var)
port_box.grid(row = 2, column = 1, padx= 10, pady= 5)

px_user_text = Label(frame2, text ='Proxy User', font=(16))
px_user_text.grid(row = 1, column = 2, padx= 10, pady= 5)

px_user_box=Entry(frame2, textvariable=px_us_var)
px_user_box.grid(row = 1, column = 3 , padx= 10, pady= 5)

px_psw_text = Label(frame2, text ='Proxy Password', font=(16))
px_psw_text.grid(row = 2, column = 2, padx= 10, pady= 5)

px_user_box=Entry(frame2, textvariable=px_pw_var)
px_user_box.grid(row = 2, column = 3, padx= 10, pady= 5)


#Form add data
title_add = Label(frame3, text= 'FORM Add', font=(16))
title_add.grid(row= 0, column= 0, padx=10, pady=5)

tit_add_text = Label(frame3 , text ='Title', font=(16))
tit_add_text.grid(row = 1, column = 0, padx= 10, pady= 5)

tit_box=Entry(frame3, textvariable=tit_var)
tit_box.grid(row = 1, column = 1, padx= 10, pady= 5)

name_text = Label(frame3 , text ='Name', font=(16))
name_text.grid(row = 2, column = 0, padx= 10, pady= 5)

name_box=Entry(frame3, textvariable=name_var)
name_box.grid(row = 2, column = 1, padx= 10, pady= 5)

phone_text = Label(frame3 , text ='Phone', font=(16))
phone_text.grid(row = 3, column = 0, padx= 10, pady= 5)

phone_box=Entry(frame3, textvariable=phone_var)
phone_box.grid(row = 3, column = 1, padx= 10, pady= 5)

phone2_text = Label(frame3 , text ='Phone 2', font=(16))
phone2_text.grid(row = 4, column = 0, padx= 10, pady= 5)

phone2_box=Entry(frame3, textvariable=phone2_var)
phone2_box.grid(row = 4, column = 1, padx= 10, pady= 5)

mail_text = Label(frame3 , text ='e-mail', font=(16))
mail_text.grid(row = 5, column = 0, padx= 10, pady= 5)

mail_box=Entry(frame3, textvariable=mail_var)
mail_box.grid(row = 5, column = 1, padx= 10, pady= 5)

mail_text = Label(frame3 , text ='e-mail', font=(16))
mail_text.grid(row = 5, column = 0, padx= 10, pady= 5)


mail_text = Label(frame4 , text ='Description', font=(16))
mail_text.grid(row = 0, column = 0, padx= 10, pady= 3)

descript_box= Text(frame4, height=7, width=70)
descript_box.grid(row=1, column=0, padx=10, pady=5)

url_text = Label(frame5 , text ='URL', font=(16))
url_text.grid(row = 0, column = 0, padx= 10, pady= 5)

url_box=Entry(frame5, textvariable=url_var, width=40)
url_box.grid(row = 0, column = 1, padx= 10, pady= 5)

url_text = Label(frame5 , text ='Form URL', font=(16))
url_text.grid(row = 0, column = 2, padx= 10, pady= 5)

url_box=Entry(frame5, textvariable=f_url_var, width=40)
url_box.grid(row = 0, column = 3, padx= 10, pady= 5)


run_button= Button(frame6, text='Run', command=button_run)
run_button.grid(row= 0, column= 0, padx=10, pady=5)








root.mainloop()