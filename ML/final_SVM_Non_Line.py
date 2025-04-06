import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
# SVM Нелинейный случай
# Условие задачи
dot_x1 = np.array([2, 2, -2, -2])
dot_y1 = np.array([2, -2, -2, 2])
dot_x2 = np.array([1, 1, -1, -1])
dot_y2 = np.array([1, -1, -1, 1])

first_gr = np.array(list(zip(dot_x1, dot_y1)))
second_gr = np.array(list(zip(dot_x2, dot_y2)))
print('Координаты положительно помеченных объектов, 1 группа:', f'X = {dot_x1}', f'Y = {dot_y1}',
     'Координаты отрицательно помеченных объектов, 2 группа:', f'X = {dot_x2}', f'Y = {dot_y2}', sep='\n')
def cord(value):
    temp = []
    for cord in value:
        if (cord[0]**2+cord[1]**2)**0.5>2:
            temp.append((4-cord[1]+abs(cord[0]-cord[1]),4-cord[0]+abs(cord[0]-cord[1])))      
        else:
            temp.append((cord[0],cord[1]))
    return temp

first_gr = cord(first_gr)
second_gr = cord(second_gr)

print('~'*60)
print('Координаты после преобразования (X, Y):', f'Первой группы: {first_gr}', f'Второй группы: {second_gr}','~'*60, sep='\n')
S1 = list(second_gr[0]) + [1,]
S2 = list(first_gr[0]) + [1,]
print('Опорные векторы', f'S1 = {S1}', f'S2 = {S2}','~'*60, sep='\n')

X = np.array([(S1), (S2)], dtype=float)
S11 = X[0].dot(X[0])
S12 = X[0].dot(X[1])
S21 = X[1].dot(X[0])
S22 = X[1].dot(X[1])
print(f'S11 = {S11} S12 = {S12}', f'S21 = {S21} S22 = {S22}', '~'*60, sep='\n')
m1 = [[S11, S12], [S21, S22]]
m2 = np.array([-1, 1])
print('Составление матрицы:', m1)
m4 = np.linalg.solve(m1, m2)
print('Решение матрицы:', m4)
alpha1 = np.asarray(m4[0]).astype(np.float32)
alpha2 = np.asarray(m4[1]).astype(np.float32)
print('~'*60, 'Результаты расчетов:', f'Альфа_1 = {alpha1}', f'Альфа_2 = {alpha2}', sep='\n')
w_wave = np.ravel((alpha1.dot(S1)) + (alpha2.dot(S2)))
w_line = w_wave[0], w_wave[1]
b = np.array(w_wave[2])
print(f'w_wave = {w_wave}', f'w_line = {w_line}', f'b = {b}', sep='\n')
# Функция получения координат x, y из списка
def cord(value):
    x = []
    y = []
    for element in value:
        x.append(element[0])
        y.append(element[1])
    return(x, y)
x1 = cord(first_gr)[0]
y1 = cord(first_gr)[1]
x2 = cord(second_gr)[0]
y2 = cord(second_gr)[1]
# Вычисления линии разделения
xx = np.linspace(-5, 10, num = 10)
yy = (w_wave[0] / (-w_wave[1]))* xx - w_wave[2]
# Построение графика
plt.figure(1)
plt.plot(dot_x1, dot_y1, 'r*', label='Объекты первой группы +', markersize=10)
plt.plot(dot_x2, dot_y2, 'bo', label='Объекты второй группы -')
plt.grid(True)
plt.title("Заданные значения")
plt.ylabel('Y')   
plt.xlabel('X')
plt.legend(prop={'size': 8})

plt.figure(2)
plt.plot(x1, y1, 'r*', label='Объекты первой группы +', markersize=10)
plt.plot(x2, y2, 'bo', label='Объекты второй группы -') 
plt.grid(True) # Сетка
plt.title("Нелинейная SVM")   
plt.ylabel('Y')   
plt.xlabel('X')
plt.legend(prop={'size': 8})
plt.plot(xx, yy, 'k-')
plt.show()


