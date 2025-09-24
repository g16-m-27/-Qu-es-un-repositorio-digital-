# 1. Crear el diccionario con datos ficticios
informacion_personal = {
    "Nombre": "Zhune Zuleyka",
    "Edad": 19,
    "Ciudad": "Santa Rosa",
    "Profesion": "Ingeniera en sistemas"
}

# 2. Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Machala"

# 3. Agregar una nueva clave-valor para la profesión
informacion_personal["profesion"] = "Ingeniera"

# 4. Verificar si existe la clave "telefono" y, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0992208372"

# 5. Eliminar la clave "edad"
del informacion_personal["edad"]

# 6.Diccionario final
print(informacion_personal)
