import database.config as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class User:
    #constructor
    def __init__(self,nombre,apellidos,email,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    #para buscar un usuario por email en la bd
    def buscar(llega):
        sql = f'SELECT * FROM usuarios WHERE email="{llega}"'
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    #para guardar un usuario en la bd
    def guardar(self):
        sql="INSERT INTO usuarios VALUE (null,%s,%s,%s,%s,now())" 
        usuario = (self.nombre,self.apellidos,self.email,self.password)
        cursor.execute(sql,usuario)
        database.commit()
        return f'{self.nombre}  Registro exitoso!!'