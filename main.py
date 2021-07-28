import tkinter as tk
import tkinter.font
import tools
from tkinter import ttk


root = tk.Tk()


#defs
def toolsMenu_Wurzeln():
    def wurzeln():
        if E1.get() == '':
            E1.insert(0, '2')
        try:
            L1.configure(text=('Ergebnis:', tools.wurzeln_ziehen(int(E2.get()), int(E1.get()))))
        except:
            L1.configure(text='Ungültige Eingabe!')
    Window_Wurzeln = tk.Toplevel(root)
    wurzel_bild = tk.PhotoImage(file = 'Bilder/wurzel-mathematik.png')
    
    img = tk.Label(Window_Wurzeln, image=wurzel_bild)
    img.image = wurzel_bild
    img.place(x=25, y=25)
    
    E1 = tk.Entry(Window_Wurzeln, width=10)
    E1.place(x=10, y=20)
    
    E2 = tk.Entry(Window_Wurzeln, width=30)
    E2.place(x=110, y=90)
    
    L1 = tk.Label(Window_Wurzeln, text="Ergebnis:")
    L1.place(x=10, y=200)
    
    rechnenButton = tk.Button(Window_Wurzeln, text="Rechnen", command=wurzeln)
    rechnenButton.place(x=320, y=190)
    
    linew = tk.Canvas(Window_Wurzeln, width=400, height=10)
    linew.create_line(5, 5, 400, 5)
    linew.place(x=0, y=230)
     
    schachtelung = tk.Frame(Window_Wurzeln)
    schachtelung.grid(column=0, row=0)
    
    Window_Wurzeln.wm_title("Wurzeln")
    Window_Wurzeln.geometry("410x280")#("410x230")
    Window_Wurzeln.iconphoto(False, icon)

def toolsMenu_Sudoku():
    Window_Sudoku = tk.Toplevel(root)
    sudoku_bild = tk.PhotoImage(file = 'Bilder/sudoku_feld_leer.png')
    
    img = tk.Label(Window_Sudoku, image=sudoku_bild)
    img.image = sudoku_bild
    img.place(x=25, y=25)
    
    Window_Sudoku.wm_title("Sudoku")
    Window_Sudoku.geometry("630x630")
    Window_Sudoku.iconphoto(False, icon)

#widgets

##icon
icon = tk.PhotoImage(file = 'icon/icon.png')

##menu
menu = tk.Menu(root)
root.config(menu=menu)

toolsMenu = tk.Menu(menu)
toolsMenu.add_command(label="Wurzeln", command=toolsMenu_Wurzeln)
toolsMenu.add_command(label="Sudoku", command=toolsMenu_Sudoku)
menu.add_cascade(label="Tools", menu=toolsMenu)

##Gitter
content = tk.Frame(root)

##Willkommen
L1font = tk.font.Font(size=45)
L1 = tk.Label(content, text="Willkommen bei\nMathetools", justify='left', font=L1font)
#L1.place(x=5, y=20)
L2 = tk.Label(content, image=icon)
#L2.place(x=490, y=5)
L3 = tk.Label(content, text='Version 0.1', anchor='sw', justify='left')
#L3.place(x=10, y=155)

##Gittereinordnung
content.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
L1.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
L2.grid(column=1, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
L3.grid(column=0, row=1, sticky=(tk.N, tk.S, tk.E, tk.W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=2)
content.rowconfigure(1, weight=5)

#end
root.iconphoto(False, icon)
root.title("Mathetools")
root.geometry("700x220")
root.mainloop()