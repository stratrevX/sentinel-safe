# Standard Python Libraries
import os
from platform import system as opSys

from typing import Any

from pathlib import Path
# Constants
MACHINE = opSys()

# Functions
def clear():
    # By learning what OS is the machine running, it translates the command to clear the terminal.
    os.system("cls" if MACHINE == "Windows" else "clear")

def eligibility(shipped: Any, desired: type, allowed_none: bool = False) -> bool:
    # Given two parameters, shipped and desired, checks whether shipped belongs to the same classtype as the desired class.
    if not isinstance(shipped, desired): 
        return False

    if shipped is None:
        return allowed_none
    
    return True

def system_fetch(path: Path) -> bool:
    # Fetches whatever path it is given
    if path.exists() is True:
        return True 

    return False

if __name__ == "__main__":
    # Eligibility Function Check
    print(eligibility(shipped=3, desired=int))
    print(eligibility(shipped="string", desired=str)) 