import sys

import requests
from PySide6.QtGui import QPainter, QColor, QFont, QLinearGradient, QPen
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout, QFrame
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QColor, QImage, QMovie
from PySide6.QtCore import Qt, QTimer, QUrl


from qt_material import apply_stylesheet, QtStyleTools


API_KEY = "a85a070117d643109d1130055230407"



from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QImage, QPainter, QPalette, QPixmap
from PySide6.QtCore import Qt, QTimer



class WeatherWidget(QWidget):
    def __init__(self):
        super().__init__()

        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)
        self.setStyleSheet("font-family: Arial; font-size: 20px;")

        self.primary_color = "#1E90FF"
        self.secondary_color = "#666666"

        
        self.weather_label = QLabel("Weather:")
        self.weather_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.weather_value = QLabel()
        self.weather_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")

        self.temperature_label = QLabel("Temperature outside:")
        self.temperature_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.temperature_value = QLabel()
        self.temperature_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")

        self.humidity_label = QLabel("Humidity outside:")
        self.humidity_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.humidity_value = QLabel()
        self.humidity_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")

       
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        layout.addWidget(self.weather_label)
        layout.addWidget(self.weather_value)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.temperature_value)
        layout.addWidget(self.humidity_label)
        layout.addWidget(self.humidity_value)

        self.setLayout(layout)

        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_weather)
        self.timer.start(5000)

    def update_weather(self):
        try:
           
            url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Novi Sad"
            response = requests.get(url)
            response.raise_for_status()  

            data = response.json()

            
            condition = data['current']['condition']['text']
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']

          
            self.weather_value.setText(condition)
            self.temperature_value.setText(f"{temperature}°C")
            self.humidity_value.setText(f"{humidity}%")

          
            if condition.lower() == "clear":
                image_path = "aaa"
            elif condition.lower() == "rain":
                image_path = "ccc"
            elif condition.lower() == "snow":
                image_path = "ddd"
            elif condition.lower() == "cloudy":
                image_path = "eee"
            elif condition.lower() == "windy":
                image_path = "fff"
            elif condition.lower() == "sunny":
                image_path = "ggg"
                
            image = QImage(image_path)
            if not image.isNull():
                self.weather_value.setPixmap(QPixmap.fromImage(image).scaledToWidth(200))
            else:
                print("Failed to load the image")

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch weather data: {e}")


class SmartHomeAutomation(QWidget):
    def __init__(self):
        super().__init__()

       
        self.setWindowTitle("Smart Home Automation")
        self.setFixedSize(550, 400)

       
        weather_widget = WeatherWidget()

       
        layout = QVBoxLayout()
        layout.addWidget(weather_widget)

       
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the application name for settings
    app.setApplicationName("Smart Home Automation")

    window = SmartHomeAutomation()
    window.show()

    sys.exit(app.exec())



