import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *       
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
        # windows frame
        self.setWindowTitle("Movie Audience Prediction")
        self.setGeometry(750, 150, 500, 700)                # (x axis, y axis, x axis size, y axis size)

        self.pushButton1 = QPushButton(' Introduction ') 
        self.pushButton1.clicked.connect(self.pushButton1Clicked)
        self.pushButton2 = QPushButton(' Ranking ')  
        self.pushButton2.clicked.connect(self.pushButton2Clicked)
        self.pushButton3 = QPushButton(' Chart ')  
        self.pushButton3.clicked.connect(self.pushButton3Clicked)
        self.pushButton4 = QPushButton(' Visualization ') 
        self.pushButton4.clicked.connect(self.pushButton4Clicked)
        self.pushButton5 = QPushButton(' Prediction ')  
        self.pushButton5.clicked.connect(self.pushButton5Clicked)
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
        self.pushButton4.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.pushButton5.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)


        image = QLabel(self)
        pixmap = QPixmap("./Data/movie_forecast_title.png")
        image.setPixmap(pixmap)
        image.setGeometry(0, 0, 0, 0)
        image.show()

        # Layout 생성
        topLayout = QVBoxLayout()
        
        # Right Layout
        bottomLayout = QGridLayout()
        bottomLayout.addWidget(image, 0, 1, 1, 1)
        bottomLayout.addWidget(self.label1, 0, 0)
        bottomLayout.addWidget(self.label1, 0, 2)
        bottomLayout.addWidget(self.pushButton1, 2, 1)
        bottomLayout.addWidget(self.pushButton2, 3, 1)
        bottomLayout.addWidget(self.pushButton3, 4, 1)
        bottomLayout.addWidget(self.pushButton4, 5, 1)
        bottomLayout.addWidget(self.pushButton5, 9, 1)

        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addLayout(bottomLayout)
        layout.setStretchFactor(topLayout, 1)
        layout.setStretchFactor(bottomLayout, 1)  

        self.setLayout(layout)
    
    def pushButton1Clicked(self) : # introduction
        os.system('python project-intro.py')

    def pushButton2Clicked(self) : # ranking
        os.system('python project-ranking.py')

    def pushButton3Clicked(self) : # chart
        os.system('python project-chart.py')
    
    def pushButton4Clicked(self) : # visualize
        os.system('python project-visualization.py')
    
    def pushButton5Clicked(self) : # machine learning
        os.system('python project-ml.py')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = mywindows()
    mywindow.show()
    app.exec_()