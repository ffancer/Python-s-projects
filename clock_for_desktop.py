"""
I needed a clock that would show the time at the top of all the windows. The watch should be in the middle of the top.
If you played Grim Dawn you know about what I want

Мне нужны часы, которые будут висеть поверх всех окон, в центре и наверху. Как в игре Grim Dawn, если вы в курсе :)
"""
from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.eval('tk::PlaceWindow . center')
root.title('Clock')


def time():
    string = strftime('%H:%M:%S')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 40, 'bold'),
            background='purple',
            foreground='white')

lbl.pack(anchor='n')
time()

mainloop()