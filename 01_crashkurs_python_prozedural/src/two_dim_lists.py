one_dim_list = [
    1, 
    6, 
    99, 
    5, 
    2
]

two_dim_list = [
    [1, 6, 9, 3, 4],
    [1, 1, 9, 5, 4], 
    [0, 6, 0, 3, 4]
]

print(two_dim_list)
print(two_dim_list[0])
print(two_dim_list[0][2])

print("### 2-dim-Listen mit Schleifen ###")
for liste in two_dim_list:
    for i in range(0, len(liste)):
        custom_end = "" if i == len(liste) - 1 else "-"
        print(liste[i], end=custom_end)
    print()

