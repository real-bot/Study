from tkinter import *
from tkinter import messagebox
import turtle

root = Tk()
root.geometry('+400+300')
root.title('Программка для быстрых подсчетов площадей')
coords = []
perim, sx, sy = 0, 0, 0
pos = 5

entry = Entry(root)
entry.pack()

per = Label(root, text='Perimeter:')
per.pack()
sqr = Label(root, text='Square:')
sqr.pack()

entry.insert(0, 'Введи расстояние')

btns = Button(root, text='Считай!', command=lambda coords=coords: squarea(coords))
btns.pack()


def right(entry=entry):
    global sx, sy, pos, coords, perim
    s = entry.get()
    if s.isdigit():
        if pos != 1:
            l = int(entry.get())
            sx = sx + l/2
            t.goto(sx, sy)
            pos = 0
            t.write(l, align = 'center')
            sx = sx + l / 2
            t.goto(sx, sy)
            perim += l
            coords.append((sx, sy,))
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


def left(entry=entry):
    global sx, sy, pos, coords, perim
    s = entry.get()
    if s.isdigit():
        if pos != 0:
            l = int(entry.get())
            sx = sx - l/2
            t.goto(sx, sy)
            pos = 1
            t.write(l, align = 'center')
            sx = sx - l / 2
            t.goto(sx, sy)
            perim += l
            coords.append((sx, sy,))
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


def up(entry=entry):
    global sx, sy, pos, coords, perim
    s = entry.get()
    if s.isdigit():
        if pos != 3:
            l = int(entry.get())
            sy = sy + l/2
            t.goto(sx, sy)
            pos = 2
            t.write(l, align = 'center')
            sy = sy + l/2
            t.goto(sx, sy)
            perim += l
            coords.append((sx, sy,))
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


def down(entry=entry):
    global sx, sy, pos, coords, perim
    s = entry.get()
    if s.isdigit():
        if pos != 2:
            l = int(entry.get())
            sy = sy - l/2
            t.goto(sx, sy)
            pos = 3
            t.write(l, align = 'center')
            sy = sy - l/2
            t.goto(sx, sy)
            perim += l
            coords.append((sx, sy,))
        else:
            messagebox.showinfo('Опасно', "Не туда воюешь")


"""
https://ru.wikipedia.org/wiki/Формула_площади_Гаусса#Определение
:param coords: [(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)]
:return: area of the polygon
"""


def squarea(coords):
    n = len(coords)
    i = 0
    sum = 0
    while i < n - 1:
        x_i = coords[i][0]
        y_i_1 = coords[i + 1][1]
        sum += x_i * y_i_1
        i += 1
    sum += coords[n - 1][0] * coords[0][1]
    i = 0
    while i < n - 1:
        x_i_1 = coords[i + 1][0]
        y_i = coords[i][1]
        sum -= x_i_1 * y_i
        i += 1
    sum -= coords[0][0] * coords[n - 1][1]
    sqr['text'] = 'Square:' + str((abs(sum) / 2))
    per['text'] = 'Perimeter:' + str(perim)
    print(abs(sum) / 2)


canvas = Canvas(root, width=500, height=500)
canvas.pack()

t = turtle.RawTurtle(canvas)
t.pencolor("#ff0000")
t.pendown()

Button(root, text="Up", command=up).pack(side=LEFT)
Button(root, text="Down", command=down).pack(side=LEFT)
Button(root, text="Left", command=left).pack(side=LEFT)
Button(root, text="Right", command=right).pack(side=LEFT)

root.mainloop()
