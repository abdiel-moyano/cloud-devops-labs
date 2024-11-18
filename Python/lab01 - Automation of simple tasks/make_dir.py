# Crear una carpeta de prueba y generar algunos archivos de prueba en ella
import os

test_directory = "./test_files"

# Crear el directorio si no existe
os.makedirs(test_directory, exist_ok=True)

# Generar algunos archivos de prueba
file_contents = [
    ("log1.txt", "This is a test log file 1."),
    ("log2.txt", "This is a test log file 2."),
    ("data1.csv", "id,name,age\n1,John,30\n2,Jane,25"),
    ("data2.csv", "id,name,age\n3,Alice,35\n4,Bob,40"),
    ("readme.md", "# Test Directory\nThis is a README file for the test directory.")
]

for filename, content in file_contents:
    with open(os.path.join(test_directory, filename), "w") as f:
        f.write(content)

test_directory