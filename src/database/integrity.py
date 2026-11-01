# Standard Python Libraries
import os
import sys
import sqlite3

from pathlib import Path

# Local Python Libraries
from src.utilities.utilities import eligibility, system_fetch

# Third-Party Python Libraries
from echolog import infoLog, successLog, warnLog, errorLog

# Constants

ROOT = Path(__file__).parents[2]
DATABASE_FOLDER = ROOT / 'database' 
DATABASE = ROOT / 'database' / 'database.db'

def create_database():
    if DATABASE_FOLDER.exists() is False:
        Path(DATABASE_FOLDER).mkdir(parents=True, exist_ok=True)



# Runtime
if __name__ == "__main__":
    pass