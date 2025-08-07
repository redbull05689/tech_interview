# Открываем файл логов для чтения
with open('logs.txt', 'r') as file:
    for line in file:
        # Удаляем лишние пробелы в начале и конце строки
        line = line.strip()
        # Пропускаем пустые строки
        if not line:
            continue
        # Разбиваем строку на части по пробелам
        parts = line.split()
        # Проверяем, что в строке достаточно частей для извлечения времени
        if len(parts) >= 3:
            time = parts[2]
            print(time)
            break