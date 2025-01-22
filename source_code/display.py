#!/usr/bin/env python3

import tkinter as tk
from operations import Operation

class Calculator:

    def __init__(self, master):
        self.master = master
        self.master.config(bg="gray")
        self.display = tk.Entry(self.master, width=16, bd=8, bg="lightgray", font=("Arial", 23), justify="right", fg="black")
        self.display.grid(row=0, column=0, columnspan=4)
        self.operations = Operation(self.display)

        row = 1
        col = 0

        buttons = [
            "7", "8", "9", "DEL",
            "4", "5", "6", "/",
            "1", "2", "3", "*",
            "C", "0", ".", "-",
            "=", "+"
            ]

        for button in buttons:
            self.build_button(button, row, col)

            col += 1

            if col > 3:
                row +=1
                col = 0

        self.master.bind("<Key>", self.key_events)

    def key_events(self, event):
        key = event.char

        if key in "0123456789./*-+":
            self.operations.click(key)
        elif key == '\r':
            self.operations.calculate()
        elif key == '\x20':
            self.operations.clear_display()
        elif key == '\x08':
            self.operations.delete_data()
        elif key == '\x1B':
            self.master.quit() # Close calculator

    def build_button(self, button, row, col):
        if button == "C":
            b = tk.Button(self.master, text=button, width=4, height=2, command=lambda: self.operations.clear_display())
            b.grid(row=row, column=col, pady=(3, 3), padx=(3, 3))
        elif button == "=":
            b = tk.Button(self.master, text=button, width=22, height=2, command= lambda: self.operations.calculate())
            b.grid(row=row, column=col, columnspan=3, pady=(3, 5), padx=(3,3))
        elif button == "DEL":
            b = tk.Button(self.master, text=button, width=4, height=2, command=lambda: self.operations.delete_data())
            b.grid(row=row, column=col, pady=(3,3), padx=(3, 3))
        elif button == "+":
            b = tk.Button(self.master, text=button, width=4, height=2, command=lambda: self.operations.click(button))
            b.grid(row=row, column=3, pady=(3, 6), padx=(2, 3))
        else:
            b = tk.Button(self.master, text=button, width=4, height=2, command=lambda: self.operations.click(button))
            b.grid(row=row, column=col, pady=(3,3), padx=(3, 3))
