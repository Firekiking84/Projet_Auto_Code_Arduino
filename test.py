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

file = open("test.txt", "r")
x = 0
for line in file:
    x += 1
    if line == "\n":
        print(f"Vide, ligne n°{x}")