# Rückblick: Bool'sche Variablen:

# Simples if-else-statement:
wahrheitswert = True

if wahrheitswert:
    print("Bedingung erfüllt!")
else:
    print("Bedingung NICHT efüllt!")

# vereinfachte Variante für simples if-else-statement
inverse_aussage = "Bedingung erfüllt!" if not wahrheitswert else "Bedingung NICHT efüllt!"

## Analog in anderen höheren Programmiersprachen (Ternärer Operator):
# inverse_aussage = wahrheitswert ? "Bedingung erfüllt!" : "Bedingung NICHT erfüllt!"

print(inverse_aussage)

print("############")
# Erweitertes if-else-statement:
wahrheitswert = True
eine_zahl = -10

if wahrheitswert and eine_zahl > 0:
    print("Bedingung erfüllt!")

elif wahrheitswert or eine_zahl > 0:
    print("Bedingung auch irgendwie erfüllt!")

else:
    print("Bedingung NICHT efüllt!")

# Verschiedene Operatoren für Bedingungen:
if eine_zahl == 1:
    print("Zahl ist genau 1!")
elif eine_zahl >= 1:
    print("Zahl ist größer oder gleich 1!")
else:
    print("Keine der obigen Bedingungen ist wahr!")