primera_cadena = input("Introduce la primera cadena: ")
segunda_cadena = input("Introduce la segunda cadena: ")
def anagrama(str1: str, str2: str) -> bool:
    if (len(str1) != len(str2)):
        return False
    return str1.lower().split().sort() == str2.lower().split().sort()
print(f'Son anagramas: {'Si' if anagrama(primera_cadena, segunda_cadena) else 'No'}')
