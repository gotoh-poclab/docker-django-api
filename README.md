# docker_django

# 使用技術
- [Django](https://docs.djangoproject.com/)
  - Django（ジャンゴ）は、Pythonで実装されたWebアプリケーションフレームワーク。
- [Django REST framework](https://www.django-rest-framework.org/)
  - PythonのWebアプリケーションフレームワークであるDjangoを使ってAPIを開発するために利用されるライブラリ
- [Docker](https://www.docker.com/)
  - コンテナ仮想化を用いてアプリケーションを開発・配置・実行するためのオープンソースソフトウェアあるいはオープンプラットフォーム。開発環境の構築のためdocker-composeを利用しています。
- [PostgreSQL](https://www.postgresql.org/)
  - 拡張性とSQL準拠を強調するフリーでオープンソースの関係データベース管理システム
- [Google Cloud Platform（GCP）](https://cloud.google.com/)
  - Google がクラウド上で提供するサービス群の総称。ここにデプロイすることを前提に作成
  
使用技術を組み合わせて、開発する上での基本的な技術検証を行っていきたい。

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

## static ファイル生成

setting.py の修正後にコマンド実行
ただし、Dockerfile 内で、毎回起動時に実行できるようにする方がよいかも。
`docker-compose run web python manage.py collectstatic`

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

- テストの実行 <br>
  `docker-compose run web python manage.py test`

- 初期データの追加<br>
  `docker-compose run web python manage.py loaddata fixtures/initial_data.yaml`


# DBの確認や操作


データベース接続
```
docker-compose exec db psql -h 127.0.0.1 -p 5432 -U postgres -d postgres
```

接続完了したら表示される内容
```
psql (13.4 (Debian 13.4-1.pgdg100+1))
Type "help" for help.

postgres=# 
```


テーブル一覧
```
postgres=# \dt;
```

テーブル構造
```
# 汎用的な記載方法
\d [テーブル名];
```
```
\d core_todomodel;
```

データ登録
```
INSERT INTO core_todomodel (id, text, "registrationTimeAt") VALUES (1, 'test', '2020-9-12 9:00:00');
commit;
```

データ検索
```
select * from core_todomodel;
```
→一件表示される

指定したテーブルのデータ初期化
```
TRUNCATE TABLE core_todomodel;
```

データ検索
```
select * from core_todomodel;
```
→データが０件なので、「0 rows」と表示される

# dockerfile だけで起動できるかを確認する。

test のところは任意

`docker build -t test .`

`docker run -p 8000:8000 test`

- 立ち上がっている docker の確認<br>
  `docker ps `
- 立ち上がっている docker を止める<br>
  `docker stop $Container ID `

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

9. fixturesで初期データの導入<br>
yaml形式の方が見やすいので、pythonでyamlが読めるように、以下をインストールする必要がある。<br>
`pip install pyyaml` <br>
requirements.txtに pyyamlを加える。<br>
書き方などは以下を参照
https://djangobrothers.com/blogs/fixture/


10. django-environで環境変数を管理してみる

https://e-tec-memo.herokuapp.com/article/172/
