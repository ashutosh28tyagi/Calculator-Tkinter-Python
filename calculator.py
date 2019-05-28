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
    n1 = int(first.get())
    n2 = int(second.get())
    n3 = n1+n2
    label4.config(text='Sum: ' + str(n3))

def sub():
    n1 = int(first.get())
    n2 = int(second.get())
    n3 = n1 - n2
    label4.config(text='Subtraction: ' + str(n3))

def mul():
    n1 = int(first.get())
    n2 = int(second.get())
    n3 = n1 * n2
    label4.config(text='Multiplication: ' + str(n3))

def div():
    n1 = int(first.get())
    n2 = int(second.get())
    n3 = n1 / n2
    label4.config(text='Division: ' + str(n3))

mainWindow.mainloop()