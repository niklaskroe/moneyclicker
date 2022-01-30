from itertools import tee
from tkinter import *
from tkinter import messagebox

Form1 = Tk()
Form1.title("Money Clicker")
Form1.option_add('*Font', 'Arial', '12')

Form1.balance = 5
Form1.clickmultiplier = 1
Form1.upgrade_multiplier = 10
Form1.autoclicker = 1

def money_click():
    Form1.balance = Form1.balance + Form1.clickmultiplier
    balance_label.config(text="Balance: " + str(Form1.balance) + " $")

def upgrade_click():
    if Form1.balance >= Form1.upgrade_multiplier:
        Form1.clickmultiplier *= 2
        Form1.balance -= Form1.upgrade_multiplier
        balance_label.config(text="Balance: " + str(Form1.balance) + " $")
        Form1.upgrade_multiplier = Form1.upgrade_multiplier * 2
        multiplier_label.config(text="Multiplier: " + str(Form1.clickmultiplier))
        upgrade_multiplier_button.config(text="Upgrade " + str(Form1.upgrade_multiplier) + " $")
    else:
        messagebox.showinfo(message="You don't have enough money to upgrade!")

def upgrade_autoclick():
    print("test")

main_frame = LabelFrame(Form1, text="Main")

# main buttons
balance_label = Label(main_frame, text="Balance: " + str(Form1.balance) + " $")
multiplier_label = Label(main_frame, text="Multiplier: " + str(Form1.clickmultiplier))
clicker_button = Button(main_frame, text="Earn Money", command=money_click)
upgrade_multiplier_button = Button(main_frame, text="Upgrade", command=upgrade_click)

# main position
main_frame.grid(column=0, row=0, padx=5, pady=5)
multiplier_label.grid(column=0, row=0, padx=10, pady=10)
balance_label.grid(column=1, row=0, padx=10, pady=10)
clicker_button.grid(column=1, row=1, padx=10, pady=10)
upgrade_multiplier_button.grid(column=0, row=1, padx=10, pady=10)

Form1.mainloop()