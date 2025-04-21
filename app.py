from flask import Flask, jsonify, send_from_directory, render_template_string
import redis
import os
import time

app = Flask(__name__)

# Подключение к Redis
redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = int(os.environ.get("REDIS_PORT", 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

# Ждём, пока Redis не поднимется
for _ in range(10):
    try:
        redis_client.ping()
        break
    except redis.exceptions.ConnectionError:
        time.sleep(1)

# Главная страница
@app.route("/")
def index():
    return render_template_string("""
        <h1>Добро пожаловать!</h1>
        <ul>
            <li><a href="/ping">/ping</a></li>
            <li><a href="/count">/count</a></li>
            <li><a href="/image">/image</a></li>
        </ul>
    """)

@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})

@app.route("/count")
def count():
    count = redis_client.incr("visits")
    return jsonify({"visits": count})

@app.route("/image")
def image():
    return send_from_directory("static", "UhXC1nzm3h.jpg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
