// connect led & water level sensor to aurduino
#define ledPin 6
#define sensorPin A0
void setup() {
  

  Serial.begin(9600);//use 9600 baud to print output
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);


}

void loop() {
  
 
  int sensorValue = analogRead(sensorPin);
  if (sensorValue > 100)  {
    int outputValue = map(sensorValue, 100, 800, 0, 255); // use map function to glow led based on amount of water present in soil
    Serial.println(outputValue);
    analogWrite(ledPin, outputValue); // generate PWM signal
  
}

}