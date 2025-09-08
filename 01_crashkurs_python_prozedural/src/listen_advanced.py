# In Python gibt's auch noch weitere "spezielle" Listen und andere komplexere Datentypen.

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

print(person)
print("Alter:", person["alter"])
print("Vorname:", person["name"]["vorname"])
print("1. Hobby:", person["hobbys"][0])
