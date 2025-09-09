def calcular_promedio_temperaturas(datos):
    """
    Calcula el promedio de temperaturas para cada ciudad y por semana.
    """
    resultados = {}

    for ciudad, semanas in datos.items():
        suma_total = 0
        cantidad_total = 0
        promedios_semanales = []

        for semana in semanas:
            suma_semana = sum(semana)
            promedio_semana = suma_semana / len(semana)
            promedios_semanales.append(round(promedio_semana, 2))

            suma_total += suma_semana
            cantidad_total += len(semana)

        promedio_general = suma_total / cantidad_total if cantidad_total > 0 else 0

        resultados[ciudad] = {
            "Promedio General": round(promedio_general, 2),
            "Promedios Semanales": promedios_semanales
        }

    return resultados

# 3 Ciudades por 4 semanas por 7 días
datos_temperaturas = {
    "Santa Rosa": [
        [27, 28, 29, 30, 28, 27, 29],  # Semana 1
        [28, 29, 30, 29, 28, 27, 28],  # Semana 2
        [29, 30, 28, 27, 29, 30, 28],  # Semana 3
        [28, 27, 29, 28, 30, 29, 28]  # Semana 4
    ],
    "Machala": [
        [29, 30, 31, 30, 29, 28, 30],  # Semana 1
        [30, 31, 29, 30, 31, 30, 29],  # Semana 2
        [31, 30, 29, 30, 31, 30, 29],  # Semana 3
        [30, 29, 31, 30, 29, 30, 31]  # Semana 4
    ],
    "Pasaje": [
        [26, 27, 28, 27, 26, 27, 28],  # Semana 1
        [27, 28, 27, 26, 27, 28, 27],  # Semana 2
        [28, 27, 26, 27, 28, 27, 26],  # Semana 3
        [27, 26, 27, 28, 27, 26, 27]  # Semana 4
    ]
}
resultado = calcular_promedio_temperaturas(datos_temperaturas)

# Resultado Final
for ciudad, valores in resultado.items():
    print(f"\nCiudad: {ciudad}")
    print(f"  Promedio General: {valores['Promedio General']}°C")
    for i, prom_sem in enumerate(valores["Promedios Semanales"], start=1):
        print(f"  Semana {i}: {prom_sem}°C")
