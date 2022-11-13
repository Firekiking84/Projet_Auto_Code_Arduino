"""
Objectif clignoter une led toutes les 5 secondes
Code Arduino voulu :
#define led 5

void setup()
{

    pinMode(led, OUTPUT);

}
void loop()
{
    digitalWrite(led, HIGH);
    delay(5000);
    digitalWrite(led, LOW);
    delay(5000);
}
"""

t1 = 0
t2 = 1
t3 = 2

if t1 == 0 and t2 == 1 or t3 == 2:
    print("Yesss")