from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from DDCores.base import *

class VerticalBar(DDWidget) :

    def __init__(self) :
        super().__init__()
        self.setFixedWidth(60)
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setContentsMargins(5,10,5,0)
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setAlignment(Qt.AlignTop)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('mainBoxV')
        self.setStyleSheet(QSS_VERTICAL)



    def putOnLayout(self, button:QPushButton) :
        self.mainBoxLayout.addWidget(button, alignment=Qt.AlignHCenter)


    def addItem(self, iconPath: str, size=22) -> QPushButton :
        icon = QIcon(iconPath)
        button = QPushButton()
        button.setObjectName('contextButton')
        button.setIcon(icon)
        button.setIconSize(QSize(size, size))
        button.setCursor(QCursor(Qt.PointingHandCursor))
        self.putOnLayout(button)
        return button




class HorizontalBar(DDWidget) :

    def __init__(self) :
        super().__init__()
        self.setFixedHeight(40)
        self.mainBoxLayout = QHBoxLayout()
        self.mainBoxLayout.setContentsMargins(10,2,10,2)
        self.mainBoxLayout.setSpacing(0)
        self.mainBoxLayout.setAlignment(Qt.AlignLeft)
        self.mainBox.setLayout(self.mainBoxLayout)
        self.mainBox.setObjectName('mainBoxH')
        self.setStyleSheet(QSS_HORIZONTAL)


    def putOnLayout(self, button:QPushButton) :
        self.mainBoxLayout.addWidget(button, alignment=Qt.AlignVCenter)


    def addButtonIcon(self, iconPath: str) -> QPushButton :
        icon = QIcon(iconPath)
        button = QPushButton()
        button.setObjectName('contextButton')
        button.setIcon(icon)
        button.setIconSize(QSize(22, 22))
        button.setCursor(QCursor(Qt.PointingHandCursor))
        self.putOnLayout(button)
        return button

    def addButton(self, title) :
        button = QPushButton(title)
        button.setObjectName('contextButton')
        button.setFixedWidth(60)
        button.setFixedHeight(25)
        button.setCursor(QCursor(Qt.PointingHandCursor))
        self.putOnLayout(button)
        return button



QSS_VERTICAL = """

#mainBoxV {
    background-color: #151515;
    border-right: 1px solid #303030;
    }



#contextButton {
    width: 100%;
    height: 40px;
    background-color: #151515;
    border-radius: 10px;

}

#contextButton:hover {
    background-color: #252525;

    }

    

"""
QSS_HORIZONTAL = """

#mainBoxH {
    background-color: #151515;
    border-bottom: 1px solid #303030;
    }

#contextButton {
    background-color: #151515;
    border-radius: 3px;
    color: white;
    font-size: 13px;

}

#contextButton:hover {
    background-color: #252525;

    }


"""


