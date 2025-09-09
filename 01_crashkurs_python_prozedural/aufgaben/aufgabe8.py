# Aufgabe 8

# Liste mit 5 beliebigen Obstsorten:
fruits = ["Apfel", "Birne", "Banane", "Orange", "Ananas"]
print(fruits)

# 1. Kiwi hinzufügen
fruits.append("Kiwi")
print(fruits)

# 2. Mango an 2. Stelle einfügen
fruits.insert(1, "Mango") # Listen beginnen bei 0 -> 2. Stelle = Index 1!
print(fruits)

# 3. Letztes Element entfernen
fruits.pop()
print(fruits)

# 4. Banane in Liste? Enternen!
if "Banane" in fruits:
    print("Banane in Liste gefunden!")
    fruits.remove("Banane")
print(fruits)

# 5. Liste umdrehen
fruits.reverse()
print(fruits)

# 6. Länge ausgeben
print("Länge der Liste:", len(fruits))

# 7. Kopie erstellen
## Flache Kopie:
fruits_flach = fruits
fruits_tief = fruits.copy()

print(f"fruits: {id(fruits)} | fruits_flach: {id(fruits_flach)} | fruits_tief: {id(fruits_tief)}")