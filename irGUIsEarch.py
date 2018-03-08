from Tkinter import *
from math import *
def evaluate(event):
    print entry.get()
    #res.configure(text = "Ergebnis: " + str(eval(entry.get())))
w = Tk()
Label(w, text="Your Expression:").pack()
entry = Entry(w)
print entry.get()
#entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()

w.mainloop()