# Задача 3: Периметр и площадь прямоугольника
# Напишите программу, которая запрашивает у пользователя длину и ширину прямоугольника и выводит его периметр и площадь.
# Пример:
# Ввод: 4, 7
# Вывод: Периметр: 22, Площадь: 28

L=int(input())
D=int(input())
P=2*(L+D)
S=L*D
print("Периметр:", P, "Площадь:", S)
