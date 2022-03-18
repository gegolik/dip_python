import sqlite3

def crear_base():
    bd = sqlite3.connect("baseprueba.db")
    return bd

def crear_tabla(bd):
    cursor = bd.cursor()
    sql = "CREATE TABLE persona(id integer PRIMARY KEY, nombre text)"
    cursor.execute(sql)
    bd.commit()
    



bd = crear_base()
crear_tabla(bd)

