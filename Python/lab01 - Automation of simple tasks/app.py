import os
import time
from datetime import datetime
import requests

def rename_files(directory, prefix):
    """
    Renombra todos los archivos en el directorio especificado con un prefijo dado.
    """
    for index, filename in enumerate(os.listdir(directory)):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1]
            new_name = f"{prefix}_{index}{extension}"
            os.rename(file_path, os.path.join(directory, new_name))
    print(f"Archivos en {directory} renombrados con el prefijo '{prefix}'")

def clean_old_logs(directory, days_old):
    """
    Elimina archivos en un directorio que tienen más de 'days_old' días.
    """
    now = time.time()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_age = (now - os.path.getmtime(file_path)) / (24 * 3600)
            if file_age > days_old:
                os.remove(file_path)
                print(f"Archivo eliminado: {filename}")
    print(f"Archivos en {directory} más antiguos que {days_old} días eliminados.")

def check_website_availability(url):
    """
    Comprueba la disponibilidad de un sitio web mediante una solicitud HTTP.
    """
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"El sitio web {url} está disponible.")
        else:
            print(f"El sitio web {url} no está disponible. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al intentar acceder a {url}: {e}")

def main():
    # Directorio de prueba
    test_directory = "./test_files"
    
    # Crear directorio si no existe
    if not os.path.exists(test_directory):
        os.makedirs(test_directory)
    
    # Renombrar archivos
    rename_files(test_directory, "renamed_file")
    
    # Limpiar logs antiguos (más de 7 días)
    clean_old_logs(test_directory, 1)
    
    # Comprobar disponibilidad de un sitio web
    check_website_availability("https://www.example.com")

if __name__ == "__main__":
    main()