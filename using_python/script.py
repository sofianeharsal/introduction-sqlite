import sqlite3

# Connect to the database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Create the 'clients' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER NOT NULL PRIMARY KEY,  
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT NOT NULL,
    date_inscription DATE NOT NULL
);
''')

# Create the 'commandes' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS commandes (
    id INTEGER NOT NULL PRIMARY KEY,  
    client_id INTEGER NOT NULL,  
    produits TEXT NOT NULL, 
    date_commande DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id)
);
''')

# Insert data into the 'clients' table
cursor.execute('''
INSERT INTO clients (id, nom, prenom, email, date_inscription)
VALUES 
    (1, 'sam', 'konte', 'samkonte@gmail.com', '2024-01-12'),
    (2, 'mike', 'bridge', 'mikebridge@gmail.com', '2024-10-21')
ON CONFLICT(id) DO NOTHING;
''')

# Insert data into the 'commandes' table
cursor.execute('''
INSERT INTO commandes (id, client_id, produits, date_commande)
VALUES 
    (10, 1, 'bike', '2024-01-13'),
    (10, 1, 'car', '2024-03-11'),
    (11, 2, 'scooter', '2024-10-22')
ON CONFLICT(id) DO NOTHING;
''')

# Commit changes
conn.commit()

# Close the connection
conn.close()
