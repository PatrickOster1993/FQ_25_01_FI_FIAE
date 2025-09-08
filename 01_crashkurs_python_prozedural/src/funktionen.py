def addiere(a, b):
    return a + b

# mit Optional-Parameter
# def addiere(a=1, b=2):
#     return a + b

ergebnis = addiere(1, 2)
print("Ergebnis:", ergebnis)

ergebnis_2 = addiere(a=2, b=3)
print("Ergebnis2:", ergebnis_2)

def verkette(vorne, hinten):
    verkettet = vorne + hinten
    return verkettet

verketteter_string = verkette("Welt!", "Hallo ")
print(verketteter_string)

verketteter_string_2 = verkette(
    hinten="Welt!",
    vorne="Hallo "
)

print(verketteter_string_2)

## Exkurs: Exception-Handling:
try:
    print("Wird immer ausgeführt, bis an Stelle, wo Fehler auftritt!")
    dozent = verkette("Dozent#", 1)
    print(dozent)
except Exception as e:
    print("Wird ausgeführt, wenn Fehler auftritt!")
    print("Fehler:", e)
else:
    print("Wird nach 'try' ausgeführt, wenn kein Fehler aufgetreten ist!")
finally:
    print("Wird immer zusätzlich am Ende ausgeführt - egal ob Fehler oder nicht!")