# -*- coding: utf-8 -*-
from Tkinter import *
import serial
import threading
import time

import csv


from time import gmtime, strftime


root=Tk()

frame1=Frame(root,width=100,heigh=100,bg='#AAAAAA',bd=5)
frame2=Frame(root,width=150,heigh=75,bd=5)
frame3=Frame(root,width=250,heigh=75,bd=5)
frame4=Frame(root,width=250,heigh=75,bd=5)

button1=Button(frame1,text=u'Подключение')#соед со всеми ардуино

se1 = Label(frame2, text="Образец:")
se2 = Entry(frame2)
se3 = Label(frame2, text=u"раст. м/у трав. L:")        
se4 = Entry(frame2)
se5 = Label(frame2, text=u"ширина W:")        
se6 = Entry(frame2)
se7 = Label(frame2, text=u"толщина T:")        
se8 = Entry(frame2)

canv = Canvas(root, width = 800, height = 400, bg = "white")#Рисуем оси графика
canv.create_line(3,400,3,0,width=2,arrow=LAST) 
canv.create_line(0,399,800,399,width=2,arrow=LAST) 

seA = Button(frame3)
seA["text"] = "HOME"
seA["command"] = lambda: serP.write("G28 Z" + '\r\n')


seB1 = Label(frame3, text=u"скорость мм/с:")
seB2 = Entry(frame3)
seB2.insert(1, "50")

seC1 = Label(frame3, text=u"удлинение мм:")
seC2 = Entry(frame3)
seC2.insert(1, "200")

seD = Button(frame3)
seD["text"] = "Старт"
seD["command"] = lambda: serP.write('G1 F%s Z%s \r\n' % (seB2.get(), seC2.get()) )


seB11 = Label(frame4, text=u"скорость мм/с:")
seB21 = Entry(frame4)
seB21.insert(1, "50")

seC10 = Label(frame4, text=u"Нач. удл. мм:")
seC20 = Entry(frame4)
seC20.insert(1, "0")

seC11 = Label(frame4, text=u"Кон. удл. мм:")
seC21 = Entry(frame4)
seC21.insert(1, "200")

seD1 = Button(frame4)
seD1["text"] = "Старт"
seD1["command"] = 'старт потока который делает переодику'

seD12 = Button(frame4)
seD12["text"] = "Стоп"
seD12["command"] = 'стоп потока который делает переодику'

frame1.grid(row = 1, column = 1)
frame2.grid(row = 1, column = 2)
frame3.grid(row = 1, column = 3)
frame4.grid(row = 1, column = 4)

canv.grid(row = 2, column =1, columnspan = 4)

button1.pack()

se1.pack()
se2.pack()
se3.pack()
se4.pack()
se5.pack()
se6.pack()
se7.pack()
se8.pack()

seB1.pack()
seB2.pack()
seC1.pack()
seC2.pack()
seA.pack(side='left')
seD.pack()


seB11.pack()
seB21.pack()
seC10.pack()
seC20.pack()
seC11.pack()
seC21.pack()
seD1.pack(side='left')
seD12.pack()

root.mainloop()
