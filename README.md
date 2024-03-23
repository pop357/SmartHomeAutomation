# SmartHomeAutomation


# About

## Smart Home Automation System

Welcome to the Smart Home Automation System project repository. This project is designed to provide an integrated solution for automating and controlling various aspects of your smart home. Below are the key components of this project:

### Temperature and Humidity Monitoring

The **Temperature and Humidity Monitoring** component is responsible for collecting real-time temperature and humidity data from external sensors. This data is then displayed on a user-friendly graphical interface. Users can easily keep track of indoor environmental conditions and make informed decisions based on this information.

### Light Control

With the **Light Control** feature, users gain precise control over their lighting systems. This component allows you to:

- **Turn Lights On and Off:** Users can remotely control the lighting in different areas of their home with a simple click.

- **Change Light Colors:** Customize the ambiance by changing the color of your lights. Select from a wide range of colors to suit your mood or preferences.

- **Adjust Lighting Intensity:** Fine-tune the brightness of your lights to create the perfect atmosphere for any occasion.

### Air Conditioning Control

The **Air Conditioning Control** feature offers control over your HVAC (Heating, Ventilation, and Air Conditioning) system. This allows users to:

- **Turn AC On and Off:** Easily manage the air conditioning system, ensuring optimal comfort and energy savings.

- **Temperature Settings:** Adjust the desired indoor temperature to match your comfort level.

- **Airflow Direction:** Control the direction of airflow to distribute conditioned air effectively.

- **Turbo Mode:** Activate turbo mode for rapid cooling or heating when needed.

### Weather Information

Stay informed about the weather conditions in your area with the **Weather Information** component. This feature provides real-time data on:

- **Temperature:** Current temperature readings for your location.

- **Humidity:** The relative humidity in the atmosphere.

- **Pressure:** Atmospheric pressure, which can be useful for weather forecasting.


### Prerequisites
Before you begin, ensure you have met the following requirements:

***Arduino IDE***: You will need the Arduino IDE installed to program the Arduino board and upload the code to it.

***Python***: This project requires Python to run. Make sure you have Python installed. You can download it from Python's official website.

***Python Libraries***: You need the following Python libraries installed. You can install them using pip:

***PySide6***: Install using pip install PySide6.
***matplotlib***: Install using pip install matplotlib.
***qt_material***: Install using pip install qt_material.
Serial Communication:  Project uses serial communication between Python and Arduino. Ensure that the Arduino board is correctly connected to your computer via USB.

Arduino Code: You'll need the Arduino code uploaded to your Arduino board. The Arduino code should be compatible with your hardware setup and match the communication protocol expected by your Python application.

Hardware Components: Make sure you have the required hardware components connected to your Arduino board as specified in your Arduino code and Python application. This might include sensors, LEDs, or other devices.

Ensure you have these prerequisites in place to run your project successfully. Additionally, provide any specific details or configurations that users or contributors need to know to set up the hardware and software correctly.

### Arduino Integration
  One of the key features of our project is the integration of Arduino microcontrollers as actuators. Here's how Arduino enhances our home automation system:
  
  **Serial Communication**: Arduino acts as an intermediary between the GUI application and hardware components. It communicates with the Python application through a serial connection.
  
  **Hardware Control**: Arduino is responsible for controlling hardware components such as RGB LED lights and sensors.
  
  **Dynamic Lighting**: The GUI application sends commands to Arduino to adjust the RGB LED light color and intensity dynamically.
  
  **Sensors Integration**: Arduino interfaces with the BME280 sensor to collect real-time temperature, humidity, and pressure data from the environment.
  
  **Responsive Climate Control**: Arduino responds to commands from the GUI to control air conditioning settings. Users can turn the AC on or off, adjust fan speeds, and manage temperature settings.

## License

This project is released under the **MIT License**, a permissive open-source license that allows you to use, modify, and distribute this software. For complete details, please refer to the [LICENSE.txt](LICENSE.txt) file included in this repository.

For comprehensive instructions on using each component of this system, please consult the relevant code files available in this repository.

Thank you for choosing the Smart Home Automation System! I hope this project enhances the comfort and convenience of your smart home.
