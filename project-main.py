import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       # 종료하는 것은 widget만으로 안됨. 추가적으로 import 해줘야 함
from PyQt5.QtGui import QImage
from PyQt5.QtGui import *
import subprocess
import os


class mywindows(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()
        self.setStyleSheet('font-size: 13pt; font-family: Courier;')
        self.setWindowIcon(QIcon('logo.png'))
        self.setStyleSheet("background-color: white;")

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("영화 관람객 예측")
        self.setGeometry(750, 150, 500, 700)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)

        self.pushButton1 = QPushButton(' 개 요 ')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton(' 차 트 ')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton(' 시각화 ')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton5 = QPushButton('관람객 수 예측하기')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton5.clicked.connect(self.pushButton5Clicked)
        self.pushButton7 = QPushButton(' 순 위 ')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton7.clicked.connect(self.pushButton7Clicked)
        self.label1 = QLabel("")

        self.pushButton1.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton2.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton3.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton5.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton7.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)


        image = QLabel(self)
        pixmap = QPixmap("./Data/movie_forecast_title.png")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 0, 0)
        image.show()

        # Layout 생성
        topLayout = QVBoxLayout()
        #topLayout.addWidget(image)
        
        # Right Layout
        bottomLayout = QGridLayout()
        bottomLayout.addWidget(image, 0, 1, 1, 1)
        bottomLayout.addWidget(self.label1, 0, 0)
        bottomLayout.addWidget(self.label1, 0, 2)
        bottomLayout.addWidget(self.pushButton1, 2, 1)
        bottomLayout.addWidget(self.pushButton7, 3, 1)
        bottomLayout.addWidget(self.pushButton2, 4, 1)
        bottomLayout.addWidget(self.pushButton3, 5, 1)
        bottomLayout.addWidget(self.pushButton5, 9, 1)


        # Layout : V Layout 2개를 나란히 붙이려면 H Layout을 사용해야함
        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addLayout(bottomLayout)
        layout.setStretchFactor(topLayout, 1)
        layout.setStretchFactor(bottomLayout, 1)  # 0은 크기 조절시 크기 변경 안됨

        self.setLayout(layout)
    
    def pushButton1Clicked(self) : # 브랜드 소개
        os.system('python project-08.py')

    def pushButton2Clicked(self) : # chart
        os.system('python project-01.py')
    
    def pushButton3Clicked(self) : # visualize
        os.system('python project-02.py')
    
    def pushButton5Clicked(self) : # machineLearning 1
        os.system('python project-06.py')

    def pushButton7Clicked(self) : # using Data
        os.system('python project-07.py')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = mywindows()
    mywindow.show()
    app.exec_()