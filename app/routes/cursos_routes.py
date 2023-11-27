from flask import Blueprint, jsonify, request
from db import get_db

cursos_routes = Blueprint('curso_routes', __name__)

@cursos_routes.route('/cursos', methods=['GET'])
def obtener_cursos():
    try:
        db = get_db()
        cursor = db.cursor()  
        sql = "SELECT * FROM curso"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos=[]
        for fila in datos:
            curso={
                'codigo': fila[0],
                'nombre': fila[1],
                'creditos': fila[2]}
            cursos.append(curso)
        return jsonify({'cursos': cursos, 'mensaje': 'Cursos listados', 'count': len(cursos)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cursos_routes.route('/cursos', methods=['POST'])
def registrar_curso():
    try:
        db = get_db()
        cursor = db.cursor()  
        sql = '''INSERT INTO curso (nombre, creditos)
        VALUES('{0}', '{1}')'''.format(request.json['nombre'], request.json['creditos'])
        cursor.execute(sql)
        
        db.commit()
        return jsonify({'mensaje': 'Curso Registrado'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

@cursos_routes.route('/cursos/<int:curso_id>', methods=['PUT'])
def update_curso(curso_id):
    return jsonify({"message": f"PUT request to /cursos/{curso_id}"})

@cursos_routes.route('/cursos/<int:curso_id>', methods=['DELETE'])
def delete_curso(curso_id):
    return jsonify({"message": f"DELETE request to /cursos/{curso_id}"})

