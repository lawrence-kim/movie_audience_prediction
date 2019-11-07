import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       # 종료하는 것은 widget만으로 안됨. 추가적으로 import 해줘야 함
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

if platform.system() == "Darwin" :    #Darwin은 MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      # 210 M고딕050.ttf
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


# chart 그리기

class graphDialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("Chart")
        self.setGeometry(200, 100, 1600, 800)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('logo.png'))         # 왼쪽 상단에 icon 넣기

        self.pushButton1 = QPushButton("월별 평균 누적관객수")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton("연도별 평균 누적관객수")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("장르별 누적관객수")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton("등급별 누적관객수")
        self.pushButton4.clicked.connect(self.pushButton4Clicked)

        # Figure Canvas
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        
        # Left Layout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.pushButton1)
        rightLayout.addWidget(self.pushButton2)
        rightLayout.addWidget(self.pushButton3)
        rightLayout.addWidget(self.pushButton4)
        rightLayout.addStretch(1)   # 제일 상단에 배치

        # Layout : V Layout 2개를 나란히 붙이려면 H Layout을 사용해야함
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  # 0은 크기 조절시 크기 변경 안됨

        self.setLayout(layout)


    def pushButton1Clicked(self) :
        
        movie_month = pd.read_csv("./Data/oneoneone_month_spectators.csv")
        ax = self.fig.add_subplot(111)
        ax.clear()
        result = movie_month['누적관객수']
        colors = cm.coolwarm(np.linspace(1,0,len(result)))
        labels = movie_month['월']
        result.plot(kind = 'bar', color = colors, ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + rect.get_width() / 2, 
                    rect.get_height() + 1, s = label, ha = 'center', va = 'bottom', fontsize=17)
                    
        ax.set_xlabel('월', fontsize = 20)
        ax.set_title('월별 누적관객수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()

    def pushButton2Clicked(self) :
        
        movie_year = pd.read_csv("./Data/oneoneone_year_spectators.csv")
        ax = self.fig.add_subplot(111)
        ax.clear()
        result = movie_year['누적관객수']
        colors = cm.coolwarm(np.linspace(1,0,len(result)))
        labels = movie_year['년']
        result.plot(kind = 'bar', color = colors, ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + rect.get_width() / 2, 
                    rect.get_height() + 1, s = label, ha = 'center', va = 'bottom', fontsize=17)
                    
        ax.set_xlabel('년', fontsize = 20)
        ax.set_title('연별 누적관객수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()

    def pushButton3Clicked(self) :
        
        movie_genre = pd.read_csv("./Data/oneoneone_genre_spectators.csv")
        ax = self.fig.add_subplot(111)
        ax.clear()
        result = movie_genre['누적관객수']
        colors = cm.coolwarm(np.linspace(1,0,len(result)))
        labels = movie_genre['개별장르']
        result.plot(kind = 'bar', color = colors, ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + rect.get_width() / 2, 
                    rect.get_height() + 1, s = label, ha = 'center', va = 'bottom', fontsize=17)
                    
        ax.set_xlabel('장르', fontsize = 20)
        ax.set_title('장르별 누적관객수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()

    def pushButton4Clicked(self) :
        movie_rating = pd.read_csv("./Data/oneoneone_rating_spectators.csv")        
        ax = self.fig.add_subplot(111)
        ax.clear()
        result = movie_rating['누적관객수']
        colors = cm.coolwarm(np.linspace(1,0,len(result)))
        labels = movie_rating['등급']
        result.plot(kind = 'bar', color = colors, ax = ax)
        rects = ax.patches

        for rect, label in zip(rects, labels) :
            plt.text(rect.get_x() + rect.get_width() / 2, 
                    rect.get_height() + 1, s = label, ha = 'center', va = 'bottom', fontsize=17)
                    
        ax.set_xlabel('등급', fontsize = 20)
        ax.set_title('등급별 누적관객수', fontsize = 25)
        for tick in ax.get_xticklabels():
            tick.set_rotation(0)
        self.canvas.draw()

    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = graphDialog()
    mywindow.show()
    app.exec_()