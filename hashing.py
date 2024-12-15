import hashlib
from tkinter import END

# Словарь хэш-функций
hash_functions = {
    'sha512': hashlib.sha512,
    'sha384': hashlib.sha384,
    'sha256': hashlib.sha256,
    'sha224': hashlib.sha224,
    'sha1': hashlib.sha1,
    'md5': hashlib.md5,
}

def hash(input_field, result_field, hash_choice):
    text = input_field.get()
    if not text:
        result_field.delete(0, END)
        result_field.insert(0, 'Please enter some text.')
        return

    hash_function = hash_choice.get()
    try:
        hashed_object = hash_functions[hash_function](text.encode())
        result_field.delete(0, END)
        result_field.insert(0, hashed_object.hexdigest())
    except KeyError:
        result_field.delete(0, END)
        result_field.insert(0, 'Unsupported hash function.')
