def filter_logs_by_level(file_path, log_level):
    try:
        with open(file_path, 'r') as file:
            filtered_lines = [line for line in file if log_level in line]
        return filtered_lines
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []
    
# Especifica el archivo de logs y el nivel de log que deseas filtrar
file_path = 'logs.txt'
log_level = 'INFO'

# Llama a la función y muestra las líneas filtradas
filtered_logs = filter_logs_by_level(file_path, log_level)
print("Filtered logs:")
for line in filtered_logs:
    print(line.strip())  # strip() para eliminar saltos de línea adicionales