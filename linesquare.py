from tkinter import *

root = Tk()
root.geometry('+400+300')


def right(self):
    pass


def left(self):
    pass


def forward(self):
    pass


def undo(self):
    pass


canva = Canvas(root, height=200, width=200)
canva.pack()
btnr = Button(root, text='Right')
btnr.pack()
btnl = Button(root, text='Left')
btnl.pack()
btnf = Button(root, text='Forward')
btnf.pack()
btnu = Button(root, text='Undo')
btnu.pack()
length = Entry(root)
length.pack()
per = Label(root, text = 'Perimeter')
per.pack()
sqr = Label(root, text = 'Square')
sqr.pack()

root.mainloop()
