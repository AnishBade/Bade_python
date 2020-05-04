import sqlite3
with sqlite3.connect("sqlite_tutorial_1.db") as db:
    cursor=db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user(userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,firstname VARCHAR(20) NOT NULL,surname VARCHAR(20)
 NOT NULL,password VARCHAR(20) NOT NULL);''')
cursor.execute("DELETE FROM user")
cursor.execute('''INSERT INTO user(username,firstname,surname,password) VALUES
('TEST_USER','Anish','Bade','password')       ''')
db.commit()
#cursor.execute("SELECT *FROM user")
cursor.execute("SELECT firstname,surname FROM user")
print(cursor.fetchall())