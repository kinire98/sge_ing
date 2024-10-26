string1 = input("Introduce una cadena: ")
string2 = input("Introduce una segunda cadena: ")

string1_ord = 0
string2_ord = 0

for i in string1:
    string1_ord += ord(i)
for i in string2:
    string2_ord += ord(i)

if string1_ord > string2_ord:
    print("La primera cadena tiene un mayor valor total")
elif string1_ord < string2_ord:
    print("La segunda cadena tiene un mayor valor total")
else:
    print("Las dos cadenas tienen el mismo valor")
