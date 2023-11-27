#1
hat_list = [1, 2, 3, 4, 5]  # Це існуючий список чисел, які приховані в капелюсі.

# Крок 1: Заміна середнього числа на ціле число, яке вводить користувач.
hat_list[2] = int(input("Введіть нове число: "))

# Крок 2: Видалення останнього елемента зі списку.
hat_list.pop()

# Крок 3: Виведення довжини існуючого списку.
print("Довжина списку:", len(hat_list))

print(hat_list)

#2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Інтерактивне введення елементів масива
arr = []
n = int(input("Введіть кількість елементів у списку: "))
for i in range(n):
    element = int(input(f"Введіть {i + 1}-й елемент: "))
    arr.append(element)

print("Початковий список:", arr)

# Сортування списку методом бульбашки
bubble_sort(arr)

print("Відсортований список:", arr)

#3
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Використовуємо set для видалення дублікатів та створення унікального списку
unique_list = list(set(my_list))

print("The list with unique elements only:")
print(unique_list)

#4
chess_board = [['_'] * 8 for _ in range(8)]

# Розставляємо тури в кутах шахівниці
chess_board[0][0] = 'R'  # Ліва верхня клітина
chess_board[0][7] = 'R'  # Права верхня клітина
chess_board[7][0] = 'R'  # Ліва нижня клітина
chess_board[7][7] = 'R'  # Права нижня клітина

# Виводимо шахівницю
for row in chess_board:
    print(row)