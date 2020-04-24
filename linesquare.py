from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('+400+300')
root.title('Программка для быстрых подсчетов площадей')
coords = []
sx, sy, x, y = 33, 33, 33, 33
pos = 5
canva = Canvas(root, bg='#b00b69', height=200, width=200)
canva.pack()

entry = Entry(root)
entry.pack()

per = Label(root, text='Perimeter:')
per.pack()
sqr = Label(root, text='Square:')
sqr.pack()

canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
entry.insert(0, 'Введи расстояние')


def right(entry=entry, canva=canva):
    global sx, sy, pos, coords
    s = entry.get()
    if s.isdigit():
        if pos != 1:
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#b00b69', outline='#b00b69')
            l = int(entry.get())
            canva.create_line(sx, sy, sx + l, sy)
            sx = sx + l
            pos = 0
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
            coords.append((sx, sy,))
            print(coords)
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


def left(entry=entry, canva=canva):
    global sx, sy, pos, coords
    s = entry.get()
    if s.isdigit():
        if pos != 0:
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#b00b69', outline='#b00b69')
            l = int(entry.get())
            canva.create_line(sx, sy, sx - l, sy)
            sx = sx - l
            pos = 1
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
            coords.append((sx, sy,))
            print(coords)
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


def up(entry=entry, canva=canva):
    global sx, sy, pos, coords
    s = entry.get()
    if s.isdigit():
        if pos != 3:
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#b00b69', outline='#b00b69')
            l = int(entry.get())
            canva.create_line(sx, sy, sx, sy - l)
            sy = sy - l
            pos = 2
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
            coords.append((sx, sy,))
            print(coords)
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


def down(entry=entry, canva=canva):
    global sx, sy, pos, coords
    s = entry.get()
    if s.isdigit():
        if pos != 2:
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#b00b69', outline='#b00b69')
            l = int(entry.get())
            canva.create_line(sx, sy, sx, sy + l)
            sy = sy + l
            pos = 3
            canva.create_oval(sx - 1.5, sy - 1.5, sx + 1.5, sy + 1.5, fill='#000')
            coords.append((sx, sy,))
            print(coords)
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


def undo():
    pass


"""
https://ru.wikipedia.org/wiki/Формула_площади_Гаусса#Определение
:param coords: [(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)]
:return: area of the polygon
"""


def squarea(coords):
    n = len(coords)
    i = 0
    sum = 0
    while i<n-1:

        x_i = coords[i][0]
        y_i_1 = coords[i + 1][1]
        sum += x_i * y_i_1
        i += 1
    sum += coords[n-1][0] * coords[0][1]
    i = 0
    while i<n-1:
        x_i_1 = coords[i + 1][0]
        y_i = coords[i][1]
        sum -= x_i_1 * y_i
        i += 1
    sum -= coords[0][0] * coords[n-1][1]
    print(abs(sum)/2)

print(
    squarea(
        [
            (2, 1),
            (5, 1),
            (5, 2),
            (6, 2),
            (6, 5),
            (5, 5),
            (5,4),
            (2, 4)
        ]
    )
)

btnr = Button(root, text='Right', command=right)
btnr.pack()
btnup = Button(root, text='Up', command=up)
btnup.pack()
btnl = Button(root, text='Left', command=left)
btnl.pack()
btnd = Button(root, text='Down', command=down)
btnd.pack()
btnu = Button(root, text='Undo', command=undo)
btnu.pack()
btns = Button(root, text='Считай!', command =lambda coords = coords: squarea(coords))
btns.pack()

root.mainloop()
