import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Execute a query to fetch all data from a specific table
cursor.execute("SELECT * FROM clients_commandes")
rows = cursor.fetchall()

# Get the column names from the table
column_names = [description[0] for description in cursor.description]

# Open a CSV file to write the data
with open('output.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the column headers to the CSV file
    writer.writerow(column_names)

    # Write the rows of data to the CSV file
    writer.writerows(rows)

# Close the database connection
conn.close()

print("Data exported successfully to 'output.csv'")
