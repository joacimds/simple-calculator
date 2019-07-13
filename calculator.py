import tkinter as tk


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = tk.IntVar()
        self.total_label_text.set(self.total)
        self.total_label = tk.Label(master, textvariable=self.total_label_text)

        self.label = tk.Label(master, text="Total:")

        vcmd = master.register(self.validate)
        self.entry = tk.Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = tk.Button(master, text="+", command=lambda: self.update("add"))
        self.sub_button = tk.Button(master, text="-", command=lambda: self.update("sub"))
        self.clear_button = tk.Button(master, text="C", command=lambda: self.update("clear"))

        # Calculator layout

        self.label.grid(row=0, column=0, sticky=tk.W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=tk.E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=tk.W+tk.E)
        self.add_button.grid(row=2, column=0)
        self.sub_button.grid(row=2, column=1)
        self.clear_button.grid(row=2, column=2, sticky=tk.W+tk.E)

    def validate(self, new_text):
        if not new_text:
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "sub":
            self.total -= self.entered_number
        else:
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, tk.END)


root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
