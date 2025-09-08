# Listen = Arrays in Python (analog zu anderen Programmiersprachen)!
## numpy-Arrays sind eine Eigenheit und nicht mit den klassischen Arrays gleichzusetzen!

a = [1, 2, 3, 4, 5]
print(type(a), a)

b = ["Hallo", " ", "Welt!"]
print(b)

# Listen können sich auch aus verschiedenen Datentypen zusammensetzen!
c = [10, "hey!", 3.14, False]
print(c)

## Elemente zur Liste hinzufügen:
c.append(11)
print(c)

## Auf ein einzelnes Element der Liste über Index zugreifen:
print(c[0]) # --> das 1. Element ist dasjenige mit dem Index 0!!!

## Auf das letzte Element der Liste über Index zugreifen:
print(c[-1])

## Logik zieht sich durch -> auf vorletztes Element zugreifen:
print(c[-2])

## Anzahl der Elemente in Liste bestimmen:
print(len(c))

## ID / Adressen

print("####### ID / Adressen #######")

x = 1
y = 2
print(id(y) - id(x))

print(id(b), id(a))


x = [5, 6, 3, 1]
y = x # Flache Kopie!

print(x)
print(y)

y.append(0)
print(x)
print(y)
print(id(x), id(y))

# wenn ich nur gleiche Werte haben möchte, nicht aber die "Call by Reference"-Abhängigkeit,
# dann benötige ich eine sog. "Tiefe Kopie"...
m = [0, 1, 2, 3, 4]
n = m.copy() # Erzeugen einer Tiefen Kopie!
print(m)
print(n)
print(id(m), id(n))

n.append(5)
m.append(5)

print(m)
print(n)

# Unterscheidung von gewissen Operatoren in Python:
print(x == y, x is y)
print(m == n, m is n)

# in Operator
print(3 in x) # überprüfen, ob Wert in Liste

# Schleifen
print("###### Schleifen #######")

i = 0

while i < len(c):
    print(c[i])
    i += 1

## rückwärts
print("*** rückwärts ***")

i = len(c) - 1

while i >= 0:
    print(c[i])
    i -= 1

print("'b' vor Schleife:", b)

while len(b) > 0:
    b.pop()
    print(b)

print("'b' nach Schleife:", b)


# for-Schleife:

for i in range(0, len(c)):
    print(f"Index-{i}: Wert-{c[i]}")

# kompakt (für die meisten Use-Cases):

for wert in c:
    print(wert)

# Sonstiges Basiswissen bzgl. Listen / Schleifen
print(c)

c.pop() # entferne letztes Element der Liste
print(c)

c.insert(0, 3.14)
print(c)

c.remove(3.14)
print(c)

c.reverse()
print(c)

c_teil = c[1:3]
print(c_teil)




