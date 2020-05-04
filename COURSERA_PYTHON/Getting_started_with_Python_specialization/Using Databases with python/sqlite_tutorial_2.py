import sqlite3
with sqlite3.connect("sqlite_tutorial_2.db") as db:
    cursor=db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user(userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,firstname VARCHAR(20) NOT NULL,surname VARCHAR(20)
 NOT NULL,password VARCHAR(20) NOT NULL);''')
cursor.execute("DELETE FROM user")
cursor.execute('''INSERT INTO user(username,firstname,surname,password) VALUES
('TEST_USER','Anish','Bade','password')       ''')
db.commit()


def new_user():
    found = 0
    while found == 0:
        name = input("Enter a username:")
        with sqlite3.connect("sqlite_tutorial_2.db") as db:
            cursor=db.cursor()
            cursor.execute("SELECT firstname,surname FROM user WHERE username=?",[(name)])
        if cursor.fetchall():
            print("The username you entered already exists.Try using another username.")
        else:

            found=1
        firstname=input("Enter your first name:")
        surname=("Enter your last name:")
        password=input("Enter a Password:")
        password1=input("Re-Enter your Password:")
        while password!=password1:
            print("You entered wrong password.Please enter your password again:")
            password1 = input("Re-Enter your Password:")
    cursor.execute('''INSERT INTO user(username,firstname,surname,password) VALUES(name,firstname,surname,password)''')
    db.commit()
new_user()
cursor.execute("SELECT *FROM user")
print(cursor.fetchall())