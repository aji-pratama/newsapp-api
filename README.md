# Simple News Apps Documentation

## 1. Setting Up Project

#### In this project we need to install reqirement for machine:
-	Postgresql/Mysql 
-	Python > 3
-	Django > 2

#### For requirement project 
- Django==2.0.3
- Pillow==5.0.0
- psycopg2==2.7.4
- Pygments==2.2.0
- pytz==2018.3

### 1. Install requirements.txt 
After clone this project, then cd to main project directory

` $ pip install requirements.txt `

### 2. Setting Environment Database
Open file `config/settings.py` and find Variable `DATABASE`

##### For Postgresql
```

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'YOUR_DATABASE_NAME',
        'USER': 'YOUR_DATABASE_USER',
        'PASSWORD': 'YOUR_DATABASE_PASSWORD'
    }
}

```
##### For Sqlite :

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
### 3. Migrate Database
`$ ./manage.py migrate`

### 4. Create Super User
`$ ./manage.py createsuperuser `

### 5. Running server
`$./manage.py runserver`

### 6. Create Tastypie API Key
Open your url admin development server by default is `127.0.0.1:8000/admin` Then find menu tastypie and create API Key & Username you want.

## 2. Testing API
If you use Postman or have postman in your machine you can import with this url `https://www.getpostman.com/collections/a2888c9d7724ed1403a6`

