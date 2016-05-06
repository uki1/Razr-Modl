# -*- coding: utf-8 -*-
import serial
import threading
import time

import csv


from time import gmtime, strftime

Eps ="=A$1"
Sigm ="A$1"

writer = csv.writer(open("some " + strftime("%d %b %H,%M,%S", gmtime()) + ".csv", "wb"),
                    delimiter=';', quoting=csv.QUOTE_MINIMAL, quotechar='`', lineterminator='\n')

writer.writerows([[полимер, длина, ширина, СКОРОСТЬ, температура]])

def saveCSV(r, dl, f):
    ti = strftime("%H:%M:%S", gmtime())
    writer.writerows([["Время", "Сопр, Ом", "Удлин., мм", "Нагр., кгс", "Отн. удл., %", "Напр. Н/мм2"]])
    writer.writerows([[ti, r, dl, f, Eps, Sigm]])
