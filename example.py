def log_function_call(func):
    """
    Este decorador imprime el nombre de la función, sus argumentos
    y su valor de retorno cada vez que es llamada.
    """
    def wrapper(*args, **kwargs):
        print(f"Llamando a la función '{func.__name__}'...")
        print(f"Argumentos posicionales (args): {args}")
        print(f"Argumentos de palabra clave (kwargs): {kwargs}")
        
        # Llama a la función original y guarda el resultado
        result = func(*args, **kwargs)
        
        print(f"La función '{func.__name__}' devolvió: {result}")
        print("-" * 20)
        
        # Devuelve el resultado de la función original
        return result
    return wrapper

@log_function_call
def sumar(a, b, c=0):
    return a + b + c

@log_function_call
def saludar(nombre):
    return f"Hola, {nombre}"

# Probamos las funciones decoradas
sumar(1, 2)
sumar(5, 10, c=5)
saludar("Mundo")

"""
Cada vez que llamas a sumar() o saludar(), en realidad estás llamando a la función wrapper que las envuelve. 
Esta función wrapper se encarga de imprimir toda la información de diagnóstico antes y después de ejecutar el código original de sumar() o saludar().
"""
