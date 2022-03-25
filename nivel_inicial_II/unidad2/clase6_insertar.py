import sqlite3

def crear_base():
    bd = sqlite3.connect("baseprueba.db")
    return bd

def insertar(bd, nombre, mi_id):
    cursor = bd.cursor()
    data = (int(mi_id), nombre)
    sql = "INSERT INTO persona(id, nombre) VALUES (?,?)"
    cursor.execute(sql, data)
    bd.commit()
    

bd = crear_base()
insertar(bd, "Oscar2", 5)

