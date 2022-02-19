#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Самый популярный спорт мира')
main_win.resize(400, 200)


RadioGroupBox = QGroupBox('Варианты')
rbtn_1 = QRadioButton('Фудбол')
rbtn_1 = QRadioButton('Волейбол')
rbtn_1 = QRadioButton('тенис')
rbtn_1 = QRadioButton('баскетбол')
layout_ans1 = QHBoxLayout()
layout_ans1 = QHVBoxLayout()
layout_ans1 = QVBoxLayout()
layout_ans2.addWiget(rbtn_1)
layout_ans2.addWiget(rbtn_2)
layout_ans2.addWiget(rbtn_3)
layout_ans2.addWiget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans2)
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)


 
btn_answer3.clicked.connect(show_win)
btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)
 
main_win.show()
app.exec_()

