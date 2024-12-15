from customtkinter import *
from PIL import Image
from hashing import hash, hash_functions

def create_ui(app):
    # Логотип
    logo = CTkImage(light_image=Image.open('hash.png'), dark_image=Image.open('hash.png'), size=(320, 170))
    logoimg = CTkLabel(master=app, image=logo, text='')
    logoimg.place(relx=.5, rely=.17, anchor='center')

    # Поле для ввода текста
    enter = CTkEntry(master=app, placeholder_text='Text that will be hashed...', width=400)
    enter.place(rely=.5, relx=.5, anchor='center')

    # Выпадающий список выбора хэш-функции
    hashchose = CTkOptionMenu(master=app, values=list(hash_functions.keys()))
    hashchose.place(rely=.38, relx=.5, anchor='center')

    # Поле для отображения результата
    result = CTkEntry(master=app, placeholder_text='Result', width=400)
    result.place(relx=.5, rely=.75, anchor='center')

    # Кнопка для хэширования
    btn = CTkButton(master=app, text='Hash', command=lambda: hash(enter, result, hashchose))
    btn.place(rely=.6, relx=.5, anchor='center')

def main():
    # Настройки приложения
    app = CTk()
    app.geometry('640x480')
    app.resizable(False, False)
    app.title('Random Hash Program')
    set_appearance_mode('dark')
    set_default_color_theme('green')

    # Инициализация интерфейса
    create_ui(app)

    # Запуск приложения
    app.mainloop()

