# Solicitar al usuario que ingrese una frase
frase = input("Por favor, ingrese una frase: ")

#Inicializar variables
contador_vocales = 0
vocales_encontradas = []

#Definir la vocales
vocales ="aeiouAEIOUáéíóúÁÉÍÓÚ"

#Recorrer cada letra de la frase
for letra in frase:
    if letra in vocales:
        contador_vocales += 1
        vocales_encontradas.append(letra)

#Mostrar resultados
print(f"Cantidad de vocales: {contador_vocales}")
print(f"Vocales encontradas: {vocales_encontradas}")