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

from sklearn.tree import DecisionTreeClassifier      # 0인지 1인지 객관식이기때문에 Classifier로 사용
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import os

if platform.system() == "Darwin" :    #Darwin은 MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"   
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


# 머신러닝
class machineLearingDialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()
        self.setStyleSheet('font-size: 13pt; font-family: Courier;')

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("MACHINE LEARNING")
        self.setGeometry(700, 150, 500, 350)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('logo.png'))          # 왼쪽 상단에 icon 넣기

        self.pushButton1 = QPushButton("관객수 예측")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        # self.pushButton2 = QPushButton("입지 선정")
        # self.pushButton2.clicked.connect(self.pushButton2Clicked)

        self.label1 = QLabel("연도 : ")
        self.label2 = QLabel("월 : ")
        
        self.label4 = QLabel("감독 : ")
        self.label5 = QLabel("배우 : ")
        self.label6 = QLabel("배급사 : ")
        self.label7 = QLabel("장르 : ")
        self.label8 = QLabel("등급 : ")
        self.label9 = QLabel("")
        # self.label4 = QLabel("")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit6 = QLineEdit()
        self.lineEdit7 = QLineEdit()
        self.lineEdit8 = QLineEdit()
    

        # Layout : V Layout 2개를 나란히 붙이려면 H Layout을 사용해야함
        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0,)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        
        layout.addWidget(self.label4, 2, 0)
        layout.addWidget(self.lineEdit4, 2, 1)

        layout.addWidget(self.label5, 3, 0)
        layout.addWidget(self.lineEdit5, 3, 1)
        
        layout.addWidget(self.label6, 4, 0)
        layout.addWidget(self.lineEdit6, 4, 1)

        layout.addWidget(self.label7, 5, 0)
        layout.addWidget(self.lineEdit7, 5, 1)

        layout.addWidget(self.label8, 6, 0)
        layout.addWidget(self.lineEdit8, 6, 1)

        
        
        
        
        
        
        
        layout.addWidget(self.pushButton1, 7, 1)
        layout.addWidget(self.label9, 8, 1)
        #layout.addWidget(self.pushButton2, 4, 1)


    
        self.setLayout(layout)

    # def pushButton2Clicked(self) :
    #     os.system('python pizza_geo2.py')

    def pushButton1Clicked(self) :
        year = int(self.lineEdit1.text())
        month = int(self.lineEdit2.text())

        director = str(self.lineEdit4.text())
        actor = str(self.lineEdit5.text())

        deliver = str(self.lineEdit6.text())
        genre = str(self.lineEdit7.text())

        level = str(self.lineEdit8.text())

        # year = self.lineEdit1.text()
        # month = self.lineEdit2.text()

        # director = self.lineEdit4.text()
        # actor = self.lineEdit5.text()

        # deliver = self.lineEdit6.text()
        # genre = self.lineEdit7.text()

        # level = self.lineEdit8.text()
        
        

        #total_line_up=pd.read_csv("C:/Users/KJW/Desktop/KJW/BigData/pySpace/PyQt GUI/workspace/movie/ten.csv")#,encoding='CP949'

        total_line_up=pd.read_csv("./ten.csv")
        
        year_input = float(year)
        month_input =float(month)
        
        director_input = total_line_up.loc[total_line_up['개별감독'].str.contains(director), '개별감독_index'].reset_index()['개별감독_index'][0]
        
        actor_input = total_line_up.loc[total_line_up['개별배우'].str.contains(actor), '개별배우_index'].reset_index()['개별배우_index'][0]
        
        deliver_input = total_line_up.loc[total_line_up['개별배급사'].str.contains(deliver), '개별배급사_index'].reset_index()['개별배급사_index'][0]
        
        genre_input = total_line_up.loc[total_line_up['개별장르'].str.contains(genre), '개별장르_index'].reset_index()['개별장르_index'][0]
        
        level_input = total_line_up.loc[total_line_up['등급'].str.contains(level), '등급_index'].reset_index()['등급_index'][0]
        
        
        # from sklearn.externals import joblib
        load_model=joblib.load("./movie_knn_model.sav")
        
        pre1 = load_model.predict([[year_input, month_input, director_input, actor_input ,deliver_input,genre_input,level_input]])
        
        self.label9.setText("예상관객수는 : " + str(np.exp(pre1)))
        #return print(np.exp(pre1))
        

        # else :
        #     cost = format(cost, ",") + "원"
        #     #self.label3.setText("최소 창업 비용 :", mincost, "\n원하는 지역 :", city, "\n안타깝지만 해당 비용으로 원하는 지역에서 창업하실 수 없습니다.")
        #     self.label3.setText("창업 비용 : " + str(cost) + "\n원하는 지역 : " + str(area) + "\n\n안타깝지만 해당 비용으로 \n원하는 지역에서 창업하실 수 없습니다.")
        #     #self.label4.setText("안타깝지만 해당 비용으로 원하는 지역에서 창업하실 수 없습니다.")

            
class mywindows(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # 윈도우 frame
        self.setWindowTitle("project-06")
        self.setGeometry(800, 200, 300, 300)                # (x축 좌표, y축 좌표, x축 크기, y축 크기)
        self.setWindowIcon(QIcon('light.png'))          # 왼쪽 상단에 icon 넣기
        
        self.pushButton = QPushButton('MACHINE LEARNING')  # Button, layout생성해서 사용할 때는 self 없이
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

        # Layout 생성
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.pushButton)
        self.setLayout(layout)
    
    def pushButtonClicked(self) :
        dlg = machineLearingDialog()        
        dlg.exec_()
        
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = machineLearingDialog()
    mywindow.show()
    app.exec_()