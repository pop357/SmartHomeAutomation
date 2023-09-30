from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QThread, Slot, Signal,
    QSize, QTime, QUrl, Qt
)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform
)
from PySide6.QtWidgets import (
    QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QStatusBar, QTableWidget, QColorDialog,
    QTableWidgetItem, QVBoxLayout, QWidget
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QResource, QIODevice, QFile
from TEMPANDHUMID import TemperatureHumidityTab
from ui_automacija import Ui_MainWindow
from weather import WeatherWidget
from lights import LightControlTab
from accontroler import ACControlTab
from PySide6.QtCore import QTimer
import ocitavanje
import serial
import re
import sys






class Worker(QThread):
    signalDataRecv = Signal(str)
    signalFinished = Signal()

    def __init__(self):
        super().__init__()
        self.ser = serial.Serial('COM3', 9600)

    def run(self):
        
        print("Otvorena komunikacija")
        while self.ser.is_open:
            try:
                text = self.ser.readline().decode().rstrip('\n')
                if "Temperature" in text:
                    temperature_str = text.split("=")[1].strip().split()[0]
                    temperature = float(temperature_str)
                    ocitavanje.set_shared_temperature(temperature)
                    print(temperature)
                elif "Humidity" in text:
                    humidity_str = text.split("=")[1].strip().split()[0]
                    humidity = float(humidity_str)
                    ocitavanje.set_shared_humidity(humidity)
                    print(f"Humidity: {humidity}")
                elif "Pressure" in text:
                    pressure_str = text.split("=")[1].strip().split()[0]
                    pressure = float(pressure_str)
                    ocitavanje.set_shared_pressure(pressure)
                    print(f"Pressure: {pressure}")
                   
                
            except Exception as e:
                print(f"Error during serial communication: {e}")
                break
        self.ser.close()
        self.signalFinished.emit()

    def write_data(self, data):
        self.ser.write(data.encode())
    def stop(self):
        self.ser.close()
    def analogWrite(self,pin, intensity):
        self.ser.write(f'analogWrite {pin} {intensity}\n'.encode())
  

class MainWindow(QMainWindow):
    signalDataSend = Signal(str)

    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        ui_file = QFile("automacija.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()
        
        
        self.th = None
        
       

        self.setCentralWidget(self.ui)

        self.temperature_humidity_tab = TemperatureHumidityTab()
        self.light_tab = LightControlTab()
        self.ac_tab = ACControlTab()
        self.weather = WeatherWidget()
        
        index = self.ui.stackedWidget.indexOf(self.ui.page_3)
        index4 = self.ui.stackedWidget.indexOf(self.ui.page_5)
        index3 = self.ui.stackedWidget.indexOf(self.ui.page_4)
        index0 = self.ui.stackedWidget.indexOf(self.ui.page_2)

        page_2_contents = self.ui.stackedWidget.widget(index0)
        page_3_contents = self.ui.stackedWidget.widget(index)
        page_4_contents = self.ui.stackedWidget.widget(index3)
        page_5_contents = self.ui.stackedWidget.widget(index4)

        for i in reversed(range(page_3_contents.layout().count())):
            page_3_contents.layout().itemAt(i).widget().setParent(None)

        for i in reversed(range(page_5_contents.layout().count())):
            page_5_contents.layout().itemAt(i).widget().setParent(None)

        for i in reversed(range(page_4_contents.layout().count())):
            page_4_contents.layout().itemAt(i).widget().setParent(None)
        
        for i in reversed(range(page_2_contents.layout().count())):
            page_2_contents.layout().itemAt(i).widget().setParent(None)

        page_3_contents.layout().addWidget(self.temperature_humidity_tab)
        page_5_contents.layout().addWidget(self.light_tab)
        page_4_contents.layout().addWidget(self.ac_tab)
        page_2_contents.layout().addWidget(self.weather)

        
        self.start_com()

        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.indexOf(self.ui.page_2))))
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.indexOf(self.ui.page_3))))
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.indexOf(self.ui.page_5))))
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex((self.ui.stackedWidget.indexOf(self.ui.page_4))))

    
    
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)  
              
        self.light_tab.on_button.clicked.connect(self.turn_lights_on)
        self.light_tab.off_button.clicked.connect(self.turn_lights_off)
        self.light_tab.color_button.clicked.connect(self.change_lights_color)
        
        
        
        
        self.ac_tab.on_button.clicked.connect(self.turn_ac_on)
        self.ac_tab.off_button.clicked.connect(self.turn_ac_off)
        self.ac_tab.left_button.clicked.connect(self.ac_left)
        self.ac_tab.turbo_button.clicked.connect(self.ac_turbo)
        self.ac_tab.right_button.clicked.connect(self.ac_right)
        self.ac_tab.temperature_changed.connect(self.receive_data_ac)
        self.ac_tab.up_button.clicked.connect(self.ac_up)
        self.ac_tab.down_button.clicked.connect(self.ac_down)
        
        

        
        
        self.setWindowTitle("Automacija")
        self.setFixedSize(900, 500)

   
      
       
    
    

    @Slot()
    def create_worker(self):
        self.th = Worker()
        self.th.signalDataRecv.connect(self.receive_data_ac)
        self.th.signalFinished.connect(self.th.deleteLater)
        self.th.start()
    @Slot()
    def start_com(self):
        if self.th is None:
            self.create_worker()   
        
    @Slot()
    def receive_data_ac(self,temperature):
        temperature = self.ac_tab.temperature
        red, green, blue = self.change_color_based_on_temperature(temperature)
        color = QColor(red, green, blue)
        print(f"Temperature: {temperature}")
    @Slot()
    def change_color_based_on_temperature(self, temperature):
        red_intensity = 255
        green_intensity = 255
        blue_intensity = 255
        temperature = self.ac_tab.temperature
        if temperature == 25:
            red_intensity = 255
            green_intensity = 0
            blue_intensity = 255
        elif temperature > 25:
            red_intensity = int(255 * (31 - temperature) / (31 - 25))
            green_intensity = 255
            blue_intensity = 255
        elif temperature < 25:
            blue_intensity = int(255 * (temperature - 16) / (25 - 16))
            red_intensity = 255
            green_intensity = 255

        self.th.analogWrite(9, red_intensity)
        self.th.analogWrite(10, green_intensity)
        self.th.analogWrite(11, blue_intensity)

        return red_intensity, green_intensity, blue_intensity
    @Slot()
    def ac_down(self):
        temperature = self.ac_tab.temperature
        self.change_color_based_on_temperature(temperature)
    @Slot()    
    def ac_up(self):
        temperature = self.ac_tab.temperature
        self.change_color_based_on_temperature(temperature)
    
    @Slot()
    def stop_com(self):
        try:
            
            if self.th is not None:
                self.th.signalFinished.connect(self.th.quit)
                self.th.stop()
                self.th.wait()
                self.th.deleteLater()
                self.th = None
        except Exception as e:
            print(e)
        
    

    
    
        
      
   
       

    @Slot()
    def turn_lights_on(self):
        print('Turn ON')
        self.th.write_data("LightOn\n")
        

        
        
    @Slot()
    def change_lights_color(self):
         
        color = QColorDialog.getColor()
        if color.isValid():
            self.primary_color = color.name()
            self.light_tab.on_button.setStyleSheet(
                f"font-family: Arial; font-size: 16px; color: #FFFFFF; "
                f"background-color: {self.primary_color}; border: none; "
                f"border-radius: 5px; padding: 5px 10px;"
             )
            self.light_tab.off_button.setStyleSheet(
                f"font-family: Arial; font-size: 16px; color: {self.primary_color}; "
                f"background-color: #D3D3D3; border: none; border-radius: 5px; "
                f"padding: 5px 10px;"
        )

        r, g, b = color.red(), color.green(), color.blue()
        command = f'l {r},{g},{b}\n'
        self.th.write_data(command)
   
          
            
    @Slot()       
    def turn_lights_off(self):
        self.th.write_data("LightOff\n")
        print('Turn OFF')
    
    @Slot()
    def turn_ac_on(self):
        self.th.write_data("acOn\n")
        print("Klima on")
    
    @Slot()
    def turn_ac_off(self):
        self.th.write_data("acOff\n")      
        print("Klima off")
    
    @Slot()
    def ac_left(self):
        self.th.analogWrite(9, 50)      
        self.th.analogWrite(10, 255)   
        self.th.analogWrite(11, 50)    
    @Slot()
    def ac_right(self):  
        self.th.analogWrite(9, 180)    
        self.th.analogWrite(10, 200)     
        self.th.analogWrite(11, 180)  
    @Slot()     
    def ac_turbo(self):
        self.th.analogWrite(9, 0)
        self.th.analogWrite(10, 115)
        self.th.analogWrite(11, 255)


    def closeEvent(self,event):
        self.stop_com()
        print("Zatvaranje app")


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
