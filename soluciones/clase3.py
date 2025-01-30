"""
Ejercicio 3: Alcance de Variables y Contextos

Este ejercicio te ayudará a entender:
- Variables globales y locales
- Contextos de funciones
- Modificación de variables en diferentes contextos
- La palabra clave 'global'
- Ámbito de variables en funciones anidadas
"""

# Variable global de ejemplo
contador = 10

def doblar_contador():
    global contador
    contador = contador * 2
    return contador

def incrementar_contador():
    """
    TODO: Modifica esta función para que:
    1. Use la variable global 'contador'
    2. Incremente su valor en 1
    3. Retorne el nuevo valor
    
    Pista: Necesitarás usar la palabra clave 'global'
    """
    global contador
    doblar_contador()
    contador = contador + 1
    return contador

def crear_multiplicador(factor):
    """
    TODO: Completa esta función que:
    1. Recibe un factor como parámetro
    2. Define una función interna 'multiplicar' que multiplica un número por el factor
    3. Retorna la función interna
    
    Ejemplo de uso:
    duplicar = crear_multiplicador(2)
    duplicar(5) -> retorna 10
    """
    pass  # Reemplaza esto con tu código

def banco():
    """
    TODO: Completa esta función que demuestre el alcance de variables:
    1. Crea una variable 'total' con valor inicial 0
    2. Define una función interna 'agregar' que:
       - Recibe un número
       - Actualiza 'total' sumándole ese número
       - Retorna el nuevo total
    3. Retorna la función 'agregar'
    
    Ejemplo de uso:
    compras_luis = banco()
    sumador_pablo = banco()
    compras_luis(5) -> retorna 5
    sumador_pablo(3) -> retorna 3

    compras_luis(5) -> retorna 10
    compras_luis(3) -> retorna 13
    sumador_pablo(1) -> retorna 4
    sumas_de_jose = banco()
    sumas_de_jos(10) -> retorna 10
    compras_luis(5) -> retorna 15
    """
    total = 0
    def agregar(numero):
        nonlocal total
        total = total + numero
        return total
    
    return agregar
    
def main():
    # Prueba de incrementar_contador
    print(f"Contador inicial: {contador}")
    for _ in range(3):
        nuevo_valor = incrementar_contador()
        print(f"Nuevo valor del contador: {nuevo_valor}")
    
    # Prueba de crear_multiplicador
    #duplicar = crear_multiplicador(2)
    #triplicar = crear_multiplicador(3)
    #numero = 5
    #print(f"\nProbando multiplicadores con {numero}:")
    #print(f"Duplicar: {duplicar(numero)}")
    #print(f"Triplicar: {triplicar(numero)}")
    
    # Prueba de banco
    ahorrar = banco()
    print("\nProbando banco:")
    print(f"Agregar 5: {ahorrar(5)}")
    print(f"Agregar 3: {ahorrar(3)}")
    print(f"Agregar 2: {ahorrar(2)}")
    llevo_ahorrado_ahora = ahorrar(5)
    print(f"Llevo {llevo_ahorrado_ahora}, Agregar 10: {ahorrar(10)}")

if __name__ == "__main__":
    main()
