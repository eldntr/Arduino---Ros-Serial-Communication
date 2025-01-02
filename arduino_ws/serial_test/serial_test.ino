void setup() {
  Serial.begin(9600);
}

void loop() {
  // If data is available to read
  if (Serial.available()) {
    // Read the incoming string
    String received = Serial.readStringUntil('\n');
    
    // Echo back with prefix
    Serial.print("Arduino received: ");
    Serial.println(received);
  }
}
