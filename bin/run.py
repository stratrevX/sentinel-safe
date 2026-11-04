# Standard Python Libraries
import sys

# Local Python Libraries
from src.database.integrity import integrity

class Procedure:
    def __init__(self) -> None:
        if integrity() is False:
            print("Database integrity check did not pass.")
            sys.exit(1)

        self.interface()

    def interface(self) -> None:
        pass # interface() in an eventual future...

if __name__ == "__main__":
    Procedure()