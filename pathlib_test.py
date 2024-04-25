from pathlib import Path
from shlex import split

if __name__ == "__main__":
    path1 = Path("/Users/natha/OneDrive/Desktop/UCI/ICS 32")
    file1 = path1 / ("test_create" + ".dsu")
    file1.mkdir()