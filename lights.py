import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout,QFrame, QSlider, QColorDialog, QComboBox
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QColor
from PySide6.QtCore import Qt, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from qt_material import apply_stylesheet, QtStyleTools
import time
import serial


ser = serial.Serial('COM3', 9600)

def analogWrite(pin, intensity):
    ser.write(f'analogWrite {pin} {intensity}\n'.encode())
    
class LightControlTab(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.redPin = 9
        self.greenPin = 10 
        self.bluePin = 11
        self.pixel_color = (255, 255, 255)*8
    
        # Set the tab title
        # Set the tab background color and font 
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)
        self.setStyleSheet("font-family: Arial; font-size: 20px;")

        self.primary_color = "#1E90FF"
        self.secondary_color = "#666666"

        # Create the labels to display the data 
        self.light_label = QLabel("Light:")
        self.light_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.light_value = QLabel("Off")
        self.light_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.secondary_color};")

        # Create the buttons to control the lights
        self.on_button = QPushButton("On")
        self.on_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
        self.on_button.clicked.connect(self.turn_on)

        self.off_button = QPushButton("Off")
        self.off_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
        self.off_button.clicked.connect(self.turn_off)

        self.color_button = QPushButton("Change Color")
        self.color_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
        self.color_button.clicked.connect(self.change_color)

        # Create a grid layout to add the labels, buttons, and pixel widgets
        layout = QGridLayout() 
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        layout.addWidget(self.light_label, 0, 0) 
        layout.addWidget(self.light_value, 0, 1) 
        layout.addWidget(self.on_button, 1, 0)
        layout.addWidget(self.off_button, 1, 1)
        layout.addWidget(self.color_button, 1, 2)

        # Set up the graphical representation of the LED strip
        
        # Set the main layout for the widget
        self.setLayout(layout)    
        self.setWindowTitle("Lighting Control") 
        self.setFixedSize(550, 400) 
        self.setWindowIcon(QIcon("icon.png"))

        # Create the tab widget and add the Lighting Control tab 
        # Create the layout to add the Lighting Control tab 
       
   
    def turn_on(self):
        self.light_value.setText("On")
        self.light_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")
        self.on_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: #FFFFFF; background-color: {self.primary_color}; border: none; border-radius: 5px; padding: 5px 10px;")
        self.off_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
        ser.write(b'1\n')  # Send 1 to turn on

    def turn_off(self):
        self.light_value.setText("Off")
        self.light_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.secondary_color};")
        self.on_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
        self.off_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: #FFFFFF; background-color: {self.primary_color}; border: none; border-radius: 5px; padding: 5px 10px;")
        ser.write(b'0\n')  # Send 0 to turn off

    
    def change_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.primary_color = color.name()
            self.on_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: #FFFFFF; background-color: {self.primary_color}; border: none; border-radius: 5px; padding: 5px 10px;")
            self.off_button.setStyleSheet(f"font-family: Arial; font-size: 16px; color: {self.primary_color}; background-color: #D3D3D3; border: none; border-radius: 5px; padding: 5px 10px;")
            
            # Get RGB values and format for Arduino
            r = color.red()
            g = color.green()
            b = color.blue()
            rgb = f"{r},{g},{b}\n"
            
            # Check serial connection before writing 
            if ser.isOpen():
                ser.write(rgb.encode())  # Send RGB values to Arduino
            else:
                print("Serial connection closed!")

    def update_pixel_colors(self):
        for i in range(8):
            r, g, b = self.pixel_colors[i]
            ser.write(f"{r},{g},{b}\n".encode())  # Send RGB values to Arduino

    def open_arduino_communication(self):
        # Otvaranje Arduino komunikacije
        try:
            self.ser = serial.Serial('COM3', 9600)
            print("Arduino communication opened successfully.")
        except serial.SerialException as e:
            print(f"Failed to open Arduino communication: {e}")
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