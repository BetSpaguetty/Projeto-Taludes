from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DDWidget(QWidget) :

    def __init__(self):
        super().__init__()
        self.baseLayout = QHBoxLayout()
        self.baseLayout.setSpacing(0)
        self.baseLayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.baseLayout)
        self.mainBox = QWidget()
        self.baseLayout.addWidget(self.mainBox)
        


class DDScrollWidget(QWidget) :
    
    def __init__(self):
        super().__init__()
        self.baseLayout = QHBoxLayout()
        self.baseLayout.setSpacing(0)
        self.baseLayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.baseLayout)
        self.scrollArea = QScrollArea()
        self.scrollArea.setObjectName('scroll')
        self.scrollArea.setWidgetResizable(True) 
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  
        self.baseLayout.addWidget(self.scrollArea)
        self.mainBox = QWidget()
        self.scrollArea.setWidget(self.mainBox)



class DDVerticalLine(QWidget) :
    def __init__(self, color='white'):
        super().__init__()
        self.setFixedWidth(1)
        qh = QHBoxLayout()
        qh.setSpacing(0)
        qh.setContentsMargins(0,0,0,0)
        self.setLayout(qh)
        line = QWidget()
        qh.addWidget(line)
        line.setStyleSheet(f"color: {color}; background-color: {color};")



class DDHorizontalLine(QFrame) :
    def __init__(self, color='white'):
        super().__init__()
        self.setFixedHeight(1)
        qh = QHBoxLayout()
        qh.setSpacing(0)
        qh.setContentsMargins(0,0,0,0)
        self.setLayout(qh)
        line = QWidget()
        qh.addWidget(line)
        line.setStyleSheet(f"color: {color}; background-color: {color};")




class DDHBoxLayout(QHBoxLayout) : 

    def __init__(self, spacing=0, contentMargins=(0,0,0,0)) : 
        super().__init__()

        self.setSpacing(spacing)
        self.setContentsMargins(*contentMargins)



class DDVBoxLayout(QVBoxLayout) : 

    def __init__(self, spacing=0, contentMargins=(0,0,0,0)) : 
        super().__init__()
        self.setSpacing(spacing)
        self.setContentsMargins(*contentMargins)




