import hashlib
from customtkinter import *
from PIL import Image

app = CTk()
app.geometry('640x480')
app.resizable(False,False)
app.title('random hash program. (should you believe it?)')
set_appearance_mode('dark')
set_default_color_theme('green')

logo = CTkImage(light_image=Image.open('hash.png'),dark_image=Image.open('hash.png'),size=(320,170))

def hash():
    global hashed_object

    if hashchose.get() == 'sha512':
        hashed_object = hashlib.sha512(enter.get().encode())
    elif hashchose.get() == 'sha384':
        hashed_object = hashlib.sha384(enter.get().encode())
    elif hashchose.get() == 'sha256':
        hashed_object = hashlib.sha256(enter.get().encode())
    elif hashchose.get() == 'sha224':
        hashed_object = hashlib.sha224(enter.get().encode())
    elif hashchose.get() == 'sha1':
        hashed_object = hashlib.sha1(enter.get().encode())
    elif hashchose.get() == 'md5':
        hashed_object = hashlib.md5(enter.get().encode())



    result.delete(0,END)
    result.insert(0, hashed_object.hexdigest())

logoimg = CTkLabel(master=app,image=logo,text='')
logoimg.place(relx=.5,rely=.17,anchor='center')

result = CTkEntry(master=app, placeholder_text='Result', width=400)
result.place(relx=.5,rely=.75,anchor='center')

btn = CTkButton(master=app, text='Hash', command=hash)
btn.place(rely=.6,relx=.5,anchor='center')

enter = CTkEntry(master=app, placeholder_text='text that will be hashed...',width=400)
enter.place(rely=.5,relx=.5,anchor='center')

hashchose = CTkOptionMenu(master=app, values=['sha512','sha384','sha256','sha224','sha1','md5'])
hashchose.place(rely=.38,relx=.5,anchor='center')

app.mainloop()