# pylint: disable=invalid-name
"""
wordCount.py

Este script cuenta la frecuencia de palabras en un archivo de texto.

Uso:
    python wordCount.py archivoConDatos.txt

Requisitos:
    1. El programa será invocado desde la línea de comando.
       Recibirá un archivo como parámetro que contendrá palabras (presumiblemente entre espacios).
    2. Deberá identificar todas las palabras distintas y su frecuencia en el archivo.
       Los resultados se imprimirán en la consola y en un archivo llamado
       WordCountResults_file_name.txt.
       Todos los cálculos deben realizarse utilizando algoritmos básicos, no funciones
       o bibliotecas.
    3. Deberá incluir un mecanismo para manejar datos no válidos en el archivo.
       Los errores deben mostrarse en la consola, y la ejecución debe continuar.
    4. El nombre del programa será wordCount.py.
    5. El formato mínimo para invocar el programa será el siguiente:
       python wordCount.py archivoConDatos.txt
    6. El programa gestionará archivos, pudiendo tener desde cientos hasta miles de artículos.
    7. El programa debe incluir al menos al final de la ejecución el tiempo transcurrido
       para la ejecución y cálculo de los datos. Este número se incluirá en el archivo de 
       resultados y en la pantalla.
    8. Cumple con PEP8.
"""

import os
import sys
import time

def read_file(file_path):
    """
    Lee un archivo de texto que contiene palabras.

    Parámetros:
    - file_path (str): Ruta del archivo a ser leído.

    Retorna:
    Una lista de palabras leídas desde el archivo.

    Si el archivo no existe, imprime un mensaje de error y retorna None.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
        return words
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
        return None

def count_word_frequency(words):
    """
    Cuenta la frecuencia de cada palabra en la lista.

    Parámetros:
    - words (list): Lista de palabras.

    Retorna:
    Un diccionario donde las claves son palabras y los valores son sus frecuencias.
    """
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

def print_and_save_results(word_frequency, file_name):
    """
    Imprime y guarda los resultados en un archivo.

    Parámetros:
    - word_frequency (dict): Diccionario con la frecuencia de palabras.
    - file_name (str): Nombre del archivo de entrada.

    Imprime la frecuencia de cada palabra en la consola y guarda los resultados en un archivo llamado WordCountResults_file_name.txt.
    """
    # Imprimir en la consola
    print("Resultados:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

    # Escribir en el archivo WordCountResults.txt
    result_file_name = f"WordCountResults_{file_name}.txt"
    with open(result_file_name, 'w', encoding='utf-8') as result_file:
        result_file.write("Resultados:\n")
        for word, frequency in word_frequency.items():
            result_file.write(f"{word}: {frequency}\n")

def main():
    """
    Función principal del programa.

    Este programa se invoca desde la línea de comandos para contar la frecuencia de palabras en un archivo de texto.
    Los resultados se imprimen en la consola y se guardan en un archivo llamado WordCountResults_file_name.txt.

    Uso:
        python wordCount.py archivoConDatos.txt
    """
    if len(sys.argv) != 2:
        print("Uso: python wordCount.py archivoConDatos.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()

    words = read_file(file_path)

    if words is not None:
        word_frequency = count_word_frequency(words)

        if word_frequency:
            print_and_save_results(word_frequency, os.path.basename(file_path))

            # Imprimir tiempo transcurrido
            elapsed_time = time.time() - start_time
            print(f"\nTiempo transcurrido: {elapsed_time} segundos")
        else:
            print("Error: No se pudieron calcular las frecuencias de palabras.")
    else:
        print("Error: No se pudo leer el archivo.")

if __name__ == "__main__":
    main()
