cadena = input("Introduce una cadena: ")
consonantes = 0
vocales = 0
def is_vowel(char: str) -> bool :
    char = char.lower()
    if (char == 'a'):
        return True
    if (char == 'e'):
        return True
    if (char == 'i'):
        return True
    if (char == 'o'):
        return True
    if (char == 'u'):
        return True
    return False


for c in cadena:
    if (not c.isalpha()):
        continue
    if (is_vowel(c)):
        vocales += 1
        continue
    consonantes += 1


print(f'Numero de consonantes: {consonantes}')
print(f'Numero de vocales: {vocales}')
