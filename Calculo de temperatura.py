import random

# Definicion de las dimensiones
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas

# Matriz
# Cada celda contiene la temperatura de ese día
temperaturas = []

for ciudad in ciudades:
    ciudad_temperaturas = []
    for semana in range(semanas):
        semana_temperaturas = []
        for dia in range(len(dias_semana)):
            # temperatura aleatoria entre 15 y 35 grados
            semana_temperaturas.append(random.randint(15, 35))
        ciudad_temperaturas.append(semana_temperaturas)
    temperaturas.append(ciudad_temperaturas)

# promedio por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedios de temperatura en {ciudad}:")
    for j in range(semanas):
        suma = 0
        for k in range(len(dias_semana)):
            suma += temperaturas[i][j][k]
        promedio = suma / len(dias_semana)
        print(f"  Semana {j+1}: {promedio:.2f} °C")
