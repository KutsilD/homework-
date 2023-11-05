#підключення бібліотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint 

app = QApplication([])#створеня програми
win = QWidget()#створеня вікна
win.setWindowTitle("Визначник переможця")# надавання назви програмі
win.resize(700, 500)# розміри вікна програми
win.move(500, 150)# розміщення вікна програми

text1 = QLabel("Натисни, щоб дізнатися переможця")#-
text2 = QLabel("?")                               # }- 
gener = QPushButton("Згенерувати")                #- 

line = QVBoxLayout()#
line.addWidget(text1, alignment = Qt.AlignCenter)#додавання text1 на екран програми
line.addWidget(text2, alignment = Qt.AlignCenter)#додавання text2 на екран програми
line.addWidget(gener, alignment = Qt.AlignCenter)#додавання кнопки "Згенерувати" на головн й екран

win.setLayout(line)#

def funk():
    num = randint(1, 100)
    text1.setText("Переможець")
    text2.setText(str(num))

gener.clicked.connect(funk)# викликання функції

win.show()#відкриття вікна програми
app.exec_()#закриття програми
