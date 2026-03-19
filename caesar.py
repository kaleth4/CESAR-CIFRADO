# ============================================================
#   CAESAR CIPHER — Cifrado y Descifrado César
#   Autor: Kaleth Corcho | WolvesTI | 2026
# ============================================================
 
def cifrar_cesar(texto, desplazamiento):
    """
    Cifra un texto usando el algoritmo César.
    Respeta mayúsculas, minúsculas y caracteres especiales.
    
    Args:
        texto (str): Mensaje a cifrar
        desplazamiento (int): Número de posiciones a desplazar (clave)
    
    Returns:
        str: Texto cifrado
    """
    resultado = ""
    desplazamiento = desplazamiento % 26  # Normalizar clave
 
    for caracter in texto:
        if caracter.isalpha():
            # Determinar base ASCII según mayúscula o minúscula
            base = ord('A') if caracter.isupper() else ord('a')
            # Aplicar desplazamiento con módulo 26 para ciclar el alfabeto
            nuevo_caracter = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nuevo_caracter
        else:
            # Conservar espacios, números y símbolos sin alterar
            resultado += caracter
 
    return resultado
 
 
def descifrar_cesar(texto_cifrado, desplazamiento):
    """
    Descifra un texto cifrado con César.
    Descifrar = cifrar con desplazamiento negativo.
    
    Args:
        texto_cifrado (str): Mensaje cifrado a descifrar
        desplazamiento (int): Clave usada para cifrar
    
    Returns:
        str: Texto original descifrado
    """
    return cifrar_cesar(texto_cifrado, -desplazamiento)
 
 
def fuerza_bruta(texto_cifrado):
    """
    Intenta romper el cifrado probando los 25 desplazamientos posibles.
    Útil cuando no se conoce la clave (ataque de fuerza bruta).
    
    Args:
        texto_cifrado (str): Mensaje cifrado a atacar
    """
    print("\n🔓 Ataque de Fuerza Bruta — Probando los 25 desplazamientos:")
    print("=" * 60)
    for clave in range(1, 26):
        intento = descifrar_cesar(texto_cifrado, clave)
        print(f"  Clave {clave:2d}: {intento}")
    print("=" * 60)
 
 
def mostrar_menu():
    """Muestra el menú principal de la herramienta."""
    print("\n" + "=" * 50)
    print("  🔐 HERRAMIENTA DE CIFRADO CÉSAR — WolvesTI")
    print("=" * 50)
    print("  1. Cifrar un mensaje")
    print("  2. Descifrar un mensaje")
    print("  3. Ataque de fuerza bruta")
    print("  4. Salir")
    print("=" * 50)
 
 
def main():
    """Función principal — interfaz de usuario."""
    while True:
        mostrar_menu()
        opcion = input("  Selecciona una opción (1-4): ").strip()
 
        if opcion == '1':
            mensaje   = input("\n  Ingresa el mensaje a cifrar: ")
            clave     = int(input("  Ingresa la clave (1-25): "))
            cifrado   = cifrar_cesar(mensaje, clave)
            print(f"\n  ✅ Mensaje original:  {mensaje}")
            print(f"  🔐 Mensaje cifrado:   {cifrado}")
            print(f"  🔑 Clave usada:       {clave}")
 
        elif opcion == '2':
            cifrado   = input("\n  Ingresa el mensaje cifrado: ")
            clave     = int(input("  Ingresa la clave: "))
            original  = descifrar_cesar(cifrado, clave)
            print(f"\n  🔐 Mensaje cifrado:   {cifrado}")
            print(f"  ✅ Mensaje original:  {original}")
            print(f"  🔑 Clave usada:       {clave}")
 
        elif opcion == '3':
            cifrado = input("\n  Ingresa el mensaje cifrado para atacar: ")
            fuerza_bruta(cifrado)
 
        elif opcion == '4':
            print("\n  👋 Saliendo... ¡Hasta pronto!\n")
            break
 
        else:
            print("\n  ❌ Opción inválida. Intenta de nuevo.")
 
 
if __name__ == "__main__":
    main()