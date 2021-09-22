// simpleWrite.ino
long ii = 0;

void setup() {
  // initialize serial communications at 9600 bps:
  Serial.begin(9600);
}

void loop() {
  Serial.println(ii);
  ii++;
}
