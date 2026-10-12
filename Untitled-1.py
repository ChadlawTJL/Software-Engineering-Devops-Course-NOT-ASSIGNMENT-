# Import necessary libraries/modules

from flask import Flask, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('workforce.db')
cursor = conn.cursor()
e S
# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        start_date TEXT,
        location TEXT,
        role TEXT
    )
''')
conn.commit()

# Define routes
@app.route('/employees', methods=['GET', 'POST'])
def manage_employees():
    if request.method == 'GET':
        # Fetch all employees from the database
        cursor.execute('SELECT * FROM employees')
        employees = cursor.fetchall()
        return jsonify(employees)
    elif request.method == 'POST':
        # Add new employee to the database
        data = request.json
        name = data['name']
        start_date = data['start_date']
        location = data['location']
        role = data['role']
        cursor.execute('INSERT INTO employees (name, start_date, location, role) VALUES (?, ?, ?, ?)', (name, start_date, location, role))
        conn.commit()
        return 'Employee added successfully', 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True) 