import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       
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
        self.setWindowTitle("VISUALIZATION")
        self.setGeometry(300, 70, 1300, 800)             
        self.setWindowIcon(QIcon('logo.png'))          

        self.pushButton15 = QPushButton("Director")
        self.pushButton15.clicked.connect(self.pushButton15Clicked)
        self.pushButton16 = QPushButton("Actor")
        self.pushButton16.clicked.connect(self.pushButton16Clicked)
        self.pushButton17 = QPushButton("Film Distributor")
        self.pushButton17.clicked.connect(self.pushButton17Clicked)
        self.pushButton18 = QPushButton("Visualization")
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

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)  

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