# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-58x1uvcux#=)au9cn)&unzo&1^g$&dt4c4h$_h%pwgq6b4y(hm'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'heroes_and_villians_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}