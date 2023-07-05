int redPin = 9;    // Red LED pin
int greenPin = 10;  // Green LED pin
int bluePin = 11;   // Blue LED pin

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(9600);           // initialize serial communication
  pinMode(redPin, OUTPUT);      // set redPin as OUTPUT
  pinMode(greenPin, OUTPUT);    // set greenPin as OUTPUT
  pinMode(bluePin, OUTPUT);     // set bluePin as OUTPUT
}

void loop() {
  // send data only when you receive data:
  if (stringComplete) {
    if (inputString == "1") {
      // Turn on LED
      analogWrite(redPin, 255);  
      analogWrite(greenPin, 255);
      analogWrite(bluePin, 255); 
    } else if (inputString == "0") {
      // Turn off LED
      analogWrite(redPin, 0);  
      analogWrite(greenPin, 0);
      analogWrite(bluePin, 0);
    } else {
      // Set LED color
      int redVal, greenVal, blueVal;
      int comma1 = inputString.indexOf(',');
      int comma2 = inputString.indexOf(',', comma1 + 1);
      redVal = inputString.substring(0, comma1).toInt();
      greenVal = inputString.substring(comma1+1, comma2).toInt();
      blueVal = inputString.substring(comma2+1).toInt();
      analogWrite(redPin, 255 - redVal);  
      analogWrite(greenPin, 255 - greenVal);
      analogWrite(bluePin, 255 - blueVal);
    }
    
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}