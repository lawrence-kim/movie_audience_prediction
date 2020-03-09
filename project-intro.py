import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       
from PyQt5.QtGui import *
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

from sklearn.tree import DecisionTreeClassifier      
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

if platform.system() == "Darwin" :    #Darwin is for MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      # font = 210 M고딕050.ttf
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


# 머신러닝
class machineLearingDialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # windows frame
        self.setWindowTitle("INTRODUCTION")
        self.setGeometry(400, 100, 1000, 600)                
        self.setWindowIcon(QIcon('logo.png'))         

        self.pushButton1 = QPushButton("Contributor")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("Objective")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("Korean Movie Industry")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)

        self.label1 = QLabel("\n\n\n\n\n\n\n\n\n\n")
        
        # Figure Canvas
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        global image
        image = QLabel(self)
        pixmap = QPixmap("./Data/noun_pizza-1.png")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 0, 0)
        image.show()
        topLayout = QGridLayout()
        topLayout.addWidget(self.pushButton1, 0, 0)
        topLayout.addWidget(self.pushButton2, 0, 1)
        topLayout.addWidget(self.pushButton3, 0, 2)

        global bottomLayout
        bottomLayout = QVBoxLayout()
        bottomLayout.addWidget(self.label1)

        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addLayout(bottomLayout)
        layout.setStretchFactor(topLayout, 0)
        layout.setStretchFactor(bottomLayout, 0) 
        self.setLayout(layout)


    def pushButton1Clicked(self) :
        self.label1.setText("""
        Lawrence Kim
        
        김용제

        김종완

        손병구
        """)

    def pushButton2Clicked(self) :
        self.label1.setText("""
        기존의 직감을 통한 영화 흥행 예측에서 빅데이터 분석을 통해 객관적으로 예측가능.\n
        그동안의 영화 시장은 열 편의 영화를 만들면 그 중 한 편이 소위 '대박'을 쳐서 나머지 아홉 편의 손실을\n
        보전해주는 확률 게임 식으로 운영되어 왔다. 스타 시스템, 작가 시스템, 프로듀서 시스템 등 안정적 흥행수익을\n
        얻기 위해 여러 시도들이 있었지만 과학적인 흥행 예측과는 거리가 멀었다. 오히려 노련한 제작자의 감과 트렌드를\n 
        읽어내는 능력이 더 잘 들어맞곤 했다고 전해진다. 최근 영화 흥행에 빅데이터 분석이 도입되면서 영화 제작은 \n
        더이상 감에 의존한 도박이 아닌 예측 가능한 산업으로 바뀌고 있다.
        """)

    def pushButton3Clicked(self) :
        self.label1.setText("""
        1919년 의리적 구투와 함께 시작한 한국영화 산업은 1998년 당시 5,000만 명에 불과했던 관람객 수가\n
        현재 2억명 수준으로 성장하였다. 한국 영화 제작 편수도 2004년 40편에서 373편까지 늘어났으며, 영화 수출액\n
        또한 1천만 달러를 돌파하며, 과거에 비해 무려 500배가 넘는 성장률을 기록하고 있다. 현재 국내영화시장은\n
        16억 달러 이상이며, 영화 시장 세계 21대 국가 중 5위를 차지를 하고 있을 정도로 그 위상이 상당하다.
        """)
     
        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = machineLearingDialog()
    mywindow.show()
    app.exec_()