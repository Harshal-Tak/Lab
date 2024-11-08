void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Input any number: ");
}

void loop() {
  // put your main code here, to run repeatedly:
  int input = Serial.parseInt();
  int squaredInput = sq(input);
  Serial.println(int(squaredInput));

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
*/
