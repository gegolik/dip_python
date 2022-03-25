import sqlite3

def crear_base():
    bd = sqlite3.connect("baseprueba.db")
    return bd

def seleccionar(bd, mi_id):
    cursor = bd.cursor()
    data = (int(mi_id),)
    sql = "SELECT * FROM persona WHERE id= ?"
    cursor.execute(sql, data)
    bd.commit()
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    


bd = crear_base()
seleccionar(bd, 1)

