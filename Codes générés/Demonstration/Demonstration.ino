#define LED1 1
#define LED2 2
#define BP1 3
int BP1_value = 0;
#define BP2 4
int BP2_value = 0;

void setup()
{
	pinMode(LED1, OUTPUT);
	pinMode(LED2, OUTPUT);
	pinMode(BP1, INPUT_PULLUP);
	pinMode(BP2, INPUT_PULLUP);
}
void loop()
{
BP1_value = digitalRead(BP1);
if (BP1_value == 0) {
digitalWrite(LED1, HIGH);

}
BP2_value = digitalRead(BP2);
if (BP2_value == 0) {
digitalWrite(LED2, HIGH);

}

}digitalWrite(LED1, LOW);

digitalWrite(LED2, LOW);

