import sqlite3

conn = sqlite3.connect('parking.db')
cursor = conn.cursor()

# Show all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables:", tables)

# Show rows from each table
for (table,) in tables:
    print(f"\n--- {table} ---")
    cursor.execute(f"SELECT * FROM {table} LIMIT 10")
    columns = [d[0] for d in cursor.description]
    print(columns)
    for row in cursor.fetchall():
        print(row)

conn.close()