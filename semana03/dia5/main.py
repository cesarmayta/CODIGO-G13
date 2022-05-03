from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

app = Flask(__name__)

#CONEXION A MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_colegio'

mysql = MySQL(app)

@app.route('/')
def index():
    return jsonify({
        'status':'OK',
        'mensaje':'Bienvenido a mi apirest con Flask'
    })
    
@app.route('/alumno')
def getAlumno():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from tbl_alumno")
    
    data = cursor.fetchall()
    
    cursor.close()
    
    print(data)
    
    return jsonify({
        'ok':True,
        "message":"lista de alumnos",
        "content":data
    })
    
@app.route('/alumno',methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    celular = request.json['celular']
    github = request.json['github']
    
    cursor = mysql.connection.cursor()
    
    cursor.execute("insert into tbl_alumno(alumno_nombre,alumno_celular,alumno_github) values('"+ nombre +"','"+ celular +"','"+ github +"')")
    
    mysql.connection.commit()
    
    cursor.close()
    
    return jsonify({
        "ok":True,
        "message":"registro insertado exitosamente"
    })

@app.route('/alumno/<id>')
def getAlumnoById(id):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from tbl_alumno where alumno_id = '"+ id +"'")
    
    data = cursor.fetchall()
    
    cursor.close()
    
    print(data)
    
    return jsonify({
        'ok':True,
        "message":"datos de un alumno",
        "content":data
    })

@app.route('/alumno/<id>',methods=['PUT'])
def updateAlumno(id):
    nombre = request.json['nombre']
    email = request.json['email']
    celular = request.json['celular']
    github = request.json['github']

    cursor = mysql.connection.cursor()
    sqlUpdateAlumno = "update tbl_alumno set "
    sqlUpdateAlumno += "alumno_nombre='"+ nombre +"',alumno_email='"+ email +"'"
    sqlUpdateAlumno += ",alumno_celular='"+ celular+"',alumno_github='"+ github +"' "
    sqlUpdateAlumno += "where alumno_id = '"+ id +"'"
    cursor.execute(sqlUpdateAlumno)

    mysql.connection.commit()
    
    cursor.close()
    
    return jsonify({
        "ok":True,
        "message":"registro actualizado exitosamente"
    })

@app.route('/alumno/<id>',methods=['DELETE'])
def deleteAlumno(id):
    
    cursor = mysql.connection.cursor()
    sqlDeleteAlumno = "delete from tbl_alumno "
    sqlDeleteAlumno += "where alumno_id = '"+ id +"'"
    cursor.execute(sqlDeleteAlumno)

    mysql.connection.commit()

    cursor.close()

    return jsonify({
        "ok":True,
        "message":"registro eliminado exitosamente"
    })
    


if __name__ == "__main__":
    app.run(debug=True,port=5000)

   