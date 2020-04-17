from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('+400+300')
root.title('Программка для быстрых подсчетов площадей')

sx, sy = 33, 33
pos = 5
canva = Canvas(root, bg='#b00b69', height=200, width=200)
canva.pack()

entry = Entry(root)
entry.pack()

per = Label(root, text='Perimeter:')
per.pack()
sqr = Label(root, text='Square:')
sqr.pack()

canva.create_oval(sx-1.5, sy-1.5, sx + 1.5, sy + 1.5, fill='#000')
entry.insert(0, 'Введи расстояние')


def right(entry=entry, canva=canva):
    global sx, sy, pos
    s = entry.get()
    if s.isdigit():
        if pos != 1:
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#b00b69',outline='#b00b69')
            l = int(entry.get()) * 2
            canva.create_line(sx, sy, sx + l, sy)
            sx = sx + l
            pos = 0
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


def left(entry=entry, canva=canva):
    global sx, sy, pos
    s = entry.get()
    if s.isdigit():
        if pos != 0:
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#b00b69', outline='#b00b69')
            l = int(entry.get()) * 2
            canva.create_line(sx, sy, sx - l, sy)
            sx = sx - l
            pos = 1
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")

def up(entry=entry, canva=canva):
    global sx, sy, pos
    s = entry.get()
    if s.isdigit():
        if pos != 3:
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#b00b69', outline='#b00b69')
            l = int(entry.get()) * 2
            canva.create_line(sx, sy, sx, sy - l)
            sy = sy - l
            pos = 2
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")

def down(entry=entry, canva=canva):
    global sx, sy, pos
    s = entry.get()
    if s.isdigit():
        if pos != 2:
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#b00b69', outline='#b00b69')
            l = int(entry.get()) * 2
            canva.create_line(sx, sy, sx, sy + l)
            sy = sy + l
            pos = 3
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")

def undo():
    pass


btnr = Button(root, text='Right', command=right)
btnr.pack()
btnl = Button(root, text='Left', command=left)
btnl.pack()
btnup = Button(root, text='Up', command=up)
btnup.pack()
btnd = Button(root, text='Down', command=down)
btnd.pack()
btnu = Button(root, text='Undo', command=undo)
btnu.pack()

root.mainloop()
