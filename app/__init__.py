from flask import Flask
from redis import Redis
from pymongo import MongoClient
import pika

def create_app():
    app = Flask(__name__)

    # تنظیمات Redis
    app.redis = Redis(host='redis', port=6379)

    # تنظیمات MongoDB
    app.mongo = MongoClient('mongodb://mongo:27017/')

    # تنظیمات RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    app.rabbitmq_channel = connection.channel()

    with app.app_context():
        from . import routes
        app.register_blueprint(routes.bp)

    return app

