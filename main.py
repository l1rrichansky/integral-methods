from math import *
from datetime import datetime
import time
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from design import Ui_MainWindow
from about import Ui_Frame

import numpy as np
import matplotlib.pyplot as plt





def expr(x, f):
    return eval(f)


def check_time(start_time):
    end_time = time.time()
    elapsed_time = end_time - start_time
    start_time_f = datetime.fromtimestamp(start_time)
    end_time_f = datetime.fromtimestamp(end_time)
    return {"elapsed_time": elapsed_time, "start_time": start_time_f, "end_time": end_time_f}


def pr_m(a, b, n, h, express):

    start_time = time.time()

    fx = [a+i*h for i in range(n)]
    fx2 = [expr(i+h/2, express) for i in fx]
    answer = h * sum(fx2)

    time_array = check_time(start_time)

    return {"answer": answer, "elapsed_time": time_array["elapsed_time"], "start_time": time_array["start_time"], "end_time": time_array["end_time"]}


def trap_m(a, b, n, h, express):
    start_time = time.time()

    fx = [a + i * h for i in range(n+1)]
    fx2 = [expr(i, express) for i in fx]

    ans = fx2[1:-1]
    ans.append((fx2[0]+fx2[-1])/2)

    answer = h * sum(ans)

    time_array = check_time(start_time)

    return {"answer": answer, "elapsed_time": time_array["elapsed_time"], "start_time": time_array["start_time"],
            "end_time": time_array["end_time"]}


def simpson_m(a, b, n, h, express):
    start_time = time.time()

    fx = [a + i * h for i in range(n+1)]
    fx2 = [expr(i, express) for i in fx]

    arr = [fx2[0], fx2[-1],
           *[i*4 for c, i in enumerate(fx2[1:-1]) if c % 2 == 0],
           *[i*2 for c, i in enumerate(fx2[1:-1]) if c % 2 != 0]]

    answer = (h/3)*sum(arr)

    time_array = check_time(start_time)

    return {"answer": answer, "elapsed_time": time_array["elapsed_time"], "start_time": time_array["start_time"],
            "end_time": time_array["end_time"]}


def get_graph(a, b, f):

    #print(x)
    x = np.linspace(a, b, 50)
    Y = eval(f)
    #print('loh' + str(Y) + str(Y[-1]))
    plt.plot(x, Y)
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.fill_between(x, Y, np.zeros_like(Y), color='yellowgreen')
    plt.xlim(-abs(max(Y)+10), abs(max(Y)+10))
    plt.ylim(-abs(max(Y)+10), abs(max(Y)+10))
    plt.show()


class About(QMainWindow):
    def __init__(self):
        super(About, self).__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)


class Integral(QMainWindow):
    def __init__(self):
        super(Integral, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.exec)
        self.ui.action_2.triggered.connect(self.about)
        self.ui.action_3.triggered.connect(self.exit)
        self.ui.action.triggered.connect(self.show_graph)

    def exit(self):
        window.close()

    def about(self):
        about_window.show()


    def exec(self):
        try:
            a = int(self.ui.lineEdit_2.text())
            b = int(self.ui.lineEdit_3.text())
            n = int(self.ui.lineEdit_4.text())
            expression = str(self.ui.lineEdit.text())
            h = (b - a) / n
            if self.ui.radioButton.isChecked():
                s = pr_m(a, b, n, h, expression)
            elif self.ui.radioButton_2.isChecked():
                s = trap_m(a, b, n, h, expression)
            elif self.ui.radioButton_3.isChecked():
                s = simpson_m(a, b, n, h, expression)
            text_answer = f' Ответ: {s["answer"]} \n Время старта: {s["start_time"]} \n Время окончания: {s["end_time"]} \n Затраченное время: {s["elapsed_time"]}'
            self.ui.textBrowser.clear()
        except Exception:
            text_answer = 'Ошибка: Некорректные данные.'
        self.ui.textBrowser.append(text_answer)

    def show_graph(self):
        try:
            a = int(self.ui.lineEdit_2.text())
            b = int(self.ui.lineEdit_3.text())
            f = str(self.ui.lineEdit.text())
            get_graph(a, b, f)
        except Exception:
            text_answer = 'Ошибка: Некорректные данные.'
            self.ui.textBrowser.append(text_answer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Integral()
    about_window = About()
    window.show()
    sys.exit(app.exec())
