import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       # 종료하는 것은 widget만으로 안됨. 추가적으로 import 해줘야 함
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import os

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns

import platform
from matplotlib import font_manager,rc
import matplotlib as mpl
import matplotlib.cm as cm

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

if platform.system() == "Darwin" :    #Darwin은 MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      # 210 M고딕050.ttf
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")

# 시각화 자료 그리기

class visualialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle(" 순 위 ")
        self.setGeometry(300, 80, 1300, 800)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('logo.png'))        # 왼쪽 상단에 icon 넣기

        self.label1 = QLabel("")
        self.label2 = QLabel("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        self.pushButton2 = QPushButton("감독")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("배우")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton("배급사")
        self.pushButton4.clicked.connect(self.pushButton4Clicked)

        # Table Widget
        global tableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(500, 500)
        #self.setTableWidgetData()

        # Left Layout
        global leftLayout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.tableWidget)

        # Right Layout
        rightLayout = QVBoxLayout()
        # rightLayout.addWidget(self.pushButton1)
        rightLayout.addWidget(self.pushButton2)
        rightLayout.addWidget(self.pushButton3)
        rightLayout.addWidget(self.pushButton4)
        # rightLayout.addWidget(self.pushButton5)
        # rightLayout.addWidget(self.pushButton6)
        
        rightLayout.addWidget(self.label2)
        rightLayout.addWidget(self.label1)

        #rightLayout.addWidget(self.pushButton5)
        rightLayout.addStretch(1)   # 제일 상단에 배치


        # Layout : V Layout 2개를 나란히 붙이려면 H Layout을 사용해야함
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  # 0은 크기 조절시 크기 변경 안됨

        self.setLayout(layout)


    def pushButton2Clicked(self) :
        movie = pd.read_csv("./Data/oneoneone_directors_spectators.csv")
        # movie.fillna(0, inplace = True)
        

        self.tableWidget.setRowCount(movie.shape[0])             # table을 2 x 2로 만듦
        self.tableWidget.setColumnCount(movie.shape[1])
        self.label1.setText("데이터는 총 " + str(movie.shape[0]) + "개 입니다.")
        self.tableWidget.setHorizontalHeaderLabels(list(movie.columns))

        movieLists = []
        movieData = {}
        for i in range(len(movie)) :
            
            for row in movie.itertuples():
                movieData['개별감독'] = row.개별감독
                # movieData['누적매출액'] = str(row.누적매출액)
                movieData['누적관객수'] = str(row.누적관객수)
                # movieData['스크린수'] = str(row.스크린수)

                movieLists.append(list(movieData.values()))

        data = movieLists

        for idx, (개별감독, 누적관객수) in enumerate(movieLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(개별감독))
            # self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적매출액))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적관객수))
            # self.tableWidget.setItem(idx, 3, QTableWidgetItem(스크린수))

    def pushButton3Clicked(self) :
        movie = pd.read_csv("./Data/oneoneone_actors_spectators.csv")
        # movie.fillna(0, inplace = True)
        

        self.tableWidget.setRowCount(movie.shape[0])             # table을 2 x 2로 만듦
        self.tableWidget.setColumnCount(movie.shape[1])
        self.label1.setText("데이터는 총 " + str(movie.shape[0]) + "개 입니다.")
        self.tableWidget.setHorizontalHeaderLabels(list(movie.columns))

        movieLists = []
        movieData = {}
        for i in range(len(movie)) :
            
            for row in movie.itertuples():
                movieData['개별배우'] = row.개별배우
                # movieData['누적매출액'] = str(row.누적매출액)
                movieData['누적관객수'] = str(row.누적관객수)
                # movieData['스크린수'] = str(row.스크린수)

                movieLists.append(list(movieData.values()))

        data = movieLists

        for idx, (개별배우,  누적관객수) in enumerate(movieLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(개별배우))
            # self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적매출액))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적관객수))
            # self.tableWidget.setItem(idx, 3, QTableWidgetItem(스크린수))

    def pushButton4Clicked(self) :
        movie = pd.read_csv("./Data/oneoneone_distributors_spectators.csv")
        # movie.fillna(0, inplace = True)
        

        self.tableWidget.setRowCount(movie.shape[0])             # table을 2 x 2로 만듦
        self.tableWidget.setColumnCount(movie.shape[1])
        self.label1.setText("데이터는 총 " + str(movie.shape[0]) + "개 입니다.")
        self.tableWidget.setHorizontalHeaderLabels(list(movie.columns))

        movieLists = []
        movieData = {}
        for i in range(len(movie)) :
            
            for row in movie.itertuples():
                movieData['개별배급사'] = row.개별배급사
                # movieData['누적매출액'] = str(row.누적매출액)
                movieData['누적관객수'] = str(row.누적관객수)
                # movieData['스크린수'] = str(row.스크린수)

                movieLists.append(list(movieData.values()))

        data = movieLists

        for idx, (개별배급사,  누적관객수) in enumerate(movieLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(개별배급사))
            # self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적매출액))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적관객수))
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = visualialog()
    mywindow.show()
    app.exec_()