from pathlib import Path
from shlex import split

if __name__ == "__main__":
    path1 = Path("/Users/natha/OneDrive/Desktop/UCI/ICS 32")
    path1.mkdir(exist_ok = True)
    
    filename1 = input("Filename: ")
    filepath1 = path1 / filename1
    f = filepath1.open("w")
    f.close