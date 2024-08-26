<details>
<summary>Class</summary>
Инкапсуляция позволяет скрывать внутренние детали объекта, предоставляя доступ только к тем данным и методам, которые необходимы внешнему миру.

Оно используется для того, чтобы создавать иерархии классов, где более специфические классы наследуют и расширяют поведение более общих классов.

Полиморфизм в объектно-ориентированном программировании (ООП) — это концепция, которая позволяет объектам разных классов обрабатывать данные одного типа или реагировать на одно и то же сообщение по-разному.

```
class Pet:     #Pet будет супер-классом для классов Cat, Dog и Raccoon
    def __init__(self, name):
        self.name = name

class Cat(Pet):
    def ask_for_food(self):
        print('Хозяин, кот {} требует пищу'.format(self.name))

    def __str__(self):
        return "Кот {}".format(self.name)

fil = Cat('Филимон')
fil.ask_for_food()

print(isinstance(fil, Cat)) #isinstance проверяет, является ли объект экземпляром указанного класса
print(issubclass(Cat, Pet)) #issubclass, проверяет, является ли класс потомком класса или одного из классов

```
У каждого метода должен быть как минимум один аргумент и называть этот аргумент принято словом self
</details>

<details>

<summary>Files</summary>

Открываем файл логов для чтения

```
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
```
</details>
<details>

<summary>Lambda</summary>

</details>

</details>
<details>

<summary>Functions</summary>
*args
*args позволяет передавать переменное количество позиционных аргументов в функцию. На практике это означает, что вы можете передать любое количество аргументов в функцию, и они будут упакованы в кортеж. Например:

```
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3)
```

**kwargs
**kwargs позволяет передавать переменное количество именованных (ключевых) аргументов в функцию. Эти аргументы будут упакованы в словарь. Например:

```
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(name="Alice", age=30, city="New York")
```
Здесь kwargs будет словарем {'name': 'Alice', 'age': 30, 'city': 'New York'},
и функция распечатает каждый ключ-значение.
</details>