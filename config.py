# config.py
import os

class Config:
    SECRET_KEY = 'clave_secreta'
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database', 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False