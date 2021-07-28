from tkinter import *
from tkinter import ttk

text= 82
textoben=3
l=len(str(text))*8
if textoben != 2:
    y=5
    x=len(str(textoben))*8
else:
    x = 0
    y = 0
master = Tk()
w = Canvas(master)
w.pack()
points = [5+x, 20+y, 10+x, 15+y, 15+x, 30+y, 20+x, 5+y, 20+x+l, 5+y, 20+x, 5+y, 15+x, 30+y, 10+x, 15+y]
w.create_polygon(points, outline='black', width=3)
w.create_text(21+x, 18+y, text=(str(text)), justify='left', anchor='w')
if textoben != 2:
    w.create_text(15, 12, text=textoben, justify='left', anchor='w')

mainloop()