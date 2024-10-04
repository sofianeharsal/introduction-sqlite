import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Insert a new row into the 'commandes' table
cursor.execute('''
INSERT INTO commandes (id, client_id, produits, date_commande)
VALUES (12, 1, 'laptop', '2024-11-01');
        ''')

# Commit the changes
conn.commit()

# Close the connection
conn.close()
