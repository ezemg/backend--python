# app/config.py

import os

class Config:
     # Configuración común a todos los entornos
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Flor2019!',
        'database': 'codoacodo',
        'port': 3306
    }

class ProductionConfig(Config):
    DEBUG = False
    # Configuración para producción

def get_config():
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig()
    else:
        return DevelopmentConfig()