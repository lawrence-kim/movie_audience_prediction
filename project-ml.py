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
import os

if platform.system() == "Darwin" :    #Darwin is for MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"   
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


class machineLearingDialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()
        self.setStyleSheet('font-size: 13pt; font-family: Courier;')

    def setupUI(self) :
        # windows frame
        self.setWindowTitle("MACHINE LEARNING")
        self.setGeometry(700, 150, 500, 350)                
        self.setWindowIcon(QIcon('logo.png'))          

        self.pushButton1 = QPushButton("Audience Prediction")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.label1 = QLabel("year : ")
        self.label2 = QLabel("month : ")
        self.label4 = QLabel("director : ")
        self.label5 = QLabel("actor : ")
        self.label6 = QLabel("film distributor : ")
        self.label7 = QLabel("genre : ")
        self.label8 = QLabel("content rating : ")
        self.label9 = QLabel("")

        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit6 = QLineEdit()
        self.lineEdit7 = QLineEdit()
        self.lineEdit8 = QLineEdit()
    
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
        self.setLayout(layout)

    def pushButton1Clicked(self) :
        year = int(self.lineEdit1.text())
        month = int(self.lineEdit2.text())
        director = str(self.lineEdit4.text())
        actor = str(self.lineEdit5.text())
        deliver = str(self.lineEdit6.text())
        genre = str(self.lineEdit7.text())
        level = str(self.lineEdit8.text())
        total_line_up=pd.read_csv("./ten.csv")
        
        year_input = float(year)
        month_input =float(month)
        director_input = total_line_up.loc[total_line_up['개별감독'].str.contains(director), '개별감독_index'].reset_index()['개별감독_index'][0]
        actor_input = total_line_up.loc[total_line_up['개별배우'].str.contains(actor), '개별배우_index'].reset_index()['개별배우_index'][0]
        deliver_input = total_line_up.loc[total_line_up['개별배급사'].str.contains(deliver), '개별배급사_index'].reset_index()['개별배급사_index'][0]
        genre_input = total_line_up.loc[total_line_up['개별장르'].str.contains(genre), '개별장르_index'].reset_index()['개별장르_index'][0]
        level_input = total_line_up.loc[total_line_up['등급'].str.contains(level), '등급_index'].reset_index()['등급_index'][0]
        
        from sklearn.externals import joblib
        load_model=joblib.load("./movie_knn_model.sav")       
        pre1 = load_model.predict([[year_input, month_input, director_input, actor_input ,deliver_input,genre_input,level_input]])
        self.label9.setText("audience prediction : " + str(np.exp(pre1)))
            
class mywindows(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # winidows frame
        self.setWindowTitle("Machine Learning")
        self.setGeometry(800, 200, 300, 300)                
        self.setWindowIcon(QIcon('light.png'))          
        self.pushButton = QPushButton('MACHINE LEARNING')  
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel()

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