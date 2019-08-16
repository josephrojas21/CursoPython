import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=144.217.222.96; DATABASE=NUCLEO_DE_ASIGNACIONES; UID=tecnomedios; PWD=a2llcm8tc2VydmVy')

with conn:
    query = """SELECT 
    id_dispositivo, url_del_video
    FROM 
    tbl_video_asignaciones"""
    crsr = conn.execute(query)
    rows = crsr.fetchall()
for row in rows:
    with open('test.txt','a') as file:
        file.writelines(str(row[0])+'|'+str(row[1])+'\n')