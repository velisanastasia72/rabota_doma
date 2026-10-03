import sqlite3

conn = sqlite3.connect('db_2.db')
cursor = conn.cursor()

query = "SELECT DISTINCT city FROM customers;"

cursor.execute(query)
results = cursor.fetchall()

print("Города заказчиков:")
for row in results:
    print(row[0])

conn.close()

