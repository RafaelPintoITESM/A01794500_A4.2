# pylint: disable=invalid-name
"""
convertNumbers.py

Este script permite la conversión de números decimales a sus equivalentes en binario
y hexadecimal. Los resultados se imprimen en la consola y se guardan en un archivo.

Uso:
    python convertNumbers.py archivoConDatos.txt
"""

import os
import sys
import time

def read_file(file_path):
    """
    Convierte números de formato decimal a binario y hexadecimal.

    Parámetros:
    - data: Lista de números en formato decimal.

    Retorna:
    Una tupla con dos listas:
    - Lista de números en formato binario.
    - Lista de números en formato hexadecimal.

    Si la lista de entrada es vacía, retorna (None, None).

    Ejemplo:
    convertNumbers([10, 20, 30])
    Salida: (['1010', '10100', '11110'], ['a', '14', '1e'])
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = [float(line.strip()) for line in file.readlines()]
        return data
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
        return None
    except ValueError:
        print("Error: El archivo contiene datos no válidos.")
        return None

def convert_numbers(data):
    """
    Convierte números de formato decimal a binario y hexadecimal.

    Parámetros:
    - data: Lista de números en formato decimal.

    Retorna:
    Una tupla con dos listas:
    - Lista de números en formato binario.
    - Lista de números en formato hexadecimal.

    Si la lista de entrada es vacía, retorna (None, None).

    Ejemplo:
    convert_numbers([10, 20, 30])
    Salida: (['1010', '10100', '11110'], ['a', '14', '1e'])
    """
    if data:
        binary_results = [bin(int(x))[2:] for x in data]
        hex_results = [hex(int(x))[2:] for x in data]
        return binary_results, hex_results
    else:
        return None, None

def print_results(data,binary_results, hex_results, file_name):
    """
    Imprime los resultados en la consola y los guarda en un archivo.

    Parámetros:
    - data: Lista de números en formato decimal.
    - binary_results: Lista de números en formato binario.
    - hex_results: Lista de números en formato hexadecimal.
    - file_name: Nombre del archivo de entrada.

    Este función imprime los resultados en la consola y los guarda en un archivo
    llamado ConvertResults_file_name.txt.

    """
    # Imprimir en la consola
    print("Resultados:")
    print("Decimal\t\tBinario\t\tHexadecimal")
    for decimal, binary, hexadecimal in zip(data, binary_results, hex_results):
        print(f"{decimal}\t\t{binary}\t\t{hexadecimal}")

    # Escribir en el archivo ConvertResults.txt
    file_name_without_extension = os.path.splitext(file_name)[0]
    result_file_name = f"ConvertResults_{file_name_without_extension}.txt"
    with open(result_file_name, 'w', encoding='utf-8') as result_file:
        result_file.write("Resultados:\n")
        result_file.write("Decimal\t\tBinario\t\tHexadecimal\n")
        for decimal, binary, hexadecimal in zip(data, binary_results, hex_results):
            result_file.write(f"{decimal}\t\t{binary}\t\t{hexadecimal}\n")

def main():
    """
    Función principal del programa.

    Este programa se invoca desde la línea de comandos para convertir
    números en base binaria y hexadecimal. Los resultados se imprimen
    en la pantalla y se guardan en un archivo llamado ConvertResults.txt.

    Uso:
        python convertNumbers.py archivoWithData.txt
    """
    if len(sys.argv) != 2:
        print("Uso: python convertNumbers.py archivoWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()

    data = read_file(file_path)

    if data is not None:
        binary_results, hex_results = convert_numbers(data)

        if binary_results is not None and hex_results is not None:
            print_results(data,binary_results, hex_results, os.path.basename(file_path))

            # Imprimir tiempo transcurrido
            elapsed_time = time.time() - start_time
            print(f"\nTiempo transcurrido: {elapsed_time} segundos")
        else:
            print("Error: No se pudieron convertir los números.")
    else:
        print("Error: No se pudo leer el archivo.")

if __name__ == "__main__":
    main()
