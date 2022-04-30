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
    
if __name__ == "__main__":
    app.run(debug=True,port=5000)