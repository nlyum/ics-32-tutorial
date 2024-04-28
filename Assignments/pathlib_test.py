from pathlib import Path
from shlex import split

if __name__ == "__main__":
    path1 = Path("C:/Users/natha/OneDrive/Desktop/UCI/ICS32/")
    path1.mkdir(exist_ok = True)
    
    filename1 = input("Filename: ")
    filepath1 = path1 / filename1
    
    filepath2 = Path("C:/Users/natha/OneDrive/Desktop/UCI/ICS32/a1_test_2024-04-26-00-20-54/Zzz/read.dsu")

    f = filepath2.open("r")
    
    for line in f.readlines():
        print(line, end = '')
    
    print()
    f.close()