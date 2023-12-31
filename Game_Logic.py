from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
winner_list = [0,1,2,3,4,5,6,7,8,9]
turn_list = [1]
import sqlite3 as sql
conn = sql.connect("Name.db")
cur = conn.cursor()
def on_window_close_event(event):
    cur.execute("DELETE FROM Player_Name;")
    conn.commit()
    conn.close()
class Ui_Form(object):
    Reset = 0
    def check_status(self):
        # """
        # The function `check_status` checks the status of the tic-tac-toe game and determines if there is
        # a winner or a draw.
        # """
        buttons = [self.one, self.two, self.three, self.four,self.five, self.six, self.seven, self.eight,self.nine]
        if (winner_list[1] == "X" and winner_list[2] == "X" and winner_list[3] == "X") or (winner_list[4]=="X" and winner_list[5] == "X" and winner_list[6] == "X") or (winner_list[7] == "X" and winner_list[8] == "X" and winner_list[9] == "X") or (winner_list[1] == "X" and winner_list[4] == "X" and winner_list[7] == "X") or (winner_list[2] == "X" and winner_list[5] == "X" and winner_list[8] == "X") or (winner_list[3] == "X" and winner_list[6] == "X" and winner_list[9] == "X") or (winner_list[1] == "X" and winner_list[5] == "X" and winner_list[9] == "X") or (winner_list[3] == "X" and winner_list[5] == "X" and winner_list[7] == "X"):
            self.Reset = 1
            cur.execute("SELECT * FROM Player_Name;")
            record = cur.fetchone()
            name = record[0]
            self.label_2.setText(name+" won the game")
            for i in buttons:
                i.setEnabled(False)
            def change_button_text():
                self.nine.setEnabled(True)
                self.nine.setText("RESTART")
                self.nine.setStyleSheet("font-size: 30px; color: RED; background-color: rgb(217, 252, 231);")
            QTimer.singleShot(3000, change_button_text)

        elif (winner_list[1] == "0" and winner_list[2] == "0" and winner_list[3] == "0") or (winner_list[4]=="0" and winner_list[5] == "0" and winner_list[6] == "0") or (winner_list[7] == "0" and winner_list[8] == "0" and winner_list[9] == "0") or (winner_list[1] == "0" and winner_list[4] == "0" and winner_list[7] == "0") or (winner_list[2] == "0" and winner_list[5] == "0" and winner_list[8] == "0") or (winner_list[3] == "0" and winner_list[6] == "0" and winner_list[9] == "0") or (winner_list[1] == "0" and winner_list[5] == "0" and winner_list[9] == "0") or (winner_list[3] == "0" and winner_list[5] == "0" and winner_list[7] == "0"):
            self.Reset = 1
            cur.execute("SELECT * FROM Player_Name;")
            record = cur.fetchone()
            name = record[1]
            self.label_2.setText(name+" won the game")
            for i in buttons:
                i.setEnabled(False)
            def change_button_text():
                self.nine.setEnabled(True)
                self.nine.setText("RESTART")
                self.nine.setStyleSheet("font-size: 30px; color: RED; background-color: rgb(217, 252, 231);")
            QTimer.singleShot(3000, change_button_text)
        else:
            if (self.one.isEnabled() == False) and (self.two.isEnabled() == False) and (self.three.isEnabled() == False) and (self.four.isEnabled() == False) and (self.five.isEnabled() == False) and (self.six.isEnabled() == False) and (self.seven.isEnabled() == False) and (self.eight.isEnabled() == False) and (self.nine.isEnabled() == False): 
                self.Reset = 1
                self.label_2.setText("Drawn!")  
                for i in buttons:
                    i.setEnabled(False)
                def change_button_text():
                    self.nine.setEnabled(True)
                    self.nine.setText("RESTART")
                    self.nine.setStyleSheet("font-size: 30px; color: RED; background-color: rgb(217, 252, 231);")
                QTimer.singleShot(3000, change_button_text)

    def one_clicked(self):
        # """
        # The function `one_clicked` updates the text and style of a button, based on the current turn, and
        # checks the game status.
        # """
        self.one.setEnabled(False)
        if turn_list[0] == 1:
            self.one.setText("X")
            winner_list[1] = "X"
            turn_list[0] = 0
            self.one.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
            self.check_status()
        else:
            self.one.setText("0")
            winner_list[1] = "0"
            turn_list[0] = 1
            self.one.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
            self.check_status()
    def two_clicked(self):
        self.two.setEnabled(False)
        if turn_list[0] == 1:
            self.two.setText("X")
            winner_list[2] = "X"
            turn_list[0] = 0
            self.two.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
            self.check_status()
        else:
            self.two.setText("0")
            winner_list[2] = "0"
            turn_list[0] = 1
            self.two.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
            self.check_status()
    def three_clicked(self):
        self.three.setEnabled(False)
        if turn_list[0] == 1:
            self.three.setText("X")
            winner_list[3] = "X"
            turn_list[0] = 0
            self.three.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
            self.check_status()
        else:
            self.three.setText("0")
            winner_list[3] = "0"
            turn_list[0] = 1
            self.three.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
            self.check_status()
    def four_clicked(self):
        self.four.setEnabled(False)
        if turn_list[0] == 1:
            self.four.setText("X")
            winner_list[4] = "X"
            turn_list[0] = 0
            self.four.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
            self.check_status()
        else:
            self.four.setText("0")
            winner_list[4] = "0"
            turn_list[0] = 1
            self.four.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
            self.check_status()
    def five_clicked(self):
        self.five.setEnabled(False)
        if turn_list[0] == 1:
            self.five.setText("X")
            winner_list[5] = "X"
            turn_list[0] = 0
            self.five.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
            self.check_status()
        else:
            self.five.setText("0")
            winner_list[5] = "0"
            turn_list[0] = 1
            self.five.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
            self.check_status()
    def six_clicked(self):
        self.six.setEnabled(False)
        if turn_list[0] == 1:
            self.six.setText("X")
            winner_list[6] = "X"
            turn_list[0] = 0
            self.six.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
            self.check_status()
        else:
            self.six.setText("0")
            winner_list[6] = "0"
            turn_list[0] = 1
            self.six.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
            self.check_status()
    def seven_clicked(self):
        self.seven.setEnabled(False)
        if turn_list[0] == 1:
            self.seven.setText("X")
            winner_list[7] = "X"
            turn_list[0] = 0
            self.seven.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
            self.check_status()
        else:
            self.seven.setText("0")
            winner_list[7] = "0"
            turn_list[0] = 1
            self.seven.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
            self.check_status()
    def eight_clicked(self):
        self.eight.setEnabled(False)
        if turn_list[0] == 1:
            self.eight.setText("X")
            winner_list[8] = "X"
            turn_list[0] = 0
            self.eight.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
            self.check_status()
        else:
            self.eight.setText("0")
            winner_list[8] = "0"
            turn_list[0] = 1
            self.eight.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
            self.check_status()
    def nine_clicked(self):
        if self.Reset == 1:
            button = [self.one, self.two, self.three, self.four,self.five, self.six, self.seven, self.eight,self.nine]
            for i in button:
                i.setEnabled(True)
                i.setText("")
            self.Reset = 0
            turn_list[0] = 1
            winner_list.clear() 
            for i in range(0,10):
                winner_list.append(i)
            self.label_2.setText("")
        else:
            self.nine.setEnabled(False)
            if turn_list[0] == 1:
                self.nine.setText("X")
                winner_list[9] = "X"
                turn_list[0] = 0
                self.nine.setStyleSheet("font-size: 30px; color: blue; background-color: rgb(217, 252, 231);")
                self.check_status()
            else:
                self.nine.setText("0")
                winner_list[9] = "0"
                turn_list[0] = 1
                self.nine.setStyleSheet("font-size: 30px; color: green; background-color: rgb(217, 252, 231);")
                self.check_status()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 436)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        Form.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setMinimumSize(QtCore.QSize(0, 0))
        self.label_1.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_1.setBaseSize(QtCore.QSize(0, 0))
        self.label_1.setStyleSheet("color:rgb(66, 3, 115);")
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_1.setFont(font)
        self.label_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_1.setMouseTracking(False)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setWordWrap(False)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.one = QtWidgets.QPushButton(Form)
        self.one.setMinimumSize(QtCore.QSize(0, 100))
        self.one.setText("")
        self.one.setObjectName("one")
        self.one.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout.addWidget(self.one)
        self.four = QtWidgets.QPushButton(Form)
        self.four.setMinimumSize(QtCore.QSize(0, 100))
        self.four.setText("")
        self.four.setObjectName("four")
        self.four.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout.addWidget(self.four)
        self.seven = QtWidgets.QPushButton(Form)
        self.seven.setMinimumSize(QtCore.QSize(0, 100))
        self.seven.setText("")
        self.seven.setObjectName("seven")
        self.seven.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout.addWidget(self.seven)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.two = QtWidgets.QPushButton(Form)
        self.two.setMinimumSize(QtCore.QSize(0, 100))
        self.two.setText("")
        self.two.setObjectName("two")
        self.two.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout_2.addWidget(self.two)
        self.five = QtWidgets.QPushButton(Form)
        self.five.setMinimumSize(QtCore.QSize(0, 100))
        self.five.setText("")
        self.five.setObjectName("five")
        self.five.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout_2.addWidget(self.five)
        self.eight = QtWidgets.QPushButton(Form)
        self.eight.setMinimumSize(QtCore.QSize(0, 100))
        self.eight.setText("")
        self.eight.setObjectName("eight")
        self.eight.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout_2.addWidget(self.eight)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.three = QtWidgets.QPushButton(Form)
        self.three.setMinimumSize(QtCore.QSize(0, 100))
        self.three.setText("")
        self.three.setObjectName("three")
        self.three.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout_3.addWidget(self.three)
        self.six = QtWidgets.QPushButton(Form)
        self.six.setMinimumSize(QtCore.QSize(0, 100))
        self.six.setText("")
        self.six.setObjectName("six")
        self.six.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout_3.addWidget(self.six)
        self.nine = QtWidgets.QPushButton(Form)
        self.nine.setMinimumSize(QtCore.QSize(0, 100))
        self.nine.setText("")
        self.nine.setObjectName("nine")
        self.nine.setStyleSheet("background-color: rgb(217, 252, 231);")
        self.verticalLayout_3.addWidget(self.nine)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 2, 1, 1)

        self.one.clicked.connect(self.one_clicked)
        self.two.clicked.connect(self.two_clicked)
        self.three.clicked.connect(self.three_clicked)
        self.four.clicked.connect(self.four_clicked)
        self.five.clicked.connect(self.five_clicked)
        self.six.clicked.connect(self.six_clicked)
        self.seven.clicked.connect(self.seven_clicked)
        self.eight.clicked.connect(self.eight_clicked)
        self.nine.clicked.connect(self.nine_clicked)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tic_Tac_Toe"))
        self.label_1.setText(_translate("Form", "TIC TAC TOE "))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.setStyleSheet("background-color: rgb(255, 242, 247);")
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Form.closeEvent = on_window_close_event
    sys.exit(app.exec_())