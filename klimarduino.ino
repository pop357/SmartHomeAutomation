int redPin = 9;
int greenPin = 10;
int bluePin = 11;

void setup() {
  // Initialize the pins as output
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  // Initialize the serial communication
  Serial.begin(9600);
}

void loop() {
  // Check if there is any serial data available
  if (Serial.available() > 0) {
    // Read the incoming serial data
    String command = Serial.readStringUntil('\n');

    // Perform the appropriate action based on the command
    if (command.startsWith("analogWrite")) {
      // Parse the command to get the pin and intensity values
      int spaceIndex = command.indexOf(' ');
      int pin = command.substring(spaceIndex + 1, command.indexOf(' ', spaceIndex + 1)).toInt();
      int intensity = command.substring(command.lastIndexOf(' ') + 1).toInt();

      // Set the analog output on the specified pin
      analogWrite(pin, intensity);
    }
  }
}
