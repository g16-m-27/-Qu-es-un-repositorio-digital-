def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def sort_row(matrix, row_index):
    if 0 <= row_index < len(matrix):
        print("Matriz original:")
        for row in matrix:
            print(row)

        # Ordenar la fila específica
        matrix[row_index] = quicksort(matrix[row_index])

        print("\nMatriz con la fila ordenada:")
        for row in matrix:
            print(row)
    else:
        print("Índice de fila fuera de rango.")


# Matriz bidimensional de ejemplo
matriz = [
    [9, 3, 7],
    [4, 1, 8],
    [6, 5, 2]
]

# Ordenar la fila 1 (segunda fila, índice 1)
sort_row(matriz, 1)
