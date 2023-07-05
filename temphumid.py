import sys
import random

from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout,QFrame
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from qt_material import apply_stylesheet, QtStyleTools
 
class TemperatureHumidityTab(QWidget): 
    def __init__(self): 
        super().__init__() 
 
        # Set the tab background color and font 
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)
        self.setStyleSheet("font-family: Arial; font-size: 20px;")
 
        self.primary_color = "#1E90FF"
        self.secondary_color = "#666666"

         # Create the labels to display the data 
        self.temp_label = QLabel("Temperature:")
        self.temp_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.temp_value = QLabel()
        self.temp_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")

        self.humid_label = QLabel("Humidity:")
        self.humid_label.setStyleSheet("font-family: Arial; font-size: 14px; color: #666666;")
        self.humid_value = QLabel()
        self.humid_value.setStyleSheet("font-family: Arial; font-size: 18px; font-weight: bold; color: #1E90FF;")


      
        
 
        # Create a layout to add the labels 
        layout = QVBoxLayout() 
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
       
        layout.addWidget(self.temp_label) 
        layout.addWidget(self.temp_value) 
        layout.addWidget(self.humid_label) 
        layout.addWidget(self.humid_value) 
        

        self.setLayout(layout)
 
        self.figure = Figure() 
        self.canvas = FigureCanvas(self.figure) 
        layout.addWidget(self.canvas) 
        
 
        layout.addStretch(1) 
        
        # Set the layout of the tab 
        self.setLayout(layout) 
 
        # Set up a timer to update the data every 5 seconds 
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.update_data) 
        self.timer.start(5000) 
         
        self.temp_data=[] 
        self.humid_data=[] 
        
   
    
    def update_data(self):
    # Generate random data
        temp = random.uniform(20, 30)
        humid = random.uniform(40, 60)

    # Append data to lists and keep only the last 10 values
        self.temp_data.append(temp)
        self.humid_data.append(humid)
        self.temp_data = self.temp_data[-10:]
        self.humid_data = self.humid_data[-10:]

    # Update label values
        self.temp_value.setText(f"{temp:.1f} C")
        self.humid_value.setText(f"{humid:.1f} %")

    # Clear figure and plot new data
        self.figure.clear()
       
        

        ax = self.figure.add_subplot(111)
        ax.plot(self.temp_data, linestyle=':', linewidth=2, label="Temperature")
        ax.plot(self.humid_data, linestyle='-', linewidth=2, label="Humidity")
        ax.set_title('Temperature and Humidity')
        
        ax.set_ylabel('Value')

    # Set x and y axis labels and legend
        ax.legend(fontsize=8, facecolor='#2F4F4F', edgecolor='#D3D3D3', labelcolor='#D3D3D3',loc = 'upper left')

    # Set grid and line colors
        ax.grid(True, linewidth=0.5, color='#D3D3D3')

    # Set background color and border for plot area
        ax.set_facecolor('#1E1E1E')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('#D3D3D3')
        ax.spines['left'].set_color('#D3D3D3')

    # Set tick colors
        ax.tick_params(axis='x', colors='#D3D3D3')
        ax.tick_params(axis='y', colors='#D3D3D3')
    
        self.canvas.draw()

         
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
 
        # Set the window title, size, and icon 
        self.setWindowTitle("Smart Home Automation") 
        self.setFixedSize(550, 400) 
        self.setWindowIcon(QIcon("icon.png")) 
 
        # Create the tab widget and add the Temperature/Humidity tab 
        tab_widget = QTabWidget() 
        tab_widget.addTab(TemperatureHumidityTab(), "Temperature/Humidity") 
         
 
        # Create the layout to add the tab widget 
        layout = QVBoxLayout() 
        layout.addWidget(tab_widget) 
 
        # Set the layout of the main window 
        self.setLayout(layout) 
 
        # Apply the Qt Material style 
        apply_stylesheet(self, theme='dark_teal.xml')
        
        
if __name__ == "__main__":  
     app = QApplication(sys.argv)

    # Set the application name and organization for settings
    
     app.setApplicationName("Smart Home Automation")
     

     window = SmartHomeAutomation()
     window.show()

     sys.exit(app.exec_())
