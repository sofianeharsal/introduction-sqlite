CREATE TABLE clients (
    id INTEGER NOT NULL PRIMARY KEY,  
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT NOT NULL,
    date_inscription DATE NOT NULL
); 

CREATE TABLE commandes (
    id INTEGER NOT NULL PRIMARY KEY,  
    client_id INTEGER NOT NULL,  
    produits TEXT NOT NULL, 
    date_commande DATE,
    FOREIGN KEY (client_id) REFERENCES clients(id)  
); 

INSERT INTO clients (id, nom, prenom, email, date_inscription)
VALUES 
    (1, 'sam', 'konte', 'samkonte@gmail.com', '2024-01-12'),
    (2, 'mike', 'bridge', 'mikebridge@gmail.com', '2024-10-21');

INSERT INTO commandes (id, client_id, produits, date_commande)
VALUES 
    (10, 1, 'bike', '2024-01-13'),
    (11, 2, 'scooter', '2024-10-22');
