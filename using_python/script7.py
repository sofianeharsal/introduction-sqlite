import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Delete a row from the 'clients' table where id = 1
cursor.execute('''
DELETE FROM commandes
WHERE id = 12;
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()
