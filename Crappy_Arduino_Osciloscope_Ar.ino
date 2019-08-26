
int sensorpin = A0;

void setup() {
  Serial.begin(115200);
}

void loop(){
  float sensorValue= analogRead(sensorpin);
  byte data= Serial.read();
  if (data== 's') {
    Serial.println(sensorValue);
    delay(10);
  }
}
