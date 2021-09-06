import sqlite3

cnt = sqlite3.connect('topic.db')
result = cnt.execute('SELECT * FROM topic')
rows = result.fetchall()
for row in rows:
    print(row)
