import mysql.connector

class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host= 'localhost',
            database = 'prueba',
            user = 'root',
            password = 'n4huel.d3v__'
        )

    def insertarData(self,nombre,color,tipo):
        cur = self.conexion.cursor()
        sql= '''INSERT INTO productos(nombre,color,tipo)
        VALUES('{}','{}','{}')'''.format(nombre,color,tipo)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
    
    def mostrarData(self):
        cursor = self.conexion.cursor()
        sql= "SELECT * FROM productos"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def buscarData(self,nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE nombre = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX= cur.fetchall()
        cur.close()
        return nombreX
    
    def eliminarData(self,nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()