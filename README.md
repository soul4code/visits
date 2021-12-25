Тестовое задание

Как запустить:

`cp .env.sample .env`

`docker-compose up`

После этого бэкенд будет доступен по адресу:

http://127.0.0.1:8000/


Админка http://127.0.0.1:8000/admin/ (логин и пароль в.env файле)


API


http://127.0.0.1:8000/api/

Авторизацией служит http заголовок Phone <Номер телефона>, где номер телефона - это phone у определенного Employee

http://127.0.0.1:8000/api/stores/ - Торговые точки.
Пример запроса: 
```
curl -i -X GET \
   -H "Authorization:Phone +79998887766" \
 'http://127.0.0.1:8000/api/stores/'
```


http://127.0.0.1:8000/api/visit/ - Визит.
Пример запроса: 
```
curl -i -X POST \
   -H "Content-Type:application/json" \
   -H "Authorization:Phone +79998887766" \
   -d \
'{"store": 2, "coordinates": [13, 13]}' \
 'http://127.0.0.1:8000/api/visit/'
 ```

Покрытие тестами 93%

Запуск тестов - pytest



