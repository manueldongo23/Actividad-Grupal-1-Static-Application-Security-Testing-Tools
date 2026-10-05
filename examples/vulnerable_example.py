"""
=========================================================
🚨 DO NOT USE IN PRODUCTION 🚨
EDUCATIONAL PURPOSE ONLY

This file demonstrates a SQL Injection vulnerability 
caused by string concatenation. 
It is intended for SAST detection demonstration.
=========================================================
"""
import sqlite3

def search_notes_vulnerable(search_term):
    conn = sqlite3.connect('secure_notes.db')
    cursor = conn.cursor()
    
    # VULNERABLE CODE: SQL string concatenation
    # An attacker could input: ' OR '1'='1
    query = "SELECT * FROM notes WHERE title LIKE '%" + search_term + "%'"
    
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()
