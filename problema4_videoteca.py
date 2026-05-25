# Problema 4 - Videoteca Digital

# Matriz con información de los títulos
# [Título, Año, Calificación, Género]

videoteca = [
    ["Avatar", 2022, 9, "Ciencia Ficción"],
    ["Titanic", 1997, 8, "Drama"],
    ["Mario Bros", 2023, 9, "Animación"],
    ["Joker", 2019, 8, "Suspenso"],
    ["Barbie", 2023, 7, "Comedia"],
    ["Oppenheimer", 2023, 10, "Drama"],
    ["Avengers Endgame", 2019, 9, "Acción"]
]

# Función para contar títulos que cumplen los criterios
def contar_titulos(matriz, calificacion_minima, anio_limite):
    contador = 0

    for titulo in matriz:
        if titulo[2] >= calificacion_minima and titulo[1] >= anio_limite:
            contador += 1

    return contador

# Datos de búsqueda
calificacion_minima = 8
anio_limite = 2020

# Llamado de la función
resultado = contar_titulos(videoteca, calificacion_minima, anio_limite)

# Mostrar resultado
print("Cantidad de títulos que cumplen los criterios:", resultado)
