Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask
... import base64
... app = Flask(name)
... def decode_flag(encoded_flag):
...     flag = base64.b64decode(encoded_flag.encode()).decode()
...     return flag
... 
... encoded_flag = "RmxhZ3tldDBfbGVnazB9"
... 
... 
... @app.route('/')
... def index():
...     decoded_flag = decode_flag(encoded_flag)
...   
...     return decoded_flag
... 
... if name == 'main':
