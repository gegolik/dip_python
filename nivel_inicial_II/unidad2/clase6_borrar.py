import sqlite3

def crear_base():
    bd = sqlite3.connect("baseprueba.db")
    return bd

def borrar(bd, mi_id):
    cursor = bd.cursor()
    data = (int(mi_id),)
    sql = "DELETE FROM persona WHERE ID = ?"
    cursor.execute(sql, data)
    bd.commit()
    

bd = crear_base()
borrar(bd, 2)

