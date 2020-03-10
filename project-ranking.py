import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       
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

if platform.system() == "Darwin" :    #Darwin is for MAC OS
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    path="c:/windows/Fonts/malgun.ttf"      # font = 210 M고딕050.ttf
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
else :
    print("Unknown System")


class visualialog(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setupUI()

    def setupUI(self) :
        # windows frame
        self.setWindowTitle(" Ranking ")
        self.setGeometry(300, 80, 1300, 800)
        self.setWindowIcon(QIcon('logo.png'))

        self.label1 = QLabel("")
        self.label2 = QLabel("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        self.pushButton2 = QPushButton("Director")
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton("Actor")
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton("Film Distributor")
        self.pushButton4.clicked.connect(self.pushButton4Clicked)

        # Table Widget
        global tableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(500, 500)
        # Left Layout
        global leftLayout
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.tableWidget)
        # Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.pushButton2)
        rightLayout.addWidget(self.pushButton3)
        rightLayout.addWidget(self.pushButton4)        
        rightLayout.addWidget(self.label2)
        rightLayout.addWidget(self.label1)
        rightLayout.addStretch(1)
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  
        self.setLayout(layout)


    def pushButton2Clicked(self) :
        movie = pd.read_csv("./Data/directors_spectators.csv")    
        self.tableWidget.setRowCount(movie.shape[0])        
        self.tableWidget.setColumnCount(movie.shape[1])
        self.label1.setText("total number of rows: " + str(movie.shape[0]))
        self.tableWidget.setHorizontalHeaderLabels(list(movie.columns))

        movieLists = []
        movieData = {}
        for i in range(len(movie)) :
            
            for row in movie.itertuples():
                movieData['개별감독'] = row.개별감독 # director
                movieData['누적관객수'] = str(row.누적관객수) # accumulated number of audiences
                movieLists.append(list(movieData.values()))

        data = movieLists

        # director, accumulated number of audiences 
        for idx, (개별감독, 누적관객수) in enumerate(movieLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(개별감독))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적관객수))

    def pushButton3Clicked(self) :
        movie = pd.read_csv("./Data/actors_spectators.csv")

        self.tableWidget.setRowCount(movie.shape[0])            
        self.tableWidget.setColumnCount(movie.shape[1])
        self.label1.setText("total number of rows: " + str(movie.shape[0]))
        self.tableWidget.setHorizontalHeaderLabels(list(movie.columns))
        movieLists = []
        movieData = {}

        for i in range(len(movie)) :
            
            for row in movie.itertuples():
                movieData['개별배우'] = row.개별배우 # actor
                movieData['누적관객수'] = str(row.누적관객수) # accumulated number of audiences

                movieLists.append(list(movieData.values()))

        data = movieLists

        # actor, accumulated number of audiences
        for idx, (개별배우,  누적관객수) in enumerate(movieLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(개별배우))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적관객수))
    
    def pushButton4Clicked(self) :
        movie = pd.read_csv("./Data/distributors_spectators.csv")
        

        self.tableWidget.setRowCount(movie.shape[0])          
        self.tableWidget.setColumnCount(movie.shape[1])
        self.label1.setText("total number of rows: " + str(movie.shape[0]))
        self.tableWidget.setHorizontalHeaderLabels(list(movie.columns))

        movieLists = []
        movieData = {}
        for i in range(len(movie)) :
            
            for row in movie.itertuples():
                movieData['개별배급사'] = row.개별배급사 # film distributor
                movieData['누적관객수'] = str(row.누적관객수) # accumulated number of audiences
                movieLists.append(list(movieData.values()))

        data = movieLists
        
        # film distributor , accumulated number of audiences 
        for idx, (개별배급사,  누적관객수) in enumerate(movieLists): 
            self.tableWidget.setItem(idx, 0, QTableWidgetItem(개별배급사))
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(누적관객수))
    
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = visualialog()
    mywindow.show()
    app.exec_()