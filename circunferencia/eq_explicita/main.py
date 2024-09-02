# main.py
from interface.gui import CircleApp
import tkinter as tk

def main():
    root = tk.Tk()
    app = CircleApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
