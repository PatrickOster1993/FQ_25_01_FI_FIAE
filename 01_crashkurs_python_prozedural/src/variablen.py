# Variable vs Konstante
## keine Konstanten in Python!
## ABER: Konvention - "Konstanten" werden immer groß geschrieben

PI = 3.14
MY_CONSTANT = "sldfjslkdfj"
SHH_KEY = "asfjwqorjofjlisjflsajf"

# Numerisch
## Dezimalsystem
x = 10
print(type(x))
print("x:", x)

y = 1_000_000_000
print("y:", y)

z = x + y

print("Summe:", z)

## Binär
print("x(bin):", bin(x))

## Hexadezimal
print("x(hex):", hex(x))

## Octal
print("x(oct):", oct(x))

# String:

vorname = "Patrick"
nachname = "Oster"

print(type(vorname))

print(vorname + " " + nachname)
print(vorname, nachname)

x2 = str(x)
x3 = int(x2)
print("type(x):", type(x), "type(x2):", type(x2))
print("type(x3):", type(x3))

# Bool
wahre_aussage = True
falsche_aussage = False

print(type(wahre_aussage))

# None

none_datentyp = None

print(type(none_datentyp))

# ID
a = 10
b = 12

print(id(a), id(b))
print(id(a) - id(b))

# # Achtung vor Referenzen!
# c = b
# b += 5

# c += b

# print(c, b)

# Freie Variablenbezeichnung in Python:
meine_23423_variable = 100
print(meine_23423_variable)

我是一个人 = "Ich bin ein Mensch!"
print(我是一个人)

