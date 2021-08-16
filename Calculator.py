from Tkinter import *
import Tkinter as tk
class Rechner():

    def __init__(self):
        self.parameter = 0
        self.operator = ""
        self.parameter2 = 0

    def add(self):
        self.operator = "+"
        if self.parameter:
            self.parameter2 = str(int(self.parameter) + int(rechnung.get()))
            result.set(self.parameter2)
            self.parameter = self.parameter2
        else:
            self.parameter = rechnung.get()
        rechnung.delete(0, len(rechnung.get()))

    def sub(self):
        self.operator = "-"
        if self.parameter:
            self.parameter2 = str(int(self.parameter) - int(rechnung.get()))
            result.set(self.parameter2)
            self.parameter = self.parameter2
        else:
            self.parameter = rechnung.get()
        rechnung.delete(0, len(rechnung.get()))

    def div(self):
        self.operator = "/"
        if self.parameter:
            self.parameter2 = str(int(self.parameter) / int(rechnung.get()))
            result.set(self.parameter2)
            self.parameter = self.parameter2
        else:
            self.parameter = rechnung.get()
        rechnung.delete(0, len(rechnung.get()))

    def mtpl(self):
        self.operator = "*"
        if self.parameter:
            self.parameter2 = str(int(self.parameter) * int(rechnung.get()))
            result.set(self.parameter2)
            self.parameter = self.parameter2
        else:
            self.parameter = rechnung.get()
        rechnung.delete(0, len(rechnung.get()))

    def equals(self):
        if self.operator == "+":
            result.set(str(int(self.parameter) + int(rechnung.get())))
            rechnerObj.__init__
        elif self.operator == "-":
            result.set(str(int(self.parameter) - int(rechnung.get())))
            rechnerObj.__init__
        elif self.operator == "/":
            result.set(str(int(self.parameter) / int(rechnung.get())))
            rechnerObj.__init__
        elif self.operator == "*":
            result.set(str(int(self.parameter) * int(rechnung.get())))
            rechnerObj.__init__

    def delete(self):
        self.parameter = None
        result.set("")
        rechnung.delete(0, len(rechnung.get()))
        rechnerObj.__init__

rechnerObj = Rechner()
rechnerObj.__init__
root = Tk()
root.title("Calculator")
result = tk.StringVar()
root.geometry("350x100")
rechnung = Entry(root)
rechnung.grid(row=0, column=0, columnspan=18)
output_result = Label(root, text="Ergebnis:").grid(row=1, column=0, columnspan=6)
output_result = Label(root, textvariable=result, activebackground="#000000").grid(row=1, column=6, columnspan=6)
button_plus = Button(root, text=" + ", bg="#D2DBFF", activebackground="#D5DCFC", command=rechnerObj.add)
button_plus.grid(row=2, column=0, columnspan=3)
button_minus = Button(root, text="  -  ", bg="#D2DBFF", activebackground="#D5DCFC", command=rechnerObj.sub)
button_minus.grid(row=2, column=3, columnspan=3)
button_geteilt = Button(root, text="  /  ", bg="#D2DBFF", activebackground="#D5DCFC", command=rechnerObj.div)
button_geteilt.grid(row=2, column=6, columnspan=3)
button_mal = Button(root, text="  *  ", bg="#D2DBFF", activebackground="#D5DCFC", command=rechnerObj.mtpl)
button_mal.grid(row=2, column=9, columnspan=3)
button_eq = Button(root, text="  =  ", bg="#D2DBFF", activebackground="#D5DCFC", command=rechnerObj.equals)
button_eq.grid(row=2, column=12, columnspan=3)
button_del = Button(root, text=" del ", bg="#D2DBFF", activebackground="#D5DCFC", command=rechnerObj.delete)
button_del.grid(row=2, column=15, columnspan=3)

root.mainloop()