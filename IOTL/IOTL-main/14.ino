void setup()
{
  pinMode(4,OUTPUT);
  pinMode(9,INPUT);
  digitalWrite(4,HIGH);
}

void loop()
{
  if(digitalRead(9)==1)
  {
    digitalWrite(4,HIGH);
  }
  else
    digitalWrite(4,LOW);
}


/*void setup() {
  Serial.begin(9600);
  Serial.println("Input any number: ");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int input = Serial.parseInt();
    int squaredInput = sq(input);
    Serial.println(squaredInput);
  }
}
In t*/
