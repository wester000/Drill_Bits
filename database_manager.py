import sqlite3

# Connect to the database
conn = sqlite3.connect('workshop_inventory.db')
cursor = conn.cursor()

# 1. Table for Single-Ended Screwdriver Bits
cursor.execute('''
CREATE TABLE IF NOT EXISTS screw_bits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bit_type TEXT NOT NULL,
    size TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    condition TEXT
)
''')

# 2. Table for Drill Bits
cursor.execute('''
CREATE TABLE IF NOT EXISTS drill_bits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material TEXT NOT NULL,
    size TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    condition TEXT
)
''')

# 3. Table for Double-Ended Bits
cursor.execute('''
CREATE TABLE IF NOT EXISTS double_ended_bits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    end1_type TEXT NOT NULL,
    end1_size TEXT NOT NULL,
    end2_type TEXT NOT NULL,
    end2_size TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    condition TEXT
)
''')

conn.commit()
conn.close()
