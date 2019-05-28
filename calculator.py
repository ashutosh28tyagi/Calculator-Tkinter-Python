import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Calculator")

label1 = tk.Label(mainWindow, text="Enter First Number")
label1.pack()

first = tk.Entry(mainWindow)
first.pack()

label2 = tk.Label(mainWindow, text="Enter Second Number")
label2.pack()

second = tk.Entry(mainWindow)
second.pack()

label3 = tk.Label(mainWindow, text="Operation")
label3.pack()

bsum = tk.Button(mainWindow, text="+", command = lambda: add())
bsum.pack()

bsub = tk.Button(mainWindow, text="-", command = lambda: sub())
bsub.pack()

bmul = tk.Button(mainWindow, text="*", command = lambda: mul())
bmul.pack()

bdiv = tk.Button(mainWindow, text="/", command = lambda: div())
bdiv.pack()

label4 = tk.Label(mainWindow, text="")
label4.pack()

def add():
    try:
        n1 = int(first.get())
        n2 = int(second.get())
        result = n1 + n2
        label4.config(text='Addition Result is:'+ str(result))
    except ValueError:
        label4.config(text="You can only enter integer numbers.")

def sub():
    try:
        n1 = int(first.get())
        n2 = int(second.get())
        result = n1 - n2
        label4.config(text='Subtraction Result is:'+ str(result))
    except ValueError:
        label4.config(text="You can only enter integer numbers.")

def mul():
    try:
        n1 = int(first.get())
        n2 = int(second.get())
        result = n1 * n2
        label4.config(text='Multiplication Result is:'+ str(result))
    except ValueError:
        label4.config(text="You can only enter integer numbers.")

def div():
    try:
        n1 = int(first.get())
        n2 = int(second.get())

        if (n2 != 0):
            result = n1 / n2
            label4.config(text='Division Result is:'+ str(result))
        else:
            label4.config(text='Value of second variable cannot be zero.')
    except ValueError:
        label4.config(text="You can only enter integer numbers.")

mainWindow.mainloop()
