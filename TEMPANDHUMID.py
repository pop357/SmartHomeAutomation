
import sys
import serial
import random

from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout,QFrame
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from qt_material import apply_stylesheet, QtStyleTools
import re
import ocitavanje


class TemperatureHumidityTab(QWidget): 
    def __init__(self): 
        super().__init__() 
 
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)
        self.setStyleSheet("font-family: Arial; font-size: 20px;")
       
 
        self.primary_color = "#1E90FF"
        self.secondary_color = "#666666"

        
        self.temp_label = QLabel("Temperature:")
        self.temp_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.temp_value = QLabel()
        self.temp_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")

        self.humid_label = QLabel("Humidity:")
        self.humid_label.setStyleSheet("font-family: Arial; font-size: 14px; color: #666666;")
        self.humid_value = QLabel()
        self.humid_value.setStyleSheet("font-family: Arial; font-size: 18px; font-weight: bold; color: #1E90FF;")

        self.pressure_label = QLabel("Pressure:")
        self.pressure_label.setStyleSheet("font-family: Arial; font-size: 14px; color: #666666;")
        self.pressure_value = QLabel()
        self.pressure_value.setStyleSheet("font-family: Arial; font-size: 18px; font-weight: bold; color: #1E90FF;")

       
 
        
        layout = QVBoxLayout() 
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
       
        layout.addWidget(self.temp_label) 
        layout.addWidget(self.temp_value) 
        layout.addWidget(self.humid_label) 
        layout.addWidget(self.humid_value) 
        layout.addWidget(self.pressure_label)
        layout.addWidget(self.pressure_value)

        self.setLayout(layout)
 
        self.figure = Figure() 
        self.canvas = FigureCanvas(self.figure) 
        layout.addWidget(self.canvas) 
        
 
        layout.addStretch(1) 
        
        
        self.setLayout(layout) 
 
        
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.update_data) 
        self.timer.start(5000) 
         
        self.temp_data=[] 
        self.humid_data=[] 
        self.pressure_data=[]
        
        self.temp = 20.0
        self.humid = 20.0
        self.pressure = 1050.0
        
   
    
    def update_data(self):
        self.temp = self._extract_temp_data()
        self.humid = self._extract_humid_data()
        self.pressure = self._extract_pressure_data()
    

        self.temp_data = self.temp_data[-10:]
        self.humid_data = self.humid_data[-10:]
        self.pressure_data = self.pressure_data[-10:]

        self.temp_data.append(self.temp)
        self.humid_data.append(self.humid)
        self.pressure_data.append(self.pressure)
    
        if self.temp is not None:
            self.temp_value.setText(f"{self.temp:.1f} C")
        else:
            self.temp_value.setText("N/A")
        if self.humid is not None:
            self.humid_value.setText(f"{self.humid:.1f} %")
        else:
            self.humid_value.setText("N/A")
        if self.pressure is not None:
            self.pressure_value.setText(f"{self.pressure:.1f} hPa")
        else:
            self.pressure_value.setText("N/A")

   
        self.figure.clear()



        ax = self.figure.add_subplot(111)
        ax.plot(self.temp_data, linestyle=':', linewidth=2, label="Temperature")
        ax.plot(self.humid_data, linestyle='-', linewidth=2, label="Humidity")
        ax.plot(self.pressure_data, linestyle='--', linewidth=2, label="Pressure")
        ax.set_title('Temperature, Humidity and Pressure')


        ax.set_ylabel('Value')
        
 
        ax.legend(fontsize=8, facecolor='#2F4F4F', edgecolor='#D3D3D3', labelcolor='#D3D3D3',loc = 'upper left')

  
        ax.grid(True, linewidth=0.5, color='#D3D3D3')

   
        ax.set_facecolor('#1E1E1E')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('#D3D3D3')
        ax.spines['left'].set_color('#D3D3D3')

    
        ax.tick_params(axis='x', colors='#D3D3D3')
        ax.tick_params(axis='y', colors='#D3D3D3')

        self.canvas.draw()

    
    

    def _extract_temp_data(self):
        self.temp = ocitavanje.get_shared_temperature()
        return self.temp

    
    def _extract_humid_data(self):
        self.humid = ocitavanje.get_shared_humidity()
        return self.humid
   
    def _extract_pressure_data(self):
        self.pressure = ocitavanje.get_shared_pressure()
        return self.pressure
     
 

         
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QTabWidget, QLabel, QPushButton, QGridLayout
from qt_material import QtStyleTools
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QTabWidget, QLabel, QPushButton, QGridLayout
from qt_material import QtStyleTools
import sys

 
class SmartHomeAutomation(QWidget): 
    def __init__(self): 
        super().__init__() 
 
       
        self.setWindowTitle("Smart Home Automation") 
        self.setFixedSize(550, 400) 
        self.setWindowIcon(QIcon("icon.png")) 
 
       
        tab_widget = QTabWidget() 
        tab_widget.addTab(TemperatureHumidityTab(), "Temperature/Humidity") 
         
 
        
        layout = QVBoxLayout() 
        layout.addWidget(tab_widget) 
 
       
        self.setLayout(layout) 
 
     
        apply_stylesheet(self, theme='dark_teal.xml') 
        
        
if __name__ == "__main__":  
     app = QApplication(sys.argv)

    
    
     app.setApplicationName("Smart Home Automation")
     

     window = SmartHomeAutomation()
     window.show()

     sys.exit(app.exec_())
