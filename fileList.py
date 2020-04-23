import sqlite3

conn = sqlite3.connect('file2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_files TEXT\
        )")
    conn.commit()
conn.close()

conn =  sqlite3.connect('file2.db')

fileList = ['information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']

for f in fileList:
    if f.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files(col_files) VALUES (?);",(f,))
            cur.execute("INSERT INTO tbl_files(col_files) VALUES (?);",(f,))
            conn.commit()
            print(f)
conn.close()
