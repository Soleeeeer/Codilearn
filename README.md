# Codilearn — Educational Platform API

Серверное API-приложение для онлайн-обучения, написанное на Django REST Framework с поддержкой WebSocket-уведомлений.


---

## 💡 Основные функции

- Управление курсами, уроками и домашними заданиями
- Роли пользователей: студент / преподаватель
- Загрузка и просмотр учебных файлов
- Уведомления в реальном времени через WebSocket
- JWT-аутентификация

---

## 🚀 Быстрый старт

1. Клонируй проект:
   ```bash
   git clone https://github.com/yourusername/codilearn.git
   cd codilearn


### 2. Создаём виртуальное окружение и запускаем его


```bash
python -m venv venv
```
Windows
```bash
venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запускаем Redis/PostgreSQL через Docker:
#### (ВАЖНАЯ РЕМАРКА. сначало надо создать env. файлик в корне проекута и заполнить его. После этого мы запускаем docker и прописываем это.)

```bash
docker run -d -e POSTGRES_PASSWORD=<введи сюда пароль из .env> -p 5432:5432 postgres

docker run -d -p 6379:6379 redis
```

### 5. Применение миграций и запускаем сервер

```bash
python manage.py makemigrations
python manage.py migrate
```
```bash
python manage.py runserver
```

## После того как сервер запустится, переходим по этой ссылки для регистрации нового пользователя

[http://127.0.0.1:8000/auth/users/me](http://127.0.0.1:8000/auth/users/me)
