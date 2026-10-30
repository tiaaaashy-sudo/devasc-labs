# Открыть файл и прочитать его целиком
with open("devices.txt", "r") as f:
    content = f.read()
print(content)

# Построчное чтение
with open("devices.txt", "r") as f:
    for line in f:
        print(line.strip())

# Добавление строки в конец файла
with open("devices.txt", "a") as f:
    f.write("\nCisco 9300 Catalyst Switch")

# Чтение в список
with open("devices.txt", "r") as f:
    devices = f.readlines()
print(len(devices))
