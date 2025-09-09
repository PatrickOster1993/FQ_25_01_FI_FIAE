# Aufgabe 9

# 1. Liste erstellen
temperaturen = [15, 18, 20, 22, 17, 19, 21]

# 2. Durchschnittstemperatur berechnen
## Beste Variante (ohne sekundäre library):
durchschnitt_best = sum(temperaturen) / len(temperaturen)
print("Durchschnittstemperatur:", durchschnitt_best, "°C")

## Manuelle Weg (über Schleife)
sum_temp = 0
anz_temp = 0

for temperatur in temperaturen:
    anz_temp += 1
    sum_temp += temperatur

durchschnitt_manuell = sum_temp / anz_temp
print("Durchschnittstemperatur (manuell):", durchschnitt_manuell, "°C")

# 3. max-min-Temperatur:
min_temp = min(temperaturen)
max_temp = max(temperaturen)

print(f"Min-Temperatur: {min_temp}°C | Max-Temperatur: {max_temp}°C")

## manuell:
def my_min_max(liste):
    i = 1
    max_wert = liste[0]
    min_wert = liste[0]

    while i < len(liste):
        aktueller = liste[i]

        if aktueller > max_wert:
            max_wert = aktueller
        
        elif aktueller < min_wert:
            min_wert = aktueller

        i += 1
    return {
        "min": min_wert,
        "max": max_wert
    }

min_max = my_min_max(temperaturen)
min_wert = min_max["min"]
max_wert = min_max["max"]

print(f"Min-Temperatur: {min_wert}°C | Max-Temperatur: {max_wert}°C")

# 4. Temperaturen unter 18 °C mit 18 °C ersetzen!

for i in range(0, len(temperaturen)):
    if temperaturen[i] < 18:
        temperaturen[i] = 18

print(temperaturen)

# 5. Temperaturen tauschen:
erstes = temperaturen[0]
letztes = temperaturen[-1]

temperaturen[0] = letztes
temperaturen[-1] = erstes

print(temperaturen)
