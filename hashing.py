from customtkinter import*
import hashlib

# Словарь хэш-функций
hash_functions = {
    'sha512': hashlib.sha512,
    'sha384': hashlib.sha384,
    'sha256': hashlib.sha256,
    'sha224': hashlib.sha224,
    'sha1': hashlib.sha1,
    'md5': hashlib.md5,
}

def hash(field,resfield,hchoose):
    text = field.get()
    if not text:
        resfield.delete(0, END)
        resfield.insert(0, 'Please enter some text.')
        return

    hash_function = hchoose.get()
    try:
        hashed_object = hash_functions[hash_function](text.encode())
        resfield.delete(0, END)
        resfield.insert(0, hashed_object.hexdigest())
    except KeyError:
        resfield.delete(0, END)
        resfield.insert(0, 'Unsupported hash function.')