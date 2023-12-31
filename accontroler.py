import sys
import random
import serial
from pyfirmata import Arduino, util
import time

from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout,QFrame, QSpinBox
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, QTimer,QObject, Signal
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from qt_material import apply_stylesheet, QtStyleTools




class ACControlTab(QWidget): 
    temperature_changed = Signal(float)
    def __init__(self): 
        super().__init__() 
        
       
        
        self.is_on = False
        
        self.temperature = 20
        self.is_turbo = False
        self.temp_setpoint = QSpinBox()
        self.temp_setpoint.setMinimum(16)
        self.temp_setpoint.setMaximum(32)
        self.temp_setpoint.setValue(25)
       
       
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

        self.temp_setpoint_label = QLabel("Set temperature:")
        self.temp_setpoint_label.setStyleSheet("font-family: Arial; font-size: 14px; color: #666666;")
        
        self.temp_setpoint.setStyleSheet("font-family: Arial; font-size: 18px; font-weight: bold; color: #1E90FF;")

        
        self.on_button = QPushButton("ON")
        self.on_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #1E90FF; color: white;")
        self.off_button = QPushButton("OFF")
        self.off_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #666666; color: white;")
        self.up_button = QPushButton("▲")
        self.up_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #1E90FF; color: white;")
        self.down_button = QPushButton("▼")
        self.down_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #1E90FF; color: white;")
        self.left_button = QPushButton("◀")
        self.left_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #1E90FF; color: white;")
        self.right_button = QPushButton("▶")
        self.right_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #1E90FF; color: white;")
        self.fan_speed_label = QLabel("Fan speed:")
        self.fan_speed_label.setStyleSheet("font-family: Arial; font-size: 14px; color: #666666;")
        self.fan_speed = QSpinBox()
        self.fan_speed.setStyleSheet("font-family: Arial; font-size: 18px; font-weight: bold; color: #1E90FF;")
        self.fan_speed.setRange(1, 5)
        self.fan_speed.setValue(3)
        self.turbo_button = QPushButton("TURBO")
        self.turbo_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #FF8C00; color: white;")

        
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.temp_label, 0, 0)
        grid_layout.addWidget(self.temp_value, 0, 1)
        grid_layout.addWidget(self.temp_setpoint_label, 1, 0)
        grid_layout.addWidget(self.temp_setpoint, 1, 1)
        grid_layout.addWidget(self.on_button, 2, 0)
        grid_layout.addWidget(self.off_button, 2, 1)
        grid_layout.addWidget(self.up_button, 3, 1)
        grid_layout.addWidget(self.down_button, 5, 1)
        grid_layout.addWidget(self.left_button, 4, 0)
        grid_layout.addWidget(self.right_button, 4, 2)
        grid_layout.addWidget(self.fan_speed_label, 6, 0)
        grid_layout.addWidget(self.fan_speed, 6, 1)
        grid_layout.addWidget(self.turbo_button, 7, 1)
        
        self.setLayout(grid_layout)

        self.on_button.clicked.connect(self.turn_on)
        self.off_button.clicked.connect(self.turn_off)
        self.up_button.clicked.connect(self.move_up)
        self.down_button.clicked.connect(self.move_down)
        self.left_button.clicked.connect(self.move_left)
        self.right_button.clicked.connect(self.move_right)
        self.turbo_button.clicked.connect(self.toggle_turbo)
        self.temp_setpoint.valueChanged.connect(self.set_temperature)

        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.update_values)
        self.timer.start()
        
   
        
    def turn_on(self):
        self.is_on = True
        self.on_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #1E90FF; color: white;")
        self.off_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #666666; color: white;")
        self.temp_setpoint.setEnabled(True)
        self.up_button.setEnabled(True)
        self.down_button.setEnabled(True)
        self.fan_speed.setEnabled(True)
        self.turbo_button.setEnabled(True)
    
    def change_color_based_on_temperature(self, temperature):
        red_intensity = 255
        green_intensity = 255
        blue_intensity = 255

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
    
            
        return red_intensity, green_intensity, blue_intensity

        
        
    def turn_off(self):
        self.is_on = False
        self.off_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #1E90FF; color: white;")
        self.on_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #666666; color: white;")
        self.temp_setpoint.setEnabled(False)
        self.up_button.setEnabled(False)
        self.down_button.setEnabled(False)
        self.fan_speed.setEnabled(False)
        self.turbo_button.setEnabled(False)
   
    def move_up(self):
        if self.temperature < 30:
            self.temperature += 1
            self.temperature += 1 
            self.temp_value.setText(f"{self.temperature}°C")
            self.change_color_based_on_temperature(self.temperature)
    
    def move_down(self):
        if self.temperature > 16:
            self.temperature -= 1
            self.temp_value.setText(f"{self.temperature}°C")
            self.change_color_based_on_temperature(self.temperature)
            
    def move_left(self):
      ''''  self.analogWrite(9, 50)      
        self.analogWrite(10, 255)   
        self.analogWrite(11, 50)     
        '''
    def move_right(self):
        ''''  self.analogWrite(9, 180)  
        self.analogWrite(10, 200)      
        self.analogWrite(11, 180)    
        '''
    def toggle_turbo(self):
        self.is_turbo = not self.is_turbo  # Promjena vrijednosti između True i False
        if self.is_turbo:
            self.turbo_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #FF8C00; color: white;")
        else:
            self.turbo_button.setStyleSheet("font-family: Arial; font-size: 16px; font-weight: bold; padding: 10px 20px; background-color: #1E90FF; color: white;")
      
    def set_temperature(self, temperature):
        if 16 <= temperature <= 32:
            self.temperature = temperature
            self.temperature_changed.emit(temperature)
            self.temp_value.setText(f"{self.temperature}°C")
            self.change_color_based_on_temperature(self.temperature)
    
    def update_ui(self):
        self.change_color_based_on_temperature(self.temperature)
           
    def update_values(self):
        if self.is_turbo:
            if self.temperature < 30:
                self.temperature += 1
        elif self.temperature > 20:
            self.temperature -= 1
    
        
class MainWindow(QWidget): 
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("AC Control")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(100, 100, 800, 600)

       
        ac_control_tab = ACControlTab()
        ac_control_tab.set_temperature(25)
        tab_widget = QTabWidget()
        tab_widget.addTab(ac_control_tab, "AC Control")

       
        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)
        apply_stylesheet(self, 'dark_blue.xml')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_purple.xml')
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
