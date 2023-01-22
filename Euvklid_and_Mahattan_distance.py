# Алгоритм KNN ближайшие соседи
# Входные данные
x = [167, 182, 176, 173, 172, 174, 169, 173, 170]
y = [51, 62, 69, 64, 65, 56, 58, 57, 55]
clas = [("Underweight"), ("Normal"), ("Normal"), ("Normal"),("Normal"), ("Underweight"), ("Normal"), ("Normal"), ("?")]
print(f'|Height|  {x}',f'|Weight|  {y}',f'|Class |  {clas}', '~' * 71, sep='\n')

# Перебор списка по x
d = len(x)-1

print('Манхэттенское расстояние:', end=' ')
manH = [] # Задание пустого списка для записи полученных результатов из цикла
for i in range(d):
    print(abs(x[-1] - x[i]) + abs(y[-1] - y[i]), end='    ')
    manH.append(abs(x[-1] - x[i]) + abs(y[-1] - y[i]))
print('\n','~'*70) 

print('Евклидово расстояние: ',end=' ')
evkL = []
for i in range(d):
    print('%.2f' %((x[-1] - x[i])**2 + (y[-1] - y[i])**2)**(0.5),end=' ')
    evkL.append('%.2f' %((x[-1] - x[i])**2 + (y[-1] - y[i])**2)**(0.5))
print ('\n','~'*70) 

# Объединение результатов расчетов записанных в список, со списком классов
manhS = (list(zip(manH, clas)))
evqlS = (list(zip(evkL, clas)))
# Сортировка
sortM = sorted(manhS)
# Функция сортировки кортежа с элементом float, по возрастанию
def sort(sortE):
       return(sorted(sortE, key = lambda x: float(x[0])))
sortE = sort(evqlS)

print("Определение класса по Манхэттенскому расстоянию, для ", 'Height', x[-1], 'Weight', y[-1], 'class', clas[-1], '\n')
print("Cортировка: ", sortM, '\n')
print("Ближайшие соседние точки k = 2: ", sortM[0:2])
print('~'*71)
print("Определение класса по Евклидову расстоянию, для ", 'Height', x[-1], 'Weight', y[-1], 'class', clas[-1], '\n')
print("Cортировка: ", sortE, '\n')
print("Ближайшие соседние точки k = 2: ", sortE[0:2])
print ('~'*71)
input('Нажмите Enter для выхода из программы')
