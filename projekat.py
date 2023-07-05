from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout
from temphumid import TemperatureHumidityTab

from ui_automacija import Ui_MainWindow
from PySide6.QtCore import QResource, QIODevice, QFile
from weather import WeatherWidget
from lights import LightControlTab



from ui_automacija import Ui_MainWindow
from PySide6.QtCore import QResource, QIODevice, QFile
from weather import WeatherWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        # UI load
        loader = QUiLoader()
        ui_file = QFile("automacija.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close() 
        self.activate_()

        
        
        
        # Set mains window
        self.setCentralWidget(self.ui) 
        self.temperature_humidity_tab = TemperatureHumidityTab()
       
       # Find index of page_3
        index = self.ui.stackedWidget.indexOf(self.ui.page_3)
        
# Export content of page_3
        page_3_contents = self.ui.stackedWidget.widget(index)
        

# Delete the content of page_3
        for i in reversed(range(page_3_contents.layout().count())):
          page_3_contents.layout().itemAt(i).widget().setParent(None)
         
          
        

# Add the  TemperatureHumidityTab in page_3
        page_3_contents.layout().addWidget(self.temperature_humidity_tab)
     
        
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.indexOf(self.ui.page_2)) ))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.indexOf(self.ui.page_3)) ))
       
        self.setWindowTitle("Automacija")
        self.setFixedSize(900,500)
        self.temperature_humidity_tab = TemperatureHumidityTab()
       
       
      
      
       

    
    def activate_(self):
        
        self.ui.closeButton.clicked.connect(self.close_win)
        self.ui.miniButton.clicked.connect(self.minimize)
        self.ui.maxiButton.clicked.connect(self.maxmize_minimize)
    def open_close_menu(self):
        width = self.leftMenu.maximumWidth()
        fr = QFrame()
        if width == 200:
            self.leftMenu.setMaximumWidth(43)
        else:
            self.leftMenu.setMaximumWidth(200)
        # return width

    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()

    def maxmize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
            
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
