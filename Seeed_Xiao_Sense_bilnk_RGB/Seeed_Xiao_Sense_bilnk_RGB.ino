
void setup() {

  // initialize serial.
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Serial Started");
  
  // Pins for the built-in RGB LEDs on the Arduino Nano 33 BLE Sense
  pinMode(LEDR, OUTPUT);
  pinMode(LEDG, OUTPUT);
  pinMode(LEDB, OUTPUT);

  // Note: The RGB LEDs are ON when the pin is LOW and off when HIGH.
  digitalWrite(LEDR, HIGH);
  digitalWrite(LEDG, HIGH);
  digitalWrite(LEDB, HIGH);
  
}

void loop() {
  digitalWrite(LEDR, LOW); 
  Serial.println("LED RED ON");
  delay(1000);              
  digitalWrite(LEDR, HIGH);    
  Serial.println("LED RED OFF");
  delay(1000);     

  digitalWrite(LEDG, LOW); 
  Serial.println("LED GREEN ON"); 
  delay(1000);              
  digitalWrite(LEDG, HIGH);  
  Serial.println("LED GREEN OFF");  
  delay(1000);  

  digitalWrite(LEDB, LOW); 
  Serial.println("LED BLUE ON");  
  delay(1000);     
  digitalWrite(LEDB, HIGH);   
  Serial.println("LED BLUE OFF");   
  delay(1000);  
}
