# Aufgabe 10

# 1. Liste mit 20 zufälligen Kursen zwischen 75 - 150 € erstellen
import random

kurse = []

anz_kurse = 20

untergrenze = 75
obergrenze = 150

for i in range(0, anz_kurse):
    kurs = random.randint(untergrenze, obergrenze)
    kurse.append(kurs)

print(kurse)