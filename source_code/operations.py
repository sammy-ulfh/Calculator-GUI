#!/usr/bin/env python3

import tkinter as tk

class Operation:

    def __init__(self, display):
        self.display = display
        self.display_text = ''
        self.current = ''
        self.op = ''
        self.last_number = 0
        self.numbers = []
        self.operations = []
        self.total = 0
        self.status = 0
        self.zero_total = False

    def clear_display(self):
        self.display.delete(0, tk.END)
        self.display_text = ''
        self.current = ''
        self.op = ''
        self.last_number = 0
        self.numbers = []
        self.operations = []
        self.total = 0
        self.status = 0
        self.zero_total = False

    def save_numbers(self):
        self.current = ''
        self.numbers = []
        self.operations = []
        self.total = 0

        try:

            for i in range(len(self.display_text)):
                if not self.display_text[i] in "/*-+":
                    self.current += self.display_text[i]
                else:
                    if not self.current:
                        self.current = '0'
                    self.numbers.append(float(self.current))
                    self.operations.append(self.display_text[i])
                    self.current = ''

                if i == (len(self.display_text) - 1):
                    if self.display_text[i] in "/*-+":
                        self.operations.append(self.display_text[i])
                    else:
                        self.numbers.append(float(self.current))
        except ValueError:
            self.clear_display()
            self.display.insert("end", "Syntax Error")
            self.display_text = "Syntax Error"
            return
        except:
            return

        if self.numbers and self.status == 0:
            self.last_number = self.numbers[-1]
            self.status +=1
        if self.operations and self.status == 1:
            self.op = self.operations[-1]
            self.status += 1

    def delete_data(self):

        if self.display_text:
            if self.display_text[-1] in "/*-+":
                self.display_text = self.display_text[0:-1]
            else:
                self.display_text = self.display_text[0:-1]
            self.display.delete(0, "end")
            self.display.insert("end", self.display_text)
            self.save_numbers()

    def calculate(self):

        self.save_numbers()


        if len(self.numbers) == 1:
            if self.op == "/":
                self.numbers[0] /= self.last_number
            elif self.op == "*":
                self.numbers[0] *= self.last_number
            elif self.op == "-":
                self.numbers[0] -= self.last_number
            elif self.op == "+":
                self.numbers[0] += self.last_number

        try:
            while "/" in self.operations:

                index = self.operations.index("/")

                if float(self.numbers[index + 1]) == 0:
                    self.clear_display()
                    self.display.insert("end", "Zero Division Error")
                    self.display_text = "Zero Division Error"
                    return

                self.total += self.numbers[index] / self.numbers[index + 1]
                self.numbers[index + 1] = self.numbers[index] / self.numbers[index + 1]
                del self.numbers[index]
                del self.operations[index]

            while "*" in self.operations:

                index = self.operations.index("*")

                self.total += self.numbers[index] * self.numbers[index + 1]
                self.numbers[index + 1] = self.numbers[index] * self.numbers[index + 1]
                del self.numbers[index]
                del self.operations[index]

            while "-" in self.operations:

                index = self.operations.index("-")

                self.total += self.numbers[index] - self.numbers[index + 1]
                self.numbers[index + 1] = self.numbers[index] - self.numbers[index + 1]
                del self.numbers[index]
                del self.operations[index]

            while "+" in self.operations:

                index = self.operations.index("+")

                self.total += self.numbers[index] + self.numbers[index + 1]
                self.numbers[index + 1] = self.numbers[index] + self.numbers[index + 1]
                del self.numbers[index]
                del self.operations[index]
        except:
            self.clear_display()
            self.display.insert("end", "Syntax Error")
            self.display_text = "Syntax Error"
            return

        try:
            self.total = self.numbers[0]
        except:
            return
        if self.total == 0:
            self.zero_total = True
        self.current = ''
        self.display_text = str(self.total)


        self.display.delete(0, tk.END)
        self.display.insert("end", round(self.total, 2))


    def click(self, key):

        if self.total != 0:
                self.current = str(self.total)
                self.display_text = self.current
                self.op = ''
                self.last_number = 0
                self.numbers = []
                self.operations = []
                self.total = 0

        if self.display_text == "Zero Division Error" or self.display_text == "Syntax Error":
            self.clear_display()

        if key in "0123456789" or key == ".":
            if self.zero_total:
                self.clear_display()

            if not self.current and key == ".":
                self.current = '0'
                self.display.insert("end", "0")

            self.current += key
            self.display.insert("end", key)
            self.display_text += key
        else:
            if self.zero_total:
                self.current = str(self.total)
                self.display_text = self.current
                self.op = ''
                self.last_number = 0
                self.numbers = []
                self.operations = []
                self.total = 0
                self.zero_total = False

            if self.current and not self.display_text[-1] in "/*-+":
                self.display.insert("end", key)
                self.display_text += key
                self.current = ''
            else:
                try:
                    if not key == self.operations[-1]:
                        self.operations[-1] = key
                        self.display_text = self.display_text[0:-1] + key
                        self.display.delete(0, "end")
                        self.display.insert("end", self.display_text)
                except:
                    self.clear_display()
                    self.current = '0'
                    self.display_text = self.current + key
                    self.display.delete(0, tk.END)
                    self.display.insert("end", self.display_text)
                    self.numbers.append(float(self.current))
                    self.operations.append(key)
                    self.current = ''

