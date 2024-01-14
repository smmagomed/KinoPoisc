import webbrowser

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)

def get_jon_vik1():
    webbrowser.open('https://www.kinopoisk.ru/film/762738/')

def get_jon_vik2():
    webbrowser.open('https://www.kinopoisk.ru/film/885658/')

def get_jon_vik3():
    webbrowser.open('https://www.kinopoisk.ru/film/1009536/')

def get_jon_vik4():
    webbrowser.open('https://www.kinopoisk.ru/film/1267348/')

def get_matrica_1():
    webbrowser.open('https://www.kinopoisk.ru/film/301/')

def get_matrica_2():
    webbrowser.open('https://www.kinopoisk.ru/film/299/')

def get_matrica_3():
    webbrowser.open('https://www.kinopoisk.ru/film/316/')

def get_matrica_4():
    webbrowser.open('https://www.kinopoisk.ru/film/1294123/')

app = QApplication([])
window = QWidget()
window.setWindowTitle('Кинопоиск')
window.resize(400,400)

main_lain = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

text = QLabel('Выберете фильм:')
button1 =QPushButton('Джон уик1 ')
button2 =QPushButton('Джон уик2')
button3 =QPushButton('Джон уик3')
button4 =QPushButton('Джон уик4')
button5 =QPushButton('Матрица')
button6 =QPushButton('Матрица_2')
button7 =QPushButton('Матрица_3')
button8 =QPushButton('Матрица_4')

button1.clicked.connect(get_jon_vik1)
button2.clicked.connect(get_jon_vik2)
button3.clicked.connect(get_jon_vik3)
button4.clicked.connect(get_jon_vik4)
button5.clicked.connect(get_matrica_1)
button6.clicked.connect(get_matrica_2)
button7.clicked.connect(get_matrica_3)
button8.clicked.connect(get_matrica_4)


line1.addWidget(button1, alignment=Qt.AlignCenter)
line1.addWidget(button2, alignment=Qt.AlignCenter)
line1.addWidget(button3, alignment=Qt.AlignCenter)
line1.addWidget(button4, alignment=Qt.AlignCenter)
line2.addWidget(button5, alignment=Qt.AlignCenter)
line2.addWidget(button6, alignment=Qt.AlignCenter)
line2.addWidget(button7, alignment=Qt.AlignCenter)
line2.addWidget(button8, alignment=Qt.AlignCenter)
main_lain.addWidget(text, alignment=Qt.AlignCenter)

window.setStyleSheet('font-size:25px; font-style:italic; background-color:rgb(150,0,0)')
button1.setStyleSheet('background-color:rgb(255,40,0); color:rgb(255,255,255)')
button2.setStyleSheet('background-color:rgb(255,40,0); color:rgb(255,255,255)')
button3.setStyleSheet('background-color:rgb(255,40,0); color:rgb(255,255,255)')
button4.setStyleSheet('background-color:rgb(255,40,0); color:rgb(255,255,255)')
button5.setStyleSheet('background-color:rgb(255,40,0); color:rgb(255,255,255)')
button6.setStyleSheet('background-color:rgb(255,40,0); color:rgb(255,255,255)')
button7.setStyleSheet('background-color:rgb(255,40,0); color:rgb(255,255,255)')
button8.setStyleSheet('background-color:rgb(255,40,0); color:rgb(255,255,255)')
text.setStyleSheet('border: 5px dashed white')
main_lain.addLayout(line1)
main_lain.addLayout(line2)

window.setLayout(main_lain)
window.show()
app.exec()
