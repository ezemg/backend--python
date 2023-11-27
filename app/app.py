# app/app.py
from flask import Flask
from routes.cursos_routes import cursos_routes
from config import DB_CONFIG
from db import get_db

app = Flask(__name__)
app.config['DB_CONFIG'] = DB_CONFIG

# # Registrar las rutas
app.register_blueprint(cursos_routes)

if __name__ == '__main__':
    app.run(debug=True)
