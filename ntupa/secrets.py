import os

SECRET_KEY = 'Dq:OeE#3}a38zKo)1{-z6n9683f$j3)6Pfip(ovt6q?`JG9@AMOf$#.{Xh`GO1J'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}