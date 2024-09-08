import tkinter as tk
import math
from math import tan,cos,sin


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Enhanced Calculator")

        # Display
        self.display = tk.Entry(master, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        button_texts = [  # buttons for calc
            "AC", "(", ")", "/",
            "sin", "cos", "tan", "log",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "%", "0", ".", "="
        ]

        row, col = 1, 0
        for text in button_texts:
            if text == "=":
                button = tk.Button(master, text=text, width=9, height=2, command=self.calculate)
            else:
                button = tk.Button(master, text=text, width=5, height=2, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1


        self.mode_var = tk.StringVar(value="simple")
        self.mode_label = tk.Label(master, text="Mode:")
        self.mode_label.grid(row=row + 1, column=0, padx=5, pady=5)
        self.mode_button = tk.Button(master, textvariable=self.mode_var, width=10, command=self.toggle_mode)
        self.mode_button.grid(row=row + 1, column=1, padx=5, pady=5)

    def button_click(self, text):
        current = self.display.get()
        if text == "AC":
            self.display.delete(0, tk.END)
        elif text == "%":
            self.display.delete(0, tk.END)
            self.display.insert(0, str(float(current) / 100))
        else:
            self.display.insert(tk.END, text)

    def calculate(self):
        try:
            expression = self.display.get()
            if self.mode_var.get() == "scientific":
                expression = expression.replace("sin", "math.sin") \
                    .replace("cos", "math.cos") \
                    .replace("tan", "math.tan") \
                    .replace("log", "math.log10")
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def toggle_mode(self):
        if self.mode_var.get() == "simple":
            self.mode_var.set("scientific")
        else:
            self.mode_var.set("simple")


root = tk.Tk()
calculator = Calculator(root)
root.geometry('500x600')
root.configure(bg="SlateBlue2")
root.mainloop()
