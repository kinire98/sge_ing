cadena = input("Introduce la cadena para verificar si es un palindromo: ").lower()
print(f"Es palindromo: {"Si" if cadena == cadena[::-1] else "No"}")
