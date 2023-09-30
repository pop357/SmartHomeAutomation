int kRedPin = 9;    
int kGreenPin = 10;  
int kBluePin = 11;   

int lRedPin = 3;   
int lGreenPin = 5; 
int lBluePin = 6;   

#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; 
unsigned long previousMillis = 0;  
const unsigned long interval = 5000;

String inputString = "";         
boolean stringComplete = false; 

void setup() {
  Serial.begin(9600);           
  pinMode(kRedPin, OUTPUT);     
  pinMode(kGreenPin, OUTPUT);    
  pinMode(kBluePin, OUTPUT);     
  pinMode(lRedPin, OUTPUT);      
  pinMode(lGreenPin, OUTPUT);    
  pinMode(lBluePin, OUTPUT);     

  if (!bme.begin(0x76)) { 
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void loop() {
  
  
  if (stringComplete) 
   {

    
    if (inputString.startsWith("analogWrite")) {
      // Parsiraj komandu kako bi dobio vrijednosti pina i intenziteta
      int spaceIndex = inputString.indexOf(' ');
      int pin = inputString.substring(spaceIndex + 1, inputString.indexOf(' ', spaceIndex + 1)).toInt();
      int intensity = inputString.substring(inputString.lastIndexOf(' ') + 1).toInt();
     
      analogWrite(pin, intensity);
    }
    else if (inputString.startsWith("LightOn")) {
     
      
      
      analogWrite(lRedPin, 0);  
      analogWrite(lGreenPin, 0);
      analogWrite(lBluePin, 0); 
    } else if (inputString.startsWith("LightOff")) {
      //Serial.println("Isklj");
      
      
      analogWrite(lRedPin, 255);  
      analogWrite(lGreenPin, 255);
      analogWrite(lBluePin, 255);
    } else if (inputString.startsWith("l")) {
      
      
      int redVal, greenVal, blueVal;
      int comma1 = inputString.indexOf(',');
      int comma2 = inputString.indexOf(',', comma1 + 1);
      redVal = inputString.substring(1, comma1).toInt();
      greenVal = inputString.substring(comma1+1, comma2).toInt();
      blueVal = inputString.substring(comma2+1).toInt();
     
      analogWrite(lRedPin, 255 - redVal);   
      analogWrite(lGreenPin, 255 - greenVal);
      analogWrite(lBluePin,   255 - blueVal);
      Serial.println("Klima crveni: "+String(redVal)+" zeleni "+String(greenVal)+" plavi "+String(blueVal));
    } else if (inputString.startsWith("acOn") ){
      analogWrite(kRedPin,0);
      analogWrite(kGreenPin, 0);
      analogWrite(kBluePin,0);
    } else if(inputString.startsWith("acOff")){
      analogWrite(kRedPin,255);
      analogWrite(kGreenPin,255);
      analogWrite(kBluePin,255);
    }

    
    inputString = "";
    stringComplete = false;
  }

  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    
    float temperature = bme.readTemperature(); 
    float humidity = bme.readHumidity(); 
    float pressure = bme.readPressure() / 100.0F; 

    
    Serial.print("Temperature = ");
    Serial.print(temperature);
    Serial.println(" *C");

    Serial.print("Humidity = ");
    Serial.print(humidity);
    Serial.println(" %");

    Serial.print("Pressure = ");
    Serial.print(pressure);
    Serial.println(" hPa");



    previousMillis = currentMillis;
  
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

