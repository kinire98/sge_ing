productos = {
"Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
"Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
"Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
"Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
"Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}
num_categorias = 0
total_productos = 0
categorias = []
for key, value in productos.items():
    num_categorias += 1
    total_productos += len(value)
    categorias.append(f"{key}: {len(value)}")
print(f"Numero de categorias: {num_categorias}")
print(f"Total de productos: {total_productos}")
print("Total por categoria: ")
print("\n".join(categorias))
