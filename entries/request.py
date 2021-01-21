import sqlite3
import json
from models import Entry

def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.db") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.date,
            e.entry,
            e.mood_id
        FROM Entry e
        """)
        # Initialize an empty list to hold all entry representations
        entries = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # entry class above.
            entry = Entry(row['id'], row['concept'], row['date'],
                        row['entry'], row['mood_id'])
            entries.append(entry.__dict__)
    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.date,
            e.entry,
            e.mood_id
        FROM Entry e
        WHERE e.id = ?
        """, ( id, ))
        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create an entry instance from the current row
        entry = Entry(data['id'], data['concept'], data['date'],
                        data['entry'], data['mood_id'])
        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        DELETE FROM Entry
        WHERE id = ?
        """, (id, ))