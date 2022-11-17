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

class Module:
    def __init__(self, nom, pin="N/A", type="digital"):
        self.nom = nom
        self.pin = pin
        self.type = type

arduino = []