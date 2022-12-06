#define t 5

void setup()
{
	pinMode(t, OUTPUT);
}
void loop()
{
digitalWrite(t, HIGH);
delay(5000);
digitalWrite(t, LOW);
delay(5000);

}