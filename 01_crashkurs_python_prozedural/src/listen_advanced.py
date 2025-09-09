# In Python gibt's auch noch weitere "spezielle" Listen und andere komplexere Datentypen.
## Liste: [] // Dict ODER Set: {} // Tupel: ()
## 1. Dictionaries:
person = {
    "name": {
        "vorname": "Patrick",
        "nachname": "Oster"
    },
    "alter": 22 + 10,
    "hobbys": ["Fußball", "Kino", "Programmieren"],
    "verheiratet": False,
}
print("### Dictionaries ###")
print(person)
print("Alter:", person["alter"])
print("Vorname:", person["name"]["vorname"])
print("1. Hobby:", person["hobbys"][0])

## 2 Tupel
mein_tupel = (5, 7, 9) # Tupel = unveränderliche Liste
print("### Tupel ###")
print(mein_tupel)
print("1. Element:", mein_tupel[0])

try:
    mein_tupel[0] = 6
except Exception as e:
    print("Fehler:", e)

### Merke: Möchte man eine Liste, bei der man einzelne Elemente nicht verändern möchte, dann Tupel!!!

## 3 Set:
print("### Set ###")
mein_set = {3, 2, 1}
print(mein_set)

mein_set.add(4)
mein_set.add(5)
mein_set.add(1)
print(mein_set)
