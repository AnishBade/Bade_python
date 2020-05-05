import sqlite3
with sqlite3.connect("week_2_assignment.sqlite") as db:
    cur=db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS email_count(email VARCHAR(100),count INTEGER)''')
file_name=input("Enter a file name::")
if len(file_name)<1 : file_name="mbox.txt"
file=open(file_name)
for line in file:
    if not line.startswith("From: "):continue
    words=line.split()
    email=words[1]
    cur.execute("SELECT count FROM email_count WHERE email=?", (email,))
    row=cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO email_count(email,count) VALUES(?,?)''',(email,1))
    else:
        cur.execute('''UPDATE email_count SET count=count+1 WHERE email=?''', (email, ))

db.commit()
#cur.execute('''SELECT *FROM email_count ORDER BY count DESC''')
#print(cur.fetchall())
sqlstr = 'SELECT email,count FROM  email_count ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()


