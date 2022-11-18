#define POT A0
int POT_value = 0;
#define LED 5

void setup()
{
	pinMode(LED, OUTPUT);
}
void loop()
{
POT_value = analogRead(POT);
if (POT_value == 500) {
digitalWrite(LED, HIGH);

}

}