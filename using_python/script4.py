import sqlite3


conn = sqlite3.connect('db.db')
cursor = conn.cursor()

    
cursor.execute("SELECT nom, prenom FROM clients")  

    
results = cursor.fetchall()

    
for row in results:
        print(row)
