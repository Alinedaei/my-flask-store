import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://localhost:6379/0'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/mydatabase'

