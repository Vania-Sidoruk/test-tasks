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
.
├── app.py
├── Dockerfile
├── requirements.txt
├── docker-compose.yaml
└── static/
    └── UhXC1nzm3h.jpg
