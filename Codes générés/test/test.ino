#define LED 8
#define BP 6
int BP_value = 0;

void setup()
{
	pinMode(LED, OUTPUT);
	pinMode(BP, INPUT_PULLUP);
}
void loop()
{
BP_value = digitalRead(BP);
if (BP_value == 0) {
digitalWrite(LED, HIGH);

}

}