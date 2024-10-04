import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Insert a new row into the 'commandes' table
cursor.execute('''
INSERT INTO clients (id, nom, prenom, email, date_inscription)
VALUES (3, 'cristiano', 'ronaldo', 'cr7@gmail.com', '2024-12-31');
''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()
