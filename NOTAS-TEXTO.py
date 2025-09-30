# ---------- Archivo de Texto ----------

# El archivo en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Notas personales
archivo.write("Nota 1: Recordar llamar a mamá mañana.\n")
archivo.write("Nota 2: Comprar carne para la cena.\n")
archivo.write("Nota 3: Visitar a mi hermano y llevarle su comida favorita.\n")

# Cerrar el archivo
archivo.close()

# ---------- Lectura de Archivo de Texto ----------

# Abrir el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leer el archivo línea por línea
linea = archivo.readline()
while linea != "":
    # Mostrar cada línea en la consola
    print(linea.strip())  # strip() elimina saltos de línea extra
    linea = archivo.readline()

# Cerrar el archivo
archivo.close()

