import numpy as np
# Створення масиву з 200 випадкових чисел від -100 до 100
array = np.random.randint(-100, 101, size = (200, )) 
print("Початковий масив: ", array)

# Фільтруємо додатні числа
positive_mask = array > 0
positive_numbers = array[positive_mask]
print("Відфільтровані додатні числа: ", positive_numbers)

# За допомогою маски фільтруємо додатні числа масиву, та від'ємні значення заміняємо на 0
array[array < 0] = 0 
print("Масив після заміни від'ємних чисел на 0: ", array)

average_value = np.average(array)
print("Середнє значення масиву: ", average_value) # Середнє значення масиву