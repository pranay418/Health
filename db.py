
import sqlite3
import datetime

conn = sqlite3.connect("health.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    sugar REAL,
    hba1c REAL,
    hemoglobin REAL,
    cholesterol REAL,
    bp REAL,
    diseases TEXT
)
""")

conn.commit()

def save_report(data, diseases):
    cursor.execute("""
    INSERT INTO reports (timestamp, sugar, hba1c, hemoglobin, cholesterol, bp, diseases)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        str(datetime.datetime.now()),
        data.get("sugar", 0),
        data.get("hba1c", 0),
        data.get("hemoglobin", 0),
        data.get("cholesterol", 0),
        data.get("bp", 0),
        ",".join(diseases)
    ))
    conn.commit()

def get_history():
    cursor.execute("SELECT * FROM reports ORDER BY id DESC")
    return cursor.fetchall()
