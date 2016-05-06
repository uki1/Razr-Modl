
void setup() {

  Serial.begin(9600);

}

void loop() {

  sens(97.7, 10);
  
  sens(9860, 6);

  sens(97800, 8);

  sens(9460000, 12);

  sens(974, 4);

  sens(972000, 2);

}

void sens(float resist, int port){
  pinMode(port, OUTPUT);
  digitalWrite(port, HIGH);

  delay(1);

  float sum = 0;
  int tim = 10;

  for (byte i = 0; i < tim; i++)
  {
    delay(1);
    sum += analogRead(A0);
  }


  float sensorValue = sum / float(tim);
  float R = resist / ((5.0 / ((5.0 / 1023.0) * sensorValue)) - 1);



  if (sensorValue>512){
    sensorValue = sensorValue -(2*(sensorValue-512));
  }
  
  Serial.print(R);  
  Serial.print(";");
  Serial.println(sensorValue);  

  digitalWrite(port, LOW);
  pinMode(port, INPUT);
  delay(1);
}
