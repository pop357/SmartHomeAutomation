import sys

import requests
from PySide6.QtGui import QPainter, QColor, QFont, QLinearGradient, QPen
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout, QFrame
from PySide6.QtGui import QFont, QIcon, QPixmap, QPalette, QColor, QImage, QMovie
from PySide6.QtCore import Qt, QTimer, QUrl


from qt_material import apply_stylesheet, QtStyleTools

# Weather API key
API_KEY = "a85a070117d643109d1130055230407"

# ...

from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QImage, QPainter, QPalette, QPixmap
from PySide6.QtCore import Qt, QTimer

# ...

class WeatherWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set the widget background color and font
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        self.setPalette(palette)
        self.setStyleSheet("font-family: Arial; font-size: 20px;")

        self.primary_color = "#1E90FF"
        self.secondary_color = "#666666"

        # Create the labels to display the data
        self.weather_label = QLabel("Weather:")
        self.weather_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.weather_value = QLabel()
        self.weather_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")

        self.temperature_label = QLabel("Temperature:")
        self.temperature_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.temperature_value = QLabel()
        self.temperature_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")

        self.humidity_label = QLabel("Humidity:")
        self.humidity_label.setStyleSheet(f"font-family: Arial; font-size: 14px; color: {self.secondary_color};")
        self.humidity_value = QLabel()
        self.humidity_value.setStyleSheet(f"font-family: Arial; font-size: 18px; font-weight: bold; color: {self.primary_color};")

        # Create a layout to add the labels
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

        # Set up a timer to update the data every 5 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_weather)
        self.timer.start(5000)

    def update_weather(self):
        try:
            # Send a request to Weather API to get weather data
            url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Novi Sad"
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx errors

            data = response.json()

            # Extract weather condition, temperature, and humidity from the response
            condition = data['current']['condition']['text']
            temperature = data['current']['temp_c']
            humidity = data['current']['humidity']

            # Update label values
            self.weather_value.setText(condition)
            self.temperature_value.setText(f"{temperature}°C")
            self.humidity_value.setText(f"{humidity}%")

            # Set image based on weather condition
            if condition.lower() == "sunny":
                image_path = "path/to/sunny.png"  # Replace with the path to your sunny image
            else:
                image_path = "path/to/cloudy.png"  # Replace with the path to your cloudy image

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

        # Set the window title, size, and icon
        self.setWindowTitle("Smart Home Automation")
        self.setFixedSize(550, 400)

        # Create the weather widget
        weather_widget = WeatherWidget()

        # Create the layout to add the weather widget
        layout = QVBoxLayout()
        layout.addWidget(weather_widget)

        # Set the layout of the main window
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Set the application name for settings
    app.setApplicationName("Smart Home Automation")

    window = SmartHomeAutomation()
    window.show()

    sys.exit(app.exec())



