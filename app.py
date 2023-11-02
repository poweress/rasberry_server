import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Создание базы данных
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS frequency_converter_data
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_name TEXT NOT NULL,
    current FLOAT,
    voltage FLOAT,
    rpm FLOAT,
    frequency FLOAT,
    temperature FLOAT,
    torque FLOAT,)''')
conn.commit()

@app.route('/add_data/<string:station_name>/<float:current>/<float:voltage>/<float:rpm>/<float:frequency>/<float:temperature>/<float:torque>')
def add_data(station_name, current, voltage, rpm, frequency, temperature, torque):
    c.execute("INSERT INTO frequency_converter_data (station_name, current, voltage, rpm, frequency, temperature, torque) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (station_name, current, voltage, rpm, frequency, temperature, torque))
    conn.commit()
    return 'Data added successfully'

@app.route('/get_data/<string:station_name>')





























if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")