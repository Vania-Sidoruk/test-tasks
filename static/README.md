# 🐳 Flask + Redis Docker Compose 

Приложение будет доступно по адресу: http://localhost:5000

---

## 📦 Функциональность

- `/ping` — возвращает статус `{"status": "ok"}`
- `/count` — увеличивает и показывает счётчик посещений с использованием Redis
- `/image` — возвращает изображение из папки `static/`
- `/` — главная страница с удобными ссылками на все маршруты

---

## 📁 Структура проекта
. ├── app.py # Flask-приложение ├── Dockerfile # Docker образ для Flask ├── docker-compose.yaml # Сборка Flask + Redis ├── requirements.txt # Python зависимости └── static/ └── UhXC1nzm3h.jpg # Картинка для /image
