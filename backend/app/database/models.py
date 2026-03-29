from app.database.db import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        state TEXT,
        strategy TEXT
    )
    """)

    conn.commit()
    conn.close()
