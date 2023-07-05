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
from ac_controller import ACControlTab
from lights import LightControlTab
from threading import Semaphore
from semaforThread import SemaforThread
from ui_automacija import Ui_MainWindow
from PySide6.QtCore import QResource, QIODevice, QFile
from weather import WeatherWidget
from PySide6.QtCore import QThread, QMutex

import serial

      
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.port_lock = QMutex() 
        
        loader = QUiLoader()
        ui_file = QFile("automacija.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close() 
        self.activate_()

        self.setCentralWidget(self.ui) 

        self.temperature_humidity_tab = TemperatureHumidityTab()
        self.ac_control_tab = ACControlTab()
        self.weather_tab = WeatherWidget()
        self.lights_tab = LightControlTab()

        # Pronalaženje indeksa stranica
        index0 = self.ui.stackedWidget.indexOf(self.ui.page_2)
        index3 = self.ui.stackedWidget.indexOf(self.ui.page_3)
        index1 = self.ui.stackedWidget.indexOf(self.ui.page_4)
        index2 = self.ui.stackedWidget.indexOf(self.ui.page_5)

        # Dohvaćanje sadržaja stranica
        page_2_contents = self.ui.stackedWidget.widget(index0)
        page_3_contents = self.ui.stackedWidget.widget(index3)
        page_4_contents = self.ui.stackedWidget.widget(index1)
        page_5_contents = self.ui.stackedWidget.widget(index2)

        for i in reversed(range(page_2_contents.layout().count())):
            page_2_contents.layout().itemAt(i).widget().setParent(None)

        for i in reversed(range(page_3_contents.layout().count())):
            page_3_contents.layout().itemAt(i).widget().setParent(None)

        for i in reversed(range(page_5_contents.layout().count())):
            page_5_contents.layout().itemAt(i).widget().setParent(None)

        layout = QVBoxLayout()
        page_4_contents.setLayout(layout)
        page_2_contents.setLayout(layout)
        page_5_contents.setLayout(layout)

        for i in reversed(range(page_4_contents.layout().count())):
            page_4_contents.layout().itemAt(i).widget().setParent(None)  

        # Dodavanje aplikacija
        page_3_contents.layout().addWidget(self.temperature_humidity_tab)
        page_4_contents.layout().addWidget(self.ac_control_tab)
        page_2_contents.layout().addWidget(self.weather_tab)
        page_5_contents.layout().addWidget(self.lights_tab)

        self.ui.btn_page_2.clicked.connect(lambda: self.open_arduino_communication(2))
        self.ui.btn_page_3.clicked.connect(lambda: self.open_arduino_communication(3))
        self.ui.btn_page_4.clicked.connect(lambda: self.open_arduino_communication(4))
        self.ui.btn_page_5.clicked.connect(lambda: self.open_arduino_communication(5))

        self.setWindowTitle("Automacija")
        self.setFixedSize(900, 500)

        self.arduino = None  # Inicijalizacija varijable za serijsku vezu s Arduinom

    def activate_(self):
        self.ui.closeButton.clicked.connect(self.close_win)
        self.ui.miniButton.clicked.connect(self.minimize)
        self.ui.maxiButton.clicked.connect(self.maximize_minimize)
    
    def open_arduino_connection(self):
        try:
            self.port_lock.lock()  # Zaključaj mutex
            if not self.arduino:
                self.arduino = serial.Serial('COM3', 9600)
                print("Serijska veza s Arduinom uspostavljena.")
        except serial.SerialException as e:
            print(f"Greška pri uspostavljanju serijske veze s Arduinom: {e}")
        finally:
            self.port_lock.unlock()  # Otključaj mutex

    def close_arduino_connection(self):
        self.port_lock.lock()
        try:
            if self.arduino and self.arduino.is_open:
                self.arduino.close()
                self.arduino = None
                print("Serijska veza s Arduinom zatvorena.")
        finally:
            self.port_lock.unlock()

    def open_arduino_communication(self, index):
        self.close_arduino_connection()  # Zatvorite postojeću serijsku vezu, ako postoji

        if index == 2:
            self.open_arduino_connection()  # Otvaranje serijske veze samo za tab 2
            self.arduino_communication = self.weather_tab
        elif index == 3:
            self.arduino_communication = self.temperature_humidity_tab
        elif index == 4:
            self.arduino_communication = self.ac_control_tab
        elif index == 5:
            self.arduino_communication = self.lights_tab

        self.port_lock.lock()  # Zaključaj mutex
        try:
            self.semafor_thread = SemaforThread(self.port_lock)
            self.semafor_thread.start()

            self.arduino_communication.open_arduino_communication()
        finally:
            self.port_lock.unlock()  # Otključaj mutex
    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()

    def maximize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
