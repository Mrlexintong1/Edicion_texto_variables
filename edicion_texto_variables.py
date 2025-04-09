# -*- coding: utf-8 -*-
# 💬 Edición de texto interactiva por Carlos Tlali

# 14 - Frase fija
frase_fija = "La programación es el futuro."
print(f"14 - Frase fija: {frase_fija}")

# 15 - Solicita una frase
frase_usuario = input("15 - Ingresa una frase: ")
print(f"Frase ingresada: {frase_usuario}")

# 16 - Frase en mayúsculas
frase_mayusculas = input("16 - Escribe otra frase: ")
print(f"Frase en MAYÚSCULAS: {frase_mayusculas.upper()}")

# 17 - Frase en minúsculas
frase_minusculas = input("17 - Escribe una frase en mayúsculas: ")
print(f"Frase en minúsculas: {frase_minusculas.lower()}")

# 18 - Elimina espacios de una frase fija
frase_con_espacios = "   Python es genial   "
print(f"18 - Frase limpia: '{frase_con_espacios.strip()}'")

# 19 - Elimina espacios de frase del usuario
frase_espaciada = input("19 - Ingresa una frase con espacios: ")
print(f"Frase sin espacios extras: '{frase_espaciada.strip()}'")

# 20 - Limpia y pone en minúsculas
frase_limpia_min = input("20 - Frase desordenada: ")
print(f"Frase limpia y en minúsculas: '{frase_limpia_min.strip().lower()}'")

# 21 - Reemplaza vocal 'e' por 'f'
frase_reemplazo_e = input("21 - Frase para reemplazar 'e' por 'f': ")
print(f"Frase modificada: {frase_reemplazo_e.replace('e', 'f')}")

# 22 - Reemplaza vocal 'a' por '@'
frase_reemplazo_a = input("22 - Frase para reemplazar 'a' por '@': ")
print(f"Frase modificada: {frase_reemplazo_a.replace('a', '@')}")

# 23 - Reemplaza consonante 's' por '$'
frase_reemplazo_s = input("23 - Frase para reemplazar 's' por '$': ")
print(f"Frase modificada: {frase_reemplazo_s.replace('s', '$')}")
