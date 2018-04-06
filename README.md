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
Open file `config/settings.py` and find Variable `DATABASES`

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
Open your url admin development server, by default is `127.0.0.1:8000/admin` Then find menu tastypie and create API Key & Username you want.

## 2. Testing API
If you use Postman or have postman in your machine you can import with this url `https://www.getpostman.com/collections/a2888c9d7724ed1403a6`


## 3. API Documentation
### News API 
There any 3 status of items draft, published, and deleted. each of them declare by number in this apps which :

- 1 : draft
- 2 : published
- 3 : deleted 

**API Docs :**

*Important* : After url API we must add username & API Key. e.g `www.example.com/api/news/?username=MyUsername&api_key=MyAPIKey 	`   

#### # News
| Method        | Url           | Description  |
| ------------- |-------------| -----|
| GET		| /api/news/ 					| List News |
| GET		| /api/news/?&status=1	|   Filter By Status (draft, published) |
| GET		| /api/news-deleted/     	|    List Deleted News |
| GET		| /api/news/?&topic=topic_name | Filter By Topic  |
| DELETE 	| /api/news/{id}/ | Delete News by id  |
| POST 	| /api/news/ | Create News Post |

```
// Json post NEWS
{
	"title":  "This is Title news",
	"content":  "This is Content News",
	"status":  "2",				// status draft / published
	"topic": ["2", "1"] 		// 2 & 1 is topic_id
}
```

#### # Topic
| Method        | Url           | Description  |
| ------------- |-------------| -----|
| GET | /api/topic/ |  List Topic  |
| GET | /api/topic/?&status=1 |   Filter By Status (draft, published) |
| GET | /api/topic-deleted/ |   List Deleted News / Filter delete  |
| DELETE  | /api/topic/{id}/ | Delete News by id |
| POST    | /api/topic/ | Create News Post  |

```
// Json post NEWS
{
	"name":  "Topic Name",
	"status":  "1" // status draft / published
}
```