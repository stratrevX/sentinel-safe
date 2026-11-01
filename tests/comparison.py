import sqlite3
from pathlib import Path

db1 = Path(__file__).parent / 'bookstore.db'
db2 = Path(__file__).parent / 'fitness.db'
databases = [db1, db2]

print(db1, db2)

def get_data():
    pass