# Aufgabe 10

# 1. Liste mit 20 zufälligen Kursen zwischen 75 - 150 € erstellen
import random

kurse = []

anz_kurse = 20

untergrenze = 75
obergrenze = 150

for i in range(0, anz_kurse):
    kurs = random.randint(untergrenze, obergrenze)
    kurse.append(kurs)

print(kurse)

# 2. Ausgabe berechnen:

## A. Den durchschnittlichen Aktienkurs des Monats.

### medium Rare Murat
print(sum(kurse)/len(kurse))

## B. Den höchsten und niedrigsten Kurs.

def print_extrama():
    print("Max:", max(kurse))
    print("Min:", min(kurse))
print_extrama()

## C. Die Anzahl der Tage, an denen der Kurs gestiegen ist.

def count_previous_element_is_bigger(elements):
    
    count_of_elements_that_are_bigger = 0
    
    for i in range(1, len(elements)):
        if elements[i] > elements[i-1]:
            count_of_elements_that_are_bigger += 1;
            
    return count_of_elements_that_are_bigger;

print("Tage an denen der Kurs gestiegen ist:", count_previous_element_is_bigger(kurse))

## D. Die Anzahl der Tage, an denen der Kurs gefallen ist

def count_previous_element_is_smaller(elements):
    
    count_of_elements_that_are_smaller = 0
    
    for i in range(1, len(elements)):
        if elements[i] < elements[i-1]:
            count_of_elements_that_are_smaller += 1;
            
    return count_of_elements_that_are_smaller;

print("Tage an denen der Kurs gefallen ist:", count_previous_element_is_smaller(kurse))