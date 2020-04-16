from tkinter import *

root = Tk()
root.geometry('+400+300')
root.title('Мой второй калькулятор')
root.resizable(False, False)
root.config(bg='#000')

buttonsplace = [
    '1', '2', '3', '+',
    '4', '5', '6', '-',
    '7', '8', '9', '*',
    '0', '(', ')', '/',
    '.'

]
buttonsact = ['C', 'DEL', '=']


class MyButton:

    def buttonnumberplace(self, root, number, label, column, row):
        self.number = number
        self.root = root
        self.btn = Button(root, text=number, width=3, height=2,
                          command=lambda label=label, number=number: self.numberplace(label, number))
        self.btn.grid(row=row, column=column, sticky=NW)

    def numberplace(self, label, number):
        label['text'] += number

    def buttonactionplace(self, root, action, label, column, row, entry):
        self.action = action
        self.root = root
        self.bn = Button(root, text=action, width=3, height=2,
                         command=lambda label = label, action = action,entry=entry: self.actdoing(label, action, entry))
        self.bn.grid(row=row, column=column, sticky=NW)

    def actdoing(self, entry, label, action):
        if action == 'C':
            label['text'] = ''
            entry
        elif action == 'DEL':
            label['text'] = label['text'][0:-1]
        elif action == '=':
            if '=' in label['text']:
                label['text'] = ''
            else:
                label['text'] += '=' + str(eval(label['text']))


linput = Label(root, width=10)
linput['text'] = ''
linput.grid(row=0, column=0, columnspan=4, sticky=W + E)
entry = Entry(root)

i = 0
buttons = MyButton()
row = 0
column = 1
for i in buttonsplace:
    buttons.buttonnumberplace(root, i, linput, row, column)
    row += 1
    if row == 4:
        row = 0
        column += 1
for i in buttonsact:
    buttons.buttonactionplace(root, i, linput, row, column,entry)
    row += 1
    if row == 4:
        row = 0
        column += 1

root.mainloop()
