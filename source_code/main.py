#!/usr/bin/env python3

import tkinter as tk
from display import Calculator

def main():
    root = tk.Tk()
    root.title("Calculator")
    root.resizable(False, False)
    my_gui = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
