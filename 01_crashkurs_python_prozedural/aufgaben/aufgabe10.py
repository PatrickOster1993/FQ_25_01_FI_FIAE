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

# 2
## A
avg = sum(kurse) / len(kurse)
print(f"Durchschnittlicher Kurs: {avg} €")

## B
max_kurs = max(kurse)
min_kurs = min(kurse)
print(f"Min-Kurs: {min_kurs} € | Max-Kurs: {max_kurs} €")

## C
def rise_or_fall_count(rise = True):
    tage_veraendert = 0
    for i in range(1, anz_kurse):
        vorher = kurse[i - 1]
        jetzt = kurse[i]
        if rise and jetzt > vorher:
            tage_veraendert += 1
        elif not rise and jetzt < vorher:
            tage_veraendert += 1
    return tage_veraendert
    
print(f"Anzahl Tage, an denen Kurs gestiegen: {rise_or_fall_count()}")

## D
### DRY: Don't Repeat Yourself!!!
print(f"Anzahl Tage, an denen Kurs gefallen: {rise_or_fall_count(False)}")

# 3 Tag, an dem Kurs am höchsten gestiegen:

max_differenz = 0
max_tag = ""

for i in range(1, anz_kurse):
    differenz = kurse[i] - kurse[i - 1]
    if differenz > max_differenz:
        max_differenz = differenz
        max_tag = f"Kurs von Tag {i} auf Tag {i + 1} am stärksten gestiegen!"

print(max_tag)

# 4
performance = round(((kurse[-1] - kurse[0]) / kurse[0]) * 100, 2)
fall_or_rise = "gestiegen" if performance >= 0 else "gefallen"

print(f"Kurs ist über den Monat hinweg um {abs(performance)} % {fall_or_rise}!")

