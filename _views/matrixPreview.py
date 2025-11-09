from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from __DDCores.base import *




class windowMapaPreview(DDWidget) : 

    def __init__(self):
        super().__init__()









class windowMapSelector(DDWidget) : 

    """
    Formato do dicionario : { 'name': str, 'size': float (size in mb) }
    """
    def __init__(self, maps:list[dict]):
        super().__init__()
        self._view()
        self.addMaps(maps)


    def _view(self) : 
        self.mainBoxLayout = QVBoxLayout()
        self.mainBoxLayout.setAlignment(Qt.AlignTop)
        self.mainBoxLayout.setContentsMargins(0,0,0,0)
        self.mainBoxLayout.setSpacing(0)
        self.mainBox.setLayout(self.mainBoxLayout)

        # PESQUISA ------------------------------ >>>
        self.widgetSearchArea = QWidget()
        self.layoutSearchArea = QHBoxLayout()
        self.widgetSearchArea.setLayout(self.layoutSearchArea)
        self.searchBar = QLineEdit()
        self.layoutSearchArea.addWidget(self.searchBar)
        self.mainBoxLayout.addWidget(self.widgetSearchArea)
        # CORPO --------------------------------- >>>
        self.widgetMaps = QWidget()
        self.layoutMaps = QVBoxLayout()
        self.layoutMaps.setAlignment(Qt.AlignTop)
        self.widgetMaps.setLayout(self.layoutMaps)
        self.mainBoxLayout.addWidget(self.widgetMaps)


        self.setStyleSheet(QSS)




    def addMaps(self, maps:list) : 
        for map in maps : 
            button = self.createButtonMapSelector(map['name'], map['size'])
            self.layoutMaps.addWidget(button)


    def createButtonMapSelector(self, name:str, size:float) -> QPushButton : 
        button = QPushButton()
        layout = QHBoxLayout()
        layout.setContentsMargins(10,0,10,0)
        layout.setSpacing(0)
        layout.addWidget(QLabel(name))
        layout.addStretch()
        layout.addWidget(QLabel(str(size)))
        button.setLayout(layout)
        button.setObjectName('buttonMapSelector')
        return button







QSS = """


#buttonMapSelector { 


}


"""


