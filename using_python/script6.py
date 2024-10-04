import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Insert a new row into the 'commandes' table
cursor.execute('''
 UPDATE clients 
 SET email = 'goat@gmail.com'
 WHERE id = 3;
               
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()
