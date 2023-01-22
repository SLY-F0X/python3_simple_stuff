import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
# SVM Linear
# Условие задачи
dot_x1 = [-2, 2, 1]
dot_y1 = [1, 2, 1]
dot_x2 = [3, 4, 0]
dot_y2 = [-1, -3, -2]
print('Координаты первой группы точек:', f'X = {dot_x1}', f'Y = {dot_y1}',
     'Координаты второй группы точек:', f'X = {dot_x2}', f'Y = {dot_y2}', sep='\n')
# Выбор опорных векторов 
X = np.array([[1, 1, 1], [3, -1, 1], [0, -2, 1]], dtype=float)
S1 = X[0]
S2 = X[1]
S3 = X[2]
print('Точки опорных векторов:', S1, S2, S3, sep='\n')
# Перемножение векторов
S11 = S1.dot(S1)
S12 = S1.dot(S2)
S13 = S1.dot(S3)
S21 = S2.dot(S1)
S22 = S2.dot(S2)
S23 = S2.dot(S3)
S31 = S3.dot(S1)
S32 = S3.dot(S2)
S33 = S3.dot(S3)
# Объединение векторов по группам
m1 = [[S11, S12, S13], [S21, S22, S23], [S31, S32, S33]]
m2 = np.array([-1, 1, 1])
# Найдем обратную матрицу
m3 = inv(np.matrix(m1))
# Найдем решение 
#m4 = np.linalg.solve(m1, m2)
m4 = np.ravel(m3.dot(m2))
# Коэффициенты альфа
alpha1 = np.asarray(m4[0]).astype(np.float32)
alpha2 = np.asarray(m4[1]).astype(np.float32)
alpha3 = np.asarray(m4[2]).astype(np.float32)
print('Результаты расчетов альфа коэффициентов:', f'alpha1 = {alpha1}', f'alpha2 = {alpha2}', f'alpha3 = {alpha3}', sep='\n')
# Вектор нормали к разделяющей гиперплоскости
w_wave = np.ravel((alpha1.dot(S1)) + (alpha2.dot(S2) + (alpha3.dot(S3))))
W_line = w_wave[0], w_wave[1]
b = np.array(w_wave[2])
print('w_wave =', w_wave)
print('W_line =', np.array(W_line))
print('Смещение b =', b)
# Ширина разделяющей полосы. Чтобы разделяющая гиперплоскость как можно
# дальше отстояла от точек выборки, ширина полосы должна быть максимальной.
M = 2 / np.linalg.norm(W_line) 
# Угол наклона линии
a = -1 * (w_wave[0] / w_wave[1])
# Генерация последовательности чисел X для построения линии
xx = np.linspace(-3, 5, num = 2)
yy = a * xx # y для разделяющей линии
yy2 = a * xx - b # y для линии с учетом смещения
yy3 = a * xx + b 
yy2_M = a * xx - M # y для линии с максимальной шириной разделяющей полосы
yy3_M = a * xx + M
# Построение графика
plt.plot(dot_x1, dot_y1, 'r*', label='Объекты первой группы', markersize=10 ) # Объекты первой группы *
plt.plot(dot_x2, dot_y2, 'bo',label='Объекты второй группы') # Объекты второй группы о
plt.axis([-3, 5, -5, 4]) # Границы графика 
plt.grid(True) # Сетка
plt.plot(xx, yy, 'k-', label='Разделяющая линия') # Разделяющая линия
plt.plot(xx, yy2, 'g--', label='Опорные веторы')
plt.plot(xx, yy3, 'g--')
plt.plot(xx, yy2_M, 'm-.', label='Максимальная ширина разделяющей полосы') # Линии с максимальной шириной разделяющей полосы
plt.plot(xx, yy3_M, 'm-.')
plt.title("Линейная SVM")   
plt.ylabel('Y')   
plt.xlabel('X')
plt.legend(prop={'size': 8})
plt.show()


