# Ejercicios de sets: catering del club de cocina

ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    """
    Elimina los ingredientes duplicados de una receta.

    Args:
        nombre_plato: String con el nombre del plato
        ingredientes: Lista de ingredientes (puede contener duplicados)

    Returns:
        Una tupla (nombre_plato, set_de_ingredientes_sin_duplicados)
    """

    set_de_ingredientes_sin_duplicados = set()
    for i in ingredientes:
        if i not in set_de_ingredientes_sin_duplicados:
            set_de_ingredientes_sin_duplicados.add(i)

    return (nombre_plato, set_de_ingredientes_sin_duplicados)

def check_drinks(nombre_bebida, ingredientes):
    """
    Clasifica una bebida como "Cocktail" (contiene alcohol) o "Mocktail"
    (no contiene alcohol) basándose en sus ingredientes.

    Los ingredientes alcohólicos válidos están definidos en el set ALCOHOLS.

    Args:
        nombre_bebida: String con el nombre de la bebida
        ingredientes: Lista de ingredientes de la bebida

    Returns:
        String con el nombre de la bebida seguido de "Cocktail" o "Mocktail"
    """

    clasificacion = "Mocktail"

    for ingrediente in ingredientes:
        if ingrediente in ALCOHOLS:
            clasificacion = "Cocktail"

    return f"{nombre_bebida} {clasificacion}"
    pass  # Reemplazar con tu implementación


def unique_chars(texto):
    """
    Retorna un set con los caracteres únicos de un string.

    Args:
        texto: Un string

    Returns:
        Un set con los caracteres únicos del texto

    Ejemplo:
        unique_chars("hello") -> {'h', 'e', 'l', 'o'}
    """

    set_unicos = set()

    for caracter in texto:
        if caracter not in set_unicos:
            set_unicos.add(caracter)

    return set_unicos

def sum_set(numeros):
    """
    Recorre un set de números y retorna la suma total.
    Si el set está vacío, retorna 0.

    No se permite usar la función built-in sum(). Implementar la suma
    recorriendo el set con un for (o while).

    Args:
        numeros: Set de números (enteros o flotantes)

    Returns:
        La suma de todos los elementos del set

    Ejemplo:
        sum_set({1, 2, 3, 4}) -> 10
        sum_set(set()) -> 0
    """

    if len(numeros) == 0:
        return 0
    else:
        suma = 0
        for numero in numeros:
            suma += numero
        return suma

def common_elements(set_a, set_b):
    """
    Retorna un nuevo set con los elementos que aparecen en AMBOS sets.

    No se permite usar el operador & ni el método .intersection().
    Implementar la intersección recorriendo uno de los sets y
    verificando pertenencia en el otro.

    Args:
        set_a: Primer set
        set_b: Segundo set

    Returns:
        Set con los elementos presentes en ambos

    Ejemplo:
        common_elements({1, 2, 3}, {2, 3, 4}) -> {2, 3}
        common_elements({1, 2}, {3, 4}) -> set()
    """

    elements_in_common = set()

    for element in set_a:
        if element in set_b:
            elements_in_common.add(element)

    return elements_in_common