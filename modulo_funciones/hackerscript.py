import os
import time
import random

def main():
    time.sleep(random.randint(1, 1000))
    desktop_path = os.path.join(os.getenv("HOME"), "Desktop")
    archivo_path = os.path.join(desktop_path, "PARA TI.txt")
    with open(archivo_path, "w") as archive:
        archive.write("Soy un hacker")

if __name__ == "__main__":
    main()