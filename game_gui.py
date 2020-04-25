from PyQt5 import QtTest
from PyQt5.QtGui import QPixmap
import time,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt
import sys, socket, time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.yacine = QtWidgets.QLabel(self.centralwidget)
        self.yacine.setGeometry(QtCore.QRect(20, 40, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono PS [UKWN]")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.yacine.setFont(font)
        self.yacine.setObjectName("yacine")
        self.mohamed = QtWidgets.QLabel(self.centralwidget)
        self.mohamed.setGeometry(QtCore.QRect(200, 40, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono PS [UKWN]")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mohamed.setFont(font)
        self.mohamed.setObjectName("mohamed")
        self.bilal = QtWidgets.QLabel(self.centralwidget)
        self.bilal.setGeometry(QtCore.QRect(380, 40, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono PS [UKWN]")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.bilal.setFont(font)
        self.bilal.setObjectName("bilal")
        self.score1 = QtWidgets.QLabel(self.centralwidget)
        self.score1.setGeometry(QtCore.QRect(20, 120, 131, 51))
        self.score1.setObjectName("score1")
        self.score1_2 = QtWidgets.QLabel(self.centralwidget)
        self.score1_2.setGeometry(QtCore.QRect(200, 120, 131, 51))
        self.score1_2.setObjectName("score1_2")
        self.score1_3 = QtWidgets.QLabel(self.centralwidget)
        self.score1_3.setGeometry(QtCore.QRect(380, 120, 131, 51))
        self.score1_3.setObjectName("score1_3")
        self.score = QtWidgets.QLineEdit(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(190, 190, 113, 33))
        self.score.setObjectName("score")

        self.timer2 = QtWidgets.QLabel(self.centralwidget)
        self.timer2.setGeometry(QtCore.QRect(200, 300, 100, 100))
        self.timer2.setText("")
        self.timer2.setFont(QtGui.QFont('Sanserif',30))
        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(210, 300, 100, 100))
        self.timer.setText("")
        self.timer.setFont(QtGui.QFont('Sanserif',30))
        self.j = -1

        pixmap = QPixmap('red.png')
        self.timer2.setPixmap(pixmap)
        self.timer2.setScaledContents(True)
        self.timer2.setObjectName("timer2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 230, 91, 30))
        self.pushButton.setText("Start")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.show()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.yacine.setText(_translate("MainWindow", "Yacine"))
        self.mohamed.setText(_translate("MainWindow", "Mohamed"))
        self.bilal.setText(_translate("MainWindow", "Bilal"))
        self.score1.setText(_translate("MainWindow", "0"))
        self.score1_2.setText(_translate("MainWindow", "0"))
        self.score1_3.setText(_translate("MainWindow", "0"))              
    def change(self):
        self.anim = QPropertyAnimation(self.timer, b"geometry")
        self.score.setText("0")
        while 200 > int(self.score1.text()) and 200 > int(self.score1_3.text()) and 200 > int(self.score1_2.text()):
            self.i =0
            self.j += 1
            while self.i < 151 and 200 > int(self.score1.text()) and 200 > int(self.score1_3.text()) and 200 > int(self.score1_2.text()):
                self.timer.setText(("{}".format(150-self.i)))
                QtTest.QTest.qWait(1000)
                self.score.returnPressed.connect(self.value)
                if self.i == 150 :
                    self.value()
                self.i  += 1


    def value(self):
        _translate = QtCore.QCoreApplication.translate
        if self.j == 0 :
            self.score1.setText(_translate("MainWindow", "{}".format(str(int(self.score.text())+int(self.score1.text())))))
        if self.j ==1 :
            self.score1_2.setText(_translate("MainWindow", "{}".format(str(int(self.score.text())+int(self.score1_2.text())))))
        if self.j ==2:
            self.score1_3.setText(_translate("MainWindow", "{}".format(str(int(self.score.text())+int(self.score1_3.text())))))
            self.j = -1
        self.score.setText("0")
        self.i = 151

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    time.sleep(2)
    sys.exit(app.exec_())    
