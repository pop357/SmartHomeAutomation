import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout,QFrame, QSlider, QColorDialog, QComboBox
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, QTimer,Slot,Signal, QThread, QObject
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from qt_material import apply_stylesheet, QtStyleTools
import time
import serial




    
class LightControlTab(QWidget): 
    signalDataSend = Signal(str)
    def __init__(self): 
        super().__init__() 
        
        
        self.redPin = 3
        self.greenPin = 5
        self.bluePin = 6
        
        
        
      
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)
        self.setStyleSheet("font-family: Arial; font-size: 20px;")

        self.primary_color = "#1E90FF"
        self.secondary_color = "#666666"

        
        self.light_label = QLabel("Light:")
        self.light_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.light_value = QLabel("Off")
        self.light_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.secondary_color};")

        
        self.on_button = QPushButton("On")
        self.on_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
        self.on_button.clicked.connect(self.turn_on)

        self.off_button = QPushButton("Off")
        self.off_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
        self.off_button.clicked.connect(self.turn_off)

        self.color_button = QPushButton("Change Color")
        self.color_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
        

       
        layout = QGridLayout() 
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        layout.addWidget(self.light_label, 0, 0) 
        layout.addWidget(self.light_value, 0, 1) 
        layout.addWidget(self.on_button, 1, 0)
        layout.addWidget(self.off_button, 1, 1)
        layout.addWidget(self.color_button, 1, 2)

        self.setLayout(layout)    
        self.setWindowTitle("Lighting Control") 
        self.setFixedSize(550, 400) 
        self.setWindowIcon(QIcon("icon.png"))

   
    def turn_on(self):
        self.light_value.setText("On")
        self.set_light_style(self.primary_color)
      
        
        
      

    def set_light_style(self, color):
        font_style = "font-family: Arial; font-size: 16px;"
        on_button_style = f"{font_style} color: #FFFFFF; background-color: {color}; border: none; border-radius: 5px; padding: 5px 10px;"
        off_button_style = f"{font_style} color: {color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;"
        
        self.on_button.setStyleSheet(on_button_style)
        self.off_button.setStyleSheet(off_button_style)

    def turn_off(self):
        self.light_value.setText("Off")
        self.light_value.setStyleSheet(
            f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.secondary_color};"
        )
        self.on_button.setStyleSheet(
            f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;"
        )
        self.off_button.setStyleSheet(
            f"font-family: Arial; font-size: 16px; color: #FFFFFF; background-color: {self.primary_color}; border: none; border-radius: 5px; padding: 5px 10px;"
        )
       
        
       

    
    ''''def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.primary_color = color.name()
            self.on_button.setStyleSheet(
                f"font-family: Arial; font-size: 16px; color: #FFFFFF; "
                f"background-color: {self.primary_color}; border: none; "
                f"border-radius: 5px; padding: 5px 10px;"
            )
            self.off_button.setStyleSheet(
                f"font-family: Arial; font-size: 16px; color: {self.primary_color}; "
                f"background-color: #D3D3D3; border: none; border-radius: 5px; "
                f"padding: 5px 10px;"
            )
            
            # Get RGB values and format for Arduino
            #r, g, b = color.red(), color.green(), color.blue()
            #command = f'l {r},{g},{b}\n'
            #ser.write(command.encode())
            #response = ser.readline().decode().strip()
    
                     '''

    
if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        apply_stylesheet(app, theme='dark_teal.xml')
        # Set the application name and organization for settings
        app.setApplicationName("Lighting Control")
        

        window = LightControlTab()
       
        window.show()
       
      

        sys.exit(app.exec_())
    except Exception as e:
        print(f"An error occurred: {e}")