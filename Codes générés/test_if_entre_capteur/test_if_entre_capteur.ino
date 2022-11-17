#define POT A0
int POT_value = 0;
#define POT1 A1
int POT1_value = 0;

void setup()
{

}
void loop()
{
POT_value = analogRead(POT);
POT1_value = analogRead(POT1);
if (POT_value == POT1_value) {

}

}