# NTUPA internal management system
## Configure
Write ```ntupa/secrets.py``` as the following example:

```python
import os

SECRET_KEY = '123hello123'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#set below to relative path of STATIC folder
STATIC_ROOT = 'static/'
```
