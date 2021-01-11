import tkinter as tk
from tkinter import messagebox
import random

class ChecklistBox(tk.Frame):
    def __init__(self, parent, choices, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.vars = []
        bg = self.cget("background")
        for choice in choices:
            var = tk.StringVar(value=choice)
            self.vars.append(var)
            cb = tk.Checkbutton(self, var=var, text=choice,
                                onvalue=choice, offvalue="",
                                anchor="w", width=20, background=bg,
                                relief="flat", highlightthickness=0
            )
            cb.pack(side="top", fill="x", anchor="w")
            cb.deselect


    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value =  var.get()
            if value:
                values.append(value)
        return values

top = tk.Tk()
nameList = ["Ken", "Hub", "Floor", "Anne", "Arjan", "Daan", 
"Bram", "Ellen Mae", "Emile", "Guy", "Jasmijn", "Julius", 
"Lely", "Raymond", "Rebecca", "Renske", "Sacha", "Sven", "Thijs", "Yumke"]
checklist = ChecklistBox(top, nameList, bd=1, relief="sunken", background="white")
checklist.pack()



def command() :
    tk.messagebox.showinfo(title="De Stand Up wordt gedaan door", message= (random.choice(checklist.getCheckedItems())))

tk.Button(top, text="Kies!", command=command).pack()

top.mainloop()