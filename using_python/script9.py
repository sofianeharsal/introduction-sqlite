import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Insert a new row into the 'commandes' table
cursor.execute('''
        SELECT produits 
        FROM clients_commandes
        WHERE nom = 'sam' AND prenom = 'konte'
               ''')
        
orders = cursor.fetchall()
print('Orders for sam konte :')
for order in orders :
   print(order)               


# Close the connection
conn.close()
