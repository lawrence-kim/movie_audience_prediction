import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       # 종료하는 것은 widget만으로 안됨. 추가적으로 import 해줘야 함
from PyQt5.QtGui import *

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import seaborn as sns
import urllib.request
import json
import bs4
import locale
from locale import atof  
from matplotlib import rcParams, style
from matplotlib import cm, colors, _cm

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QBoxLayout

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

import platform
from matplotlib import font_manager,rc
import matplotlib as mpl

import time

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
        self.setWindowTitle("VISUALIZATION")
        self.setGeometry(300, 70, 1300, 800)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('logo.png'))          # 왼쪽 상단에 icon 넣기

        self.pushButton15 = QPushButton("감독")
        self.pushButton15.clicked.connect(self.pushButton15Clicked)
        self.pushButton16 = QPushButton("배우")
        self.pushButton16.clicked.connect(self.pushButton16Clicked)
        self.pushButton17 = QPushButton("배급사")
        self.pushButton17.clicked.connect(self.pushButton17Clicked)
        self.pushButton18 = QPushButton("누적관객수 시각화")
        self.pushButton18.clicked.connect(self.pushButton18Clicked)

        self.labelDone = QLabel("")
        self.label1 = QLabel("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.label2 = QLabel("\n\n\n\n\n\n\n")

        
        # Left Layout
        global leftLayout
        leftLayout = QVBoxLayout()

        # Right Layout
        rightLayout = QVBoxLayout()

        righttopLayout = QVBoxLayout()
        rightmidLayout = QGridLayout()
        rightbottomLayout = QVBoxLayout()

        righttopLayout.addWidget(self.label2)
        righttopLayout.addWidget(self.pushButton15)
        righttopLayout.addWidget(self.pushButton16)
        righttopLayout.addWidget(self.pushButton17)
        righttopLayout.addWidget(self.pushButton18)
        rightmidLayout.addWidget(self.labelDone, 7, 0)

        rightbottomLayout.addWidget(self.label1)
        rightbottomLayout.addWidget(self.labelDone)


        rightLayout.addLayout(righttopLayout)
        rightLayout.addLayout(rightmidLayout)
        rightLayout.addLayout(rightbottomLayout)
        #rightLayout.addStretch(1)   # 제일 상단에 배치

        # Layout : V Layout 2개를 나란히 붙이려면 H Layout을 사용해야함
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  # 0은 크기 조절시 크기 변경 안됨

        self.setLayout(layout)


    def pushButton15Clicked(self) :
        image = QLabel(self)
        pixmap = QPixmap("./Data/wc_director.png")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 0, 0)
        image.show()
        leftLayout.addWidget(image)

    
    def pushButton16Clicked(self) :
        image = QLabel(self)
        pixmap = QPixmap("./Data/wc_actor.png")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 0, 0)
        image.show()
        leftLayout.addWidget(image)

    def pushButton17Clicked(self) :
        
        image = QLabel(self)
        pixmap = QPixmap("./Data/wc_distributor.png")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 0, 0)
        image.show()
        leftLayout.addWidget(image)
    
    def pushButton18Clicked(self) :
        image = QLabel(self)
        pixmap = QPixmap("./Data/spectator_visualization.png")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 0, 0)
        image.show()
        leftLayout.addWidget(image)


        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = visualialog()
    mywindow.show()
    app.exec_()