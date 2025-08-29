# Definimos la matriz 3x3
matriz = [
    [5, 8, 3],
    [1, 7, 9],
    [4, 6, 2]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorremos las filas
        for j in range(len(matriz[i])):  # Recorremos las columnas
            if matriz[i][j] == valor:
                return f"El valor {valor} fue encontrado en la posición ({i}, {j})."
    return f"El valor {valor} no se encuentra en la matriz."

# Valor a buscar
valor_a_buscar = 7

# Llamamos a la función y mostramos el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)
