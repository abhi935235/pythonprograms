from tkinter import *

import table as table
from docx import Document
import matplotlib.pyplot as plt
import numpy as np
import statistics
from operator import itemgetter
import statistics

root = Tk()
root.title("GUI")
root.geometry("1000x600+600+500")
root.resizable(height=False, width=False)
x = 0
n = 0
total = []
total1 = []
global flag
global cut_2d

cut_2d = []

sample = 1


# global no_of_entries = 0


def avg():
    tot_sum = 0
    for i in total:
        tot_sum += i
    avg = tot_sum / len(total)
    print(avg)
    text = Text(root)
    text.insert(END, avg)
    text.pack()


def make():
    global s
    s = int(ent6.get())
    new1()


def new1():
    global ent1
    global ent2
    global ent3
    global ent4
    global ent5
    global ent6
    global cut_1d
    global c_and_acc
    c_and_acc = []
    cut_1d = []
    ent1 = []

    global number1
    number1 = StringVar()

    for i in range(s):
        lb1 = Label(root, text=f'cut{i + 1}')
        temp_ent1 = Entry(root)
        ent1.append(temp_ent1)
        lb1.pack()
        temp_ent1.pack()
        # value.append(ent1)
        # mydict = dict(enumerate(map(itemgetter("ent1"), iterload(f)), start=1))
    lb3 = Label(root, text="Each Cartridge Mean Payload Weight (g)")
    ent3 = Entry(root, textvariable=number1)
    lb3.pack()
    ent3.pack()
    lb4 = Label(root, text="Container & Accessories")
    ent4 = Entry(root)
    lb4.pack()
    ent4.pack()
    lb5 = Label(root, text="Assembled Cartridge Weight (g)")
    ent5 = Entry(root)
    lb5.pack()
    ent5.pack()
    btn = Button(root, text="add", command=show)
    btn.pack()


def show():
    # no_of_entries +=1
    global sample

    for i in range(s):
        cut_1d.append(int(ent1[i].get()))
    cut_2d.append(cut_1d)
    print(cut_2d)
    c_and_acc.append(ent4.get())
    calc()
    ent3.insert(0, calc())
    new1()


def calc():
    print(statistics.mean((cut_2d[0])))



#    ent3.insert(0, str(float(sum(value.get())) / i))

# ent3.insert(0, str(int(statistics.mean(value))))


# ent3.insert(0, str(int(ent2.get()) / int(ent3.get())))
# row = table.add_row()
## total.append(int(ent1.get()))
# otal.append(int(ent2.get()))
# total1.append(int(ent3.get()))
# cell = table.rows[len(total)].cells
# cell[0].text = str(sample)
# cell[1].text = ent1.get()
# cell[1].text = ent2.get()
# cell[2].text = ent3.get()
# cell[3].text = str(int(ent2.get()) / int(ent3.get()))
# print(total)
# print(total1)
# sample += 1
# new()
# new1()


def quit():
    doc.save("mod2.docx")
    root.destroy()


def graph():
    global total1
    global total
    doc.save("mod2.docx")
    ndoc = Document('mod2.docx')
    table = ndoc.tables[0]

    sample_n = []
    data = []

    i = 0
    for row in table.rows:
        for cell in row.cells:
            print(cell.text)
            if i == 0:
                i += 1
                continue
            elif i % 4 == 0:
                sample_n.append(int(cell.text))
                i += 1
            elif i % 7 == 0:
                data.append(int(cell.text))
                i += 1

    print(len(sample_n))
    print(len(data))

    graphvar = []
    if len(sample_n) == 0:
        for i in range(len(total)):
            graphvar.append((i + 1, total[i] / total1[i]))
        ind = []
        value = []
        for index, val in graphvar:
            ind.append(index)
            value.append(val)
        plt.plot(ind, value)
        plt.xlabel(['sample'])
        plt.ylabel(['linear resistance'])
        plt.show()
    else:
        plt.plot(sample_n, data)
        plt.xlabel(['sample'])
        plt.ylabel(['linear resistance'])
        plt.show()
    print(graphvar)


doc = Document()
doc.add_heading("Measurement data of input wire electrical resistance", 0)
table = doc.add_table(rows=1, cols=4)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = "Sample number"
hdr_cells[1].text = "Each Cartridge Mean Payload Weight (g)"
hdr_cells[2].text = "Container & Accessories"
hdr_cells[3].text = "Assembled Cartridge Weight (g)"

if x == 0:
    lb6 = Label(root, text="no of cuts:")
    ent6 = Entry(root)
    lb6.pack()
    ent6.pack()
    btn6 = Button(root, text="enter", command=make)
    btn6.pack()
    x += 1

# btn1 = Button(root,text="add Data",command=make)
# btn1.pack()
# btn6 = Button(root,text="add Resistance",command=new1)
# btn6.pack()
btn4 = Button(root, text="show graph", command=graph)
btn4.pack()
btn3 = Button(root, text="quit", command=quit)
btn3.pack()
root.mainloop()
