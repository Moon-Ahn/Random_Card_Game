#!/usr/bin/env python3
#coding: UTF-8
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from scapy.all import *
import random
from PyQt5 import QtCore

path1 = "./picture/작은기회"
S = os.listdir(path1)

path2 = "./picture/큰기회"
B = os.listdir(path2)

path3 = "./picture/시장"
M = os.listdir(path3)

path4 = "./picture/지출"
G = os.listdir(path4)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 설정

        self.setGeometry(500, 220, 1920, 1080)  # x, y, w, h
        self.setWindowTitle('Card Game')
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.center()
        self.setStyleSheet("background-color: white;")

        # QButton 위젯 생성
        self.button1 = QPushButton('', self)
        self.button1.clicked.connect(self.Start1)
        self.button1.setGeometry(0, 0, 640, 540)
        self.button1.setIcon(QtGui.QIcon('picture_re/re/re_작은기회_메인.jpg'))
        self.button1.setIconSize(QtCore.QSize(640, 540))

        self.button2 = QPushButton('', self)
        self.button2.clicked.connect(self.Start2)
        self.button2.setGeometry(640, 0, 640, 540)
        self.button2.setIcon(QtGui.QIcon('./picture/화면/메인화면/큰기회_메인.jpg'))
        self.button2.setIconSize(QtCore.QSize(640, 540))
        #self.button2.setCheckable(True)

        self.button3 = QPushButton('', self)
        self.button3.clicked.connect(self.Start3)
        self.button3.setGeometry(0, 540, 640, 540)
        self.button3.setIcon(QtGui.QIcon('./picture/화면/메인화면/시장카드_메인.jpg'))
        self.button3.setIconSize(QtCore.QSize(640, 540))
        #self.button3.setCheckable(True)

        self.button4 = QPushButton('', self)
        self.button4.clicked.connect(self.Start4)
        self.button4.setGeometry(640, 540, 640, 540)
        self.button4.setIcon(QtGui.QIcon('./picture/화면/메인화면/지출카드_메인.jpg'))
        self.button4.setIconSize(QtCore.QSize(640, 540))
        #self.button4.setCheckable(True)

        self.button5 = QPushButton('', self)
        self.button5.clicked.connect(self.Start5)
        self.button5.setGeometry(1280, 0, 640, 270)
        self.button5.setIcon(QtGui.QIcon('./picture/화면/메인화면/월급날_메인.jpg'))
        self.button5.setIconSize(QtCore.QSize(640, 270))
        #self.button5.setCheckable(True)

        self.button6 = QPushButton('', self)
        self.button6.clicked.connect(self.Start6)
        self.button6.setGeometry(1280, 270, 640, 270)
        self.button6.setIcon(QtGui.QIcon('./picture/화면/메인화면/아기탄생_메인.jpg'))
        self.button6.setIconSize(QtCore.QSize(640, 270))
        #self.button6.setCheckable(True)

        self.button7 = QPushButton('', self)
        self.button7.clicked.connect(self.Start7)
        self.button7.setGeometry(1280, 540, 640, 270)
        self.button7.setIcon(QtGui.QIcon('./picture/화면/메인화면/자선_메인.jpg'))
        self.button7.setIconSize(QtCore.QSize(640, 270))
        #self.button7.setCheckable(True)

        self.button8 = QPushButton('', self)
        self.button8.clicked.connect(self.Start8)
        self.button8.setGeometry(1280, 810, 640, 270)
        self.button8.setIcon(QtGui.QIcon('./picture/화면/메인화면/정리해고_메인.jpg'))
        self.button8.setIconSize(QtCore.QSize(640, 270))
        #self.button8.setCheckable(True)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#######################################################################

    # 버튼 이벤트 함수

    def Start1(self):
        #print('kk')
        print(len(S))
        if len(S) == 0:
            self.Q1 = QMessageBox.about(self, 'Message', '작은기회카드가 모두 소진되었습니다')
            return 0
        a = random.randint(0, len(S) - 1)
        print(a)
        print(S[a])
        p1 = './picture/작은기회/' + str(S[a])
        print(p1)
        self.buttonE1 = QPushButton('', self)
        self.buttonE1.clicked.connect(self.Disappear1)
        self.buttonE1.setGeometry(0, 0, 1920, 1080)
        self.buttonE1.setIcon(QtGui.QIcon(p1))
        self.buttonE1.setIconSize(QtCore.QSize(1920, 1080))
        self.buttonE1.show()
        S.pop(a)
        # self.button1.setIcon(QtGui.QIcon(p))
        # self.button1.setIconSize(QtCore.QSize(200, 225))


    def Disappear1(self):
        self.buttonE1.hide()

    def Start2(self):
        # print('kk')
        print(len(B))
        if len(B) == 0:
            self.Q2 = QMessageBox.about(self, 'Message', '큰기회카드가 모두 소진되었습니다')
            return 0
        a = random.randint(0, len(B) - 1)
        print(a)
        print(B[a])
        p2 = './picture/큰기회/' + str(B[a])
        print(p2)
        self.buttonE2 = QPushButton('', self)
        self.buttonE2.clicked.connect(self.Disappear2)
        self.buttonE2.setGeometry(0, 0, 1920, 1080)
        self.buttonE2.setIcon(QtGui.QIcon(p2))
        self.buttonE2.setIconSize(QtCore.QSize(1920, 1080))
        self.buttonE2.show()
        B.pop(a)

    def Disappear2(self):
        self.buttonE2.hide()

    def Start3(self):
        # print('kk')
        print(len(M))
        if len(M) == 0:
            self.Q3 = QMessageBox.about(self, 'Message', '시장카드가 모두 소진되었습니다')
            return 0
        a = random.randint(0, len(M) - 1)
        print(a)
        print(M[a])
        p3 = './picture/시장/' + str(M[a])
        print(p3)
        self.buttonE3 = QPushButton('', self)
        self.buttonE3.clicked.connect(self.Disappear3)
        self.buttonE3.setGeometry(0, 0, 1920, 1080)
        self.buttonE3.setIcon(QtGui.QIcon(p3))
        self.buttonE3.setIconSize(QtCore.QSize(1920, 1080))
        self.buttonE3.show()
        M.pop(a)

    def Disappear3(self):
        self.buttonE3.hide()

    def Start4(self):
        # print('kk')
        print(len(G))
        if len(G) == 0:
            self.Q4 = QMessageBox.about(self, 'Message', '지출카드가 모두 소진되었습니다')
            return 0
        a = random.randint(0, len(G) - 1)
        print(a)
        print(G[a])
        p4 = './picture/지출/' + str(G[a])
        print(p4)
        self.buttonE4 = QPushButton('', self)
        self.buttonE4.clicked.connect(self.Disappear4)
        self.buttonE4.setGeometry(0, 0, 1920, 1080)
        self.buttonE4.setIcon(QtGui.QIcon(p4))
        self.buttonE4.setIconSize(QtCore.QSize(1920, 1080))
        self.buttonE4.show()
        G.pop(a)
        # self.button4.setIcon(QtGui.QIcon(p))
        # self.button4.setIconSize(QtCore.QSize(200, 225))

    def Disappear4(self):
        self.buttonE4.hide()

    def Start5(self):
        # print('kk')
        self.buttonE5 = QPushButton('', self)
        self.buttonE5.clicked.connect(self.Disappear5)
        self.buttonE5.setGeometry(0, 0, 1920, 1080)
        self.buttonE5.setIcon(QtGui.QIcon('./picture/화면/큰화면/월급날_큰화면.jpg'))
        self.buttonE5.setIconSize(QtCore.QSize(1920, 1080))
        self.buttonE5.show()

    def Disappear5(self):
        self.buttonE5.hide()

    def Start6(self):
        # print('kk')
        self.buttonE6 = QPushButton('', self)
        self.buttonE6.clicked.connect(self.Disappear6)
        self.buttonE6.setGeometry(0, 0, 1920, 1080)
        self.buttonE6.setIcon(QtGui.QIcon('./picture/화면/큰화면/아기탄생_큰화면.jpg'))
        self.buttonE6.setIconSize(QtCore.QSize(1920, 1080))
        self.buttonE6.show()

    def Disappear6(self):
        self.buttonE6.hide()

    def Start7(self):
        # print('kk')
        self.buttonE7 = QPushButton('', self)
        self.buttonE7.clicked.connect(self.Disappear7)
        self.buttonE7.setGeometry(0, 0, 1920, 1080)
        self.buttonE7.setIcon(QtGui.QIcon('./picture/화면/큰화면/자선_큰화면.jpg'))
        self.buttonE7.setIconSize(QtCore.QSize(1920, 1080))
        self.buttonE7.show()

    def Disappear7(self):
        self.buttonE7.hide()

    def Start8(self):
        # print('kk')
        self.buttonE8 = QPushButton('', self)
        self.buttonE8.clicked.connect(self.Disappear8)
        self.buttonE8.setGeometry(0, 0, 1920, 1080)
        self.buttonE8.setIcon(QtGui.QIcon('./picture/화면/큰화면/정리해고_큰화면.jpg'))
        self.buttonE8.setIconSize(QtCore.QSize(1920, 1080))
        self.buttonE8.show()

    def Disappear8(self):
        self.buttonE8.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())