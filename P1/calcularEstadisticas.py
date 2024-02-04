# pylint: disable=invalid-name
"""
calcularEstadisticas.py

Este script calcula estadísticas descriptivas (media, mediana, moda, desviación estándar
y varianza) a partir de un archivo que contiene números en formato decimal.

Uso:
    python calcularEstadisticas.py archivoConDatos.txt
"""

import time
import sys

def read_file(file_path):
    """
    Lee un archivo de texto que contiene números en formato decimal.

    Parámetros:
    - file_path (str): Ruta del archivo a ser leído.

    Retorna:
    Una lista de números en formato decimal leídos desde el archivo.

    Si el archivo no existe, imprime un mensaje de error y retorna None.
    Si hay datos no válidos en el archivo, imprime un mensaje de error y retorna None.
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

def count_records(data):
    """
    Cuenta el número de registros en la lista de datos.

    Parámetros:
    - data (list): Lista de datos para la cual se contará el número de registros.

    Retorna:
    La cantidad de registros en la lista. Retorna 0 si la lista está vacía o es `None`.
    """
    return len(data) if data else 0

def calculate_mean(data):
    """
    Calcula la media aritmética de los datos en la lista.

    Parámetros:
    - data (list): Lista de datos para la cual se calculará la media.

    Retorna:
    La media aritmética de los datos en la lista. Retorna `None` si la lista está vacía o es `None`.
    """
    return sum(data) / len(data) if data else None

def calculate_median(data):
    """
    Calcula la mediana de los datos en la lista.

    Parámetros:
    - data (list): Lista de datos para la cual se calculará la mediana.

    Retorna:
    La mediana de los datos en la lista. Retorna `None` si la lista está vacía o es `None`.
    """
    sorted_data = sorted(data)
    n_data = len(sorted_data)
    if n_data % 2 == 0:
        return (sorted_data[n_data // 2 - 1] + sorted_data[n_data // 2]) / 2 if data else None
    else:
        return sorted_data[n_data // 2] if data else None

def calculate_mode(data):
    """
    Calcula la moda de los datos en la lista.

    Parámetros:
    - data (list): Lista de datos para la cual se calculará la moda.

    Retorna:
    La moda de los datos en la lista. Retorna "No hay moda" si la lista está vacía o es `None`.
    """
    occurrences = {}
    for value in data:
        occurrences[value] = occurrences.get(value, 0) + 1
    max_occurrences = max(occurrences.values())
    mode_candidates = [key for key, value in occurrences.items() if value == max_occurrences]

    mode = mode_candidates[0] if max_occurrences > 1 else "No hay moda"
    return mode[0] if data else None

def calculate_std_dev(data, mean):
    """
    Calcula la desviación estándar de los datos en la lista dado el valor medio (media).

    Parámetros:
    - data (list): Lista de datos para la cual se calculará la desviación estándar.
    - mean (float): Valor medio (media) de los datos.

    Retorna:
    La desviación estándar de los datos en la lista. Retorna `None`
    si la lista está vacía o es `None`.
    """
    squared_diff = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diff) / len(data) if data else None
    return variance ** 0.5 if data else None

def calculate_variance(data, mean):
    """
    Calcula la varianza de los datos en la lista dado el valor medio (media).

    Parámetros:
    - data (list): Lista de datos para la cual se calculará la varianza.
    - mean (float): Valor medio (media) de los datos.

    Retorna:
    La varianza de los datos en la lista. Retorna `None` si la lista está vacía o es `None`.
    """
    squared_diff = [(x - mean) ** 2 for x in data]
    return sum(squared_diff) / len(data) if data else None

def calculate_statistics(data):
    """
    Calcula estadísticas descriptivas a partir de una lista de números.

    Parámetros:
    - data (list): Lista de números en formato decimal.

    Retorna:
    Una tupla con las estadísticas calculadas en el siguiente orden:
    (media, mediana, moda, desviación estándar, varianza).

    Si la lista de entrada es vacía, retorna None.
    """
    if data:
        count = count_records(data)
        mean = calculate_mean(data)
        median = calculate_median(data)
        mode = calculate_mode(data)
        std_dev = calculate_std_dev(data, mean)
        variance = calculate_variance(data, mean)
        return count, mean, median, mode, std_dev, variance
    else:
        return None

def print_results(count,mean, median, mode, std_dev, variance, elapsed_time):
    """
    Imprime los resultados en la consola y los guarda en un archivo.

    Parámetros:
    - mean (float): Media de los datos.
    - median (float): Mediana de los datos.
    - mode (float or str): Moda de los datos o mensaje indicando que no hay moda.
    - std_dev (float): Desviación estándar de los datos.
    - variance (float): Varianza de los datos.
    - file_name (str): Nombre del archivo de entrada.

    Imprime los resultados en la consola y los guarda en un archivo llamado
    ResultadosEstadísticos_file_name.txt.
    """
    # Imprimir en la consola
    print("Resultados:")
    print(f"Cantidad: {count}")
    print(f"Media: {mean}")
    print(f"Mediana: {median}")
    print(f"Moda: {mode}")
    print(f"Desviación estándar: {std_dev}")
    print(f"Varianza: {variance}")

    # Imprimir tiempo transcurrido
    print(f"\nTiempo transcurrido: {elapsed_time} segundos")

    # Escribir en el archivo ResultadosEstadísticos.txt
    with open("ResultadosEstadísticos.txt", 'w', encoding='utf-8') as result_file:
        result_file.write("Resultados:\n")
        result_file.write(f"Cantidad: {count}\n")
        result_file.write(f"Media: {mean}\n")
        result_file.write(f"Mediana: {median}\n")
        result_file.write(f"Moda: {mode}\n")
        result_file.write(f"Desviación estándar: {std_dev}\n")
        result_file.write(f"Varianza: {variance}\n")
        result_file.write(f"\nTiempo transcurrido: {elapsed_time} segundos")

def main():
    """
    Función principal del programa.

    Este programa se invoca desde la línea de comandos para calcular
    estadísticas descriptivas a partir de un archivo que contiene números
    en formato decimal. Los resultados se imprimen en la consola y se
    guardan en un archivo llamado ResultadosEstadísticos_file_name.txt.

    Uso:
        python calcularEstadisticas.py archivoConDatos.txt
    """
    if len(sys.argv) != 2:
        print("Uso: python calcularEstadísticas.py archivoConDatos.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()

    data = read_file(file_path)

    if data is not None:
        results = calculate_statistics(data)
        if results:
            count, mean, median, mode, std_dev, variance = results
            elapsed_time = time.time() - start_time
            print_results(count,mean, median, mode, std_dev, variance, elapsed_time)
        else:
            print("Error: No se pudieron calcular las estadísticas.")
    else:
        print("Error: No se pudo leer el archivo.")

if __name__ == "__main__":
    main()
