import sqlite3

# Connect to the database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Query all rows in the task table
cursor.execute("SELECT * FROM task")
tasks = cursor.fetchall()

# Print each task
for task in tasks:
    print(task)

# Close the connection
conn.close()

