import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Insert a new row into the 'commandes' table
cursor.execute('''
        SELECT produits 
        FROM commandes
        WHERE client_id = 1
               ''')
        
orders = cursor.fetchall()
print('Orders for client_id = 1 :')
for order in orders :
   print(order)               


# Close the connection
conn.close()
