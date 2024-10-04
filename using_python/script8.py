import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Create a new table by joining 'clients' and 'commandes'
fusion_table = '''
CREATE TABLE IF NOT EXISTS clients_commandes AS
SELECT 
    clients.id AS client_id, 
    clients.prenom, 
    clients.nom,
    commandes.produits,
    commandes.date_commande

FROM 
    clients 
INNER JOIN 
    commandes ON clients.id = commandes.client_id;
'''

# Execute the create table query
cursor.execute(fusion_table)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
