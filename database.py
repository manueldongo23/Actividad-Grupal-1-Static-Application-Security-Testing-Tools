import sqlite3
import os

DB_NAME = 'secure_notes.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    conn.close()

def get_all_notes():
    conn = get_db_connection()
    notes = conn.execute('SELECT * FROM notes ORDER BY created_at DESC').fetchall()
    conn.close()
    return notes

def search_notes(search_term):
    conn = get_db_connection()
    # SECURE IMPLEMENTATION: Using parameterized queries to prevent SQL Injection
    notes = conn.execute('SELECT * FROM notes WHERE title LIKE ? ORDER BY created_at DESC', (f'%{search_term}%',)).fetchall()
    conn.close()
    return notes

def add_note(title, content):
    conn = get_db_connection()
    with conn:
        conn.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
    conn.close()

def delete_note(note_id):
    conn = get_db_connection()
    with conn:
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.close()
