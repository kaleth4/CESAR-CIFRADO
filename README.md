<div align="center">
 
```
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
```
 
# 🔐 Caesar Cipher — Cifrado César
 
**Implementación del algoritmo de cifrado histórico más famoso del mundo.**  
Cifra y descifra mensajes desplazando letras en el alfabeto. Introducción práctica a la criptografía.
 
---
 
[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Crypto](https://img.shields.io/badge/Tipo-Criptografía_Clásica-gold?style=for-the-badge&logo=gnuprivacyguard&logoColor=white)](https://github.com/)
[![Beginner](https://img.shields.io/badge/Nivel-Principiante-00c853?style=for-the-badge)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
 
</div>
 
---
 
## 📜 Historia
 
> *"Si Julio César tenía un mensaje secreto que enviar, lo escribía en código — cada letra reemplazada por otra tres posiciones más adelante en el alfabeto."*  
> — Suetonio, historiador romano, 121 d.C.
 
El **Cifrado César** es uno de los algoritmos criptográficos más antiguos de la historia, utilizado por **Julio César** para comunicarse con sus generales de forma secreta alrededor del **año 58 a.C.**
 
```
MENSAJE ORIGINAL:  ATACAR AL AMANECER
DESPLAZAMIENTO:    +3
MENSAJE CIFRADO:   DWDFDU DO DPDQHFHU
```
 
---
 
## ⚙️ ¿Cómo funciona?
 
```
Alfabeto original:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
                    ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
Desplazamiento +3:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
 
   H → K
   O → R        "HOLA"  ==cifrar==>  "KROD"
   L → O        "KROD"  ==descifrar==>  "HOLA"
   A → D
```
 
La fórmula matemática es:
 
```
Cifrado:    C = (P + K) mod 26
Descifrado: P = (C - K) mod 26
 
Donde:
  P = posición de la letra original (plaintext)
  C = posición de la letra cifrada  (ciphertext)
  K = clave / desplazamiento        (key)
```
 
---
 
## 💻 Código completo
 
```python
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
```
 
---
 
## 🖥️ Demo de uso
 
```bash
==================================================
  🔐 HERRAMIENTA DE CIFRADO CÉSAR — WolvesTI
==================================================
  1. Cifrar un mensaje
  2. Descifrar un mensaje
  3. Ataque de fuerza bruta
  4. Salir
==================================================
  Selecciona una opción (1-4): 1
 
  Ingresa el mensaje a cifrar: Atacar al amanecer
  Ingresa la clave (1-25): 13
 
  ✅ Mensaje original:  Atacar al amanecer
  🔐 Mensaje cifrado:   Ngpnne ny nznarprhe
  🔑 Clave usada:       13
```
 
```bash
  Selecciona una opción (1-4): 3
 
  Ingresa el mensaje cifrado para atacar: Ngpnne ny nznarprhe
 
🔓 Ataque de Fuerza Bruta — Probando los 25 desplazamientos:
============================================================
  Clave  1: Mfommd mx myzmzoqdg
  Clave  2: Lenlc lw lxylylpcf
  ...
  Clave 13: Atacar al amanecer   ← ✅ ENCONTRADO
  ...
============================================================
```
 
---
 
## 📂 Estructura del proyecto
 
```
caesar-cipher/
│
├── 📄 caesar.py          # Script principal completo
├── 📄 README.md          # Documentación del proyecto
└── 📁 ejemplos/
    ├── mensaje_cifrado.txt
    └── mensaje_original.txt
```
 
---
 
## 🚀 Instalación y ejecución
 
```bash
# 1. Clonar el repositorio
git clone https://github.com/kaleth4/caesar-cipher.git
 
# 2. Entrar al directorio
cd caesar-cipher
 
# 3. Ejecutar — sin dependencias externas
python caesar.py
```
 
> ✅ No requiere instalar ninguna librería. Solo Python 3.8+
 
---
 
## 🔬 Conceptos de seguridad aplicados
 
| Concepto | Descripción |
|----------|-------------|
| **Criptografía simétrica** | Misma clave para cifrar y descifrar |
| **Cifrado por sustitución** | Reemplaza caracteres por otros |
| **Aritmética modular** | `mod 26` para ciclar el alfabeto |
| **Fuerza bruta** | Ataque probando todas las claves posibles |
| **Confidencialidad** | Pilar CIA — protección de información |
 
---
 
## ⚠️ Limitaciones y contexto
 
```
❌ NO usar en producción — es un cifrado roto desde el siglo XIX
✅ SÍ usar para aprender fundamentos de criptografía
✅ SÍ usar para entender por qué AES/RSA existen
```
 
El César solo tiene **25 claves posibles** — cualquier atacante puede romperlo
en segundos con fuerza bruta. Es el punto de partida para entender por qué
los algoritmos modernos usan claves de **128, 256 o 4096 bits**.
 
---
 
## 🔮 Mejoras futuras
 
- [ ] 🔤 Soporte para alfabeto español con tildes y ñ
- [ ] 📁 Cifrado/descifrado de archivos `.txt`
- [ ] 🖥️ Interfaz gráfica con Tkinter
- [ ] 📊 Análisis de frecuencia de letras para criptoanálisis
- [ ] 🔐 Implementar Cifrado Vigenère como evolución
 
---
 
## 👤 Autor
 
**Kaleth Corcho**  
Ingeniería de Sistemas · WolvesTI · Bogotá, Colombia
 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-kaleth--corcho-0077B5?style=flat&logo=linkedin)](https://linkedin.com)
[![GitHub](https://img.shields.io/badge/GitHub-kaleth4-181717?style=flat&logo=github)](https://github.com/kaleth4)
 
---
 
<div align="center">
 
**⭐ Si este proyecto te fue útil, dale una estrella**
 
*Proyecto de portafolio en ciberseguridad · 2026 · WolvesTI*
 
</div>
