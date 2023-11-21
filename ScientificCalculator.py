import math
import tkinter as tk

class ScientificCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("435x400")
        self.root.resizable(False, False)

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_gui()

    def create_gui(self):
        entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 20), bd=10, insertwidth=4, width=20, justify='right')
        entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("(", 4, 1), (")", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("Del", 5, 1), ("=", 5, 2),
            ("sin", 1, 4), ("cos", 2, 4), ("tan", 3, 4),
            ("sqrt", 4, 4), ("log", 5, 4),
            ("pi", 1, 5), ("e", 2, 5), ("x^2", 3, 5), ("x^y", 4, 5), ("ln", 5, 5),
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, width=6, height=2, bg='yellow', command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, padx=10, pady=10)

    def button_click(self, value):
        if value == "=":
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except ZeroDivisionError:
                self.result_var.set("Math Error")
            except Exception as e:
                self.result_var.set("Error")
        elif value == "C":
            self.result_var.set("")
        elif value == "Del":
            current_text = self.result_var.get()
            self.result_var.set(current_text[:-1])
        else:
            current_text = self.result_var.get()
            new_text = current_text + value
            self.result_var.set(new_text)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    app.run()
