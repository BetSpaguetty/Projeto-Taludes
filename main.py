from PyQt5.QtWidgets import QApplication
from app import TaludesApp
import sys
 
if __name__ == "__main__":

    app = QApplication(sys.argv)
    controller = TaludesApp()
    window = controller.window
    window.show()
    sys.exit(app.exec_())
  
    
   
     
 