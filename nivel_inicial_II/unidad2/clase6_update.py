import sqlite3

def crear_base():
    bd = sqlite3.connect("baseprueba.db")
    return bd

def actualizar(bd, mi_id, nombre):
    cursor = bd.cursor()
    data = (nombre, int(mi_id))
    sql = "UPDATE persona SET Nombre = ? WHERE ID = ?"
    cursor.execute(sql, data)
    bd.commit()
    

bd = crear_base()
actualizar(bd, 1, "Jose")

