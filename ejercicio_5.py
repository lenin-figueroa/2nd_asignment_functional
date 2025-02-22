def noDoble(cadena):
    if not cadena:  # Si la cadena está vacía, retornamos una cadena vacía.
        return ""
    
    resultado = []  # Lista para almacenar los caracteres del resultado.
    resultado.append(cadena[0])  # Agregamos el primer carácter a la lista de resultados.

    # Iteramos a través de la cadena, comenzando desde el segundo carácter.
    for i in range(1, len(cadena)):
        # Solo añadimos el carácter a resultado si es diferente al último carácter añadido.
        if cadena[i] != cadena[i - 1]:
            resultado.append(cadena[i])
    
    return ''.join(resultado)  # Unimos la lista en una cadena y la devolvemos.

# Ejemplo de uso
cadena_ejemplo = "abcccfabadeff"
resultado = noDoble(cadena_ejemplo)
print(resultado)  # Salida: "abcfabadef"