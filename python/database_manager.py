import sqlite3
from typing import Optional
from enums import BitCategory, BitCondition

def create_tables(cursor):
# 1. Table for Single-Ended Screwdriver Bits
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS screw_bits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        bit_type TEXT NOT NULL,
        size TEXT NOT NULL,
        condition TEXT,
        extra_note TEXT DEFAULT NUll
    )
    ''')

    # 2. Table for Drill Bits
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS drill_bits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        material TEXT NOT NULL,
        size TEXT NOT NULL,
        condition TEXT,
        extra_note TEXT DEFAULT NULL

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
        condition TEXT,
        extra_note TEXT DEFAULT NULL
    )
    ''')
    return

def drop_tables(cursor):
    # This deletes the table structure and all data within them
    cursor.execute("DROP TABLE IF EXISTS screw_bits")
    cursor.execute("DROP TABLE IF EXISTS drill_bits")
    cursor.execute("DROP TABLE IF EXISTS double_ended_bits")

def empty_tables(cursor):
    # This removes all rows but keeps the structure
    cursor.execute("DELETE FROM screw_bits")
    cursor.execute("DELETE FROM drill_bits")
    cursor.execute("DELETE FROM double_ended_bits")
        
    cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('screw_bits', 'drill_bits', 'double_ended_bits')")


def insert_screw(cursor, type, size, condition, extra):
    query = '''
    INSERT INTO screw_bits (bit_type, size, condition, extra_note)
    VALUES (?, ?, ?, ?)
    '''
    cursor.execute(query, (type, size, condition, extra))

def insert_drill(cursor, type, size, condition, extra):
    query = '''
    INSERT INTO screw_bits (bit_type, size, condition, extra_note)
    VALUES (?, ?, ?, ?)
    '''
    cursor.execute(query, (type, size, condition, extra))

def insert_double(cursor, type1, size1, type2, size2, condition, extra):
    query = '''
    INSERT INTO screw_bits (end1_type, end1_size, end2_type, end2_size, condition, extra_note)
    VALUES (?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (type1, size1, type2, size2, condition, extra))


def insert_bit(cursor:sqlite3.Cursor, 
               bit_type:BitCategory, 
               type, size, condition, 
               type2: Optional[str] = None, size2:Optional[str] = None, 
               extra: Optional[str] = None
               ):
    
    #a quick guard against none types make sure this is catched in the frontend.
    params = {"type": type, "size": size, "condition": condition}
    for name, value in params.items():
        if value is None:
            raise ValueError(f"{name} cannot be None")

    match bit_type:
        case BitCategory.SCREW:
            insert_screw(cursor, type, size, condition, extra)
            return
        case BitCategory.DRILL:
            insert_drill(cursor, type, size, condition, extra)
            return
        case BitCategory.DOUBLE:
            params = {"type2": type2, "size2": size2 }
            for name, value in params.items():
                if value is None:
                    raise ValueError(f"{name} cannot be None")
            insert_double(cursor, type, size, type2, size2, condition, extra)
            return







def main():
    conn = sqlite3.connect('workshop_inventory.db')
    cursor = conn.cursor()
    create_tables(cursor)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()

# Connect to the database
