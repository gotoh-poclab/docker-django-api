# docker_django

# 初回

- 起動<br>
  `docker-compose up -d`
- migrtions<br>
  `docker-compose run web python manage.py makemigrations `

- migrate <br>
  `docker-compose run web python manage.py migrate `

- superuser の作成 <br>
  `docker-compose run web python manage.py createsuperuser`
- 終了<br>
  `docker-compose stop`

# 初回以降の毎回の操作方法

- 起動<br>
  `docker-compose start`
- ログをみながら行う場合<br>
  `docker-compose logs -f`

- 開発状況を確認<br>
  http://localhost:8000/

- 管理画面を確認<br>
  http://localhost:8000/admin

- 停止 <br>
  `docker-compose stop`

# 最初から作成する方法

1. startproject
   docker-compose run web django-admin.py startproject config .

2. setting の db を変更

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'postgres',
'USER': 'postgres',
'HOST': 'db',
'PORT': 5432,
}
}

3. startapp core <br>
   `docker-compose run web django-admin startapp core`

setting.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', #追加
]
```

4. startapp users<br>
   `docker-compose run web django-admin startapp users`

customuser 関係を作成

Django で Custom User Model を実装する<br>
https://qiita.com/keita_gawahara/items/e534178d9ae89872ebab

5. makemigrations
   docker-compose run web python manage.py makemigrations

6. migrate
   docker-compose run web python manage.py migrate
7. settings.py の書き換え
   本番運用を想定した Django settings.py の書き方入門<br>
   https://speakerdeck.com/ryu22e/ben-fan-yun-yong-woxiang-ding-sitadjango-settings-dot-pyfalseshu-kifang-ru-men <br>
   Django の settings を切り替えるようにした話<br>
   https://qiita.com/ukisoft/items/8912d0a66151609d9ff9

config/setting.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'users', #追加
]
...
AUTH_USER_MODEL = 'users.CustomUser' # 追加
```

users/models.py

```
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
```

8. startapp api<br>
   `docker-compose run web django-admin startapp api`

#その他のメモ(起動確認など)。

Cloud Run 環境での Django の実行を見て、勉強する。
https://cloud.google.com/python/django/run#macos-64-bit

# dockerfile だけで起動できるかを確認する。

test のところは任意

`docker build -t test .`

`docker run -p 8000:8000 test`

- 立ち上がっている docker の確認<br>
  `docker ps `
- 立ち上がっている docker を止める<br>
  `docker stop $Container ID `
