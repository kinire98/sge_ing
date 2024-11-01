def combinar_diccionarios(dict1: dict, dict2: dict) -> dict:
    dict_combinado = dict()
    for key, value in dict1.items():
        if dict2.get(key, 0) != 0:
            dict_combinado[key] = value + dict2.get(key)
            continue
        dict_combinado[key] = value
    for key, value in dict2.items():
        if dict1.get(key, 0) != 0:
            continue
        dict_combinado[key] = value
    return dict_combinado   

precios1 = {
        "Pera": 1,
        "Manzana": 3,
        "Kiwi": 7
}
precios2 = {
        "Manzana": 7,
        "Kiwi": 5,
        "Naranja": 8,
}
print(combinar_diccionarios(precios1, precios2))
