# Standard Python Libraries
from pathlib import Path
from datetime import datetime
from typing import Optional

# Constants
## Script Orientation
FILE = Path(__file__)
ROOT = FILE.parents[2]
FOLDER = FILE.parent

## Logs
LOG_FOLDER = ROOT / ".logs"

class Logger:
    def __init__(self, folder = LOG_FOLDER) -> None:
        self.folder = folder
        self.cache: list[str] = []

        try:
            self.folder.mkdir(parents=True, exist_ok=True)
        except PermissionError as error:
            raise SystemExit(f"Cannot create log folder.\nError: {error}")

        timestamp = datetime.now().strftime("%y%m%d-%H%M")
        self.path = self.folder / f"sentinel-log{timestamp}.log"

    def append(self, log: str, flush: bool = False, prompt: bool = False) -> bool:
        if prompt:
            print(log)
        
        self.cache.append(log)

        ok = self.flush() if flush else True

        return ok if flush else True

    def flush(self) -> bool:
        try:
            if len(self.cache) > 0:
                with open(self.path, 'a', encoding='utf-8') as f:
                    f.write("\n".join(self.cache) + '\n')
                self.cache.clear()
                return True
        except OSError:
            return False

        return False 