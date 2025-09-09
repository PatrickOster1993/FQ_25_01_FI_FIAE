# Aufgabe 12

import random

two_dim_list = []

for x in range(0, 4):
    one_dim_list = []
    for y in range(0, 4):
        random_number = random.randint(1, 9)
        one_dim_list.append(random_number)
    two_dim_list.append(one_dim_list)

print(two_dim_list)

# 1
for liste in two_dim_list:
    for element in liste:
        print(element, end=" ")
    print()

# 2
summe = 0
for liste in two_dim_list:
    for element in liste:
        summe += element

print("Summe aller Elemente:", summe)

# 3
max_number = 1
indizes = []

for liste in two_dim_list:
    for element in liste:
        if element > max_number:
            max_number = element

for m in range(0, 4):
    for n in range(0, 4):
        aktueller_wert = two_dim_list[m][n]
        if aktueller_wert == max_number:
            indizes.append((m, n))

print("MAX-WERT:", max_number)
print("Indizes für MAX-WERT:", indizes)


