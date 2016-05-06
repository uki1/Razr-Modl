
#include "hx7.h"

Hx711 scale(A5, A4);

void setup() {

  Serial.begin(9600);

}

void loop() {
  long mas=0;
  mas = scale.getGram();
  Serial.print(mas/1.63, 1);//1,59 magic k for grad sensor value to gramm
}


