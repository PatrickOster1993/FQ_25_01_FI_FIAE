# das ist ein einzeiliger Kommentar!

'''
Das ist
ein
mehrzeiliger Kommentar
'''

print("Hallo Welt!")
name = "Patrick"
print("Hallo " + name + "!") # Alter Weg
print(f"Hallo {name}!") # moderner Weg




# Wichtige Parameter der print()-Funktion:
## sep: Seperator zwischen 2 Variablen innerhalb einer print-Funktion
## end: Ende einer print-Funktion (Was soll nach dem print passieren!)
nachname = "Oster"

print(name, nachname, sep="*******")

print("Hallo", end= " ")
print("Welt!")

print("Hallo")
print()
print("Welt!")

# Bad Practice:
print("Hallo", end=" "); print("Welt!"); print()

# Input() mit Print() im Zusammenspiel:
name = input("Name: ")
print(f"Hallo {name}")


