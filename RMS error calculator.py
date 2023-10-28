import random
import math
print('~'*50)
# Начальное условие
nums = int(3)
student_coef = 4.302652729911275
result_of_calc = 6081
nadejnost = 0.95

print(f'Число измерений: {nums}',f'Коэффициент Стьюдента: {student_coef}',
      f'Результат измерений: {result_of_calc}', f'Надежность: {nadejnost}', sep='\n')
print('~'*50)

# Получение чисел от количества измерений
x_i=[]
for i in range(nums):
    x_i.append(random.randint(-5, 5) + result_of_calc)
print('Рандомные числа от результата:',*x_i, sep=' ')

# Среднее арифметическое
srednee_arifm = []
srednee_arifm.append(sum(x_i)/nums)
srednee_arifm = [round(v, 2) for v in srednee_arifm]  # округление
print('Cреднее арифметическое:',srednee_arifm[0])
print('~'*50)

# Среднеквадратичная погрешность σ
srdn_kvadr_pogresh = []
elems = []
for j in range(int(nums)):
    elems.append((x_i[j] - srednee_arifm[0])**2) # квадраты погрешностей отдельных измерений
    srdn_kvadr_pogresh = math.sqrt(sum(elems)/(nums*(nums-1)))
srdn_kvadr_pogresh = round(srdn_kvadr_pogresh,3)
print('Среднеквадратичная погрешность σ:',srdn_kvadr_pogresh)

# Доверительный интервал
dover_interv = student_coef * srdn_kvadr_pogresh
dover_interv = round(dover_interv,3)
print('Доверительный интервал (Δa):', dover_interv)
minus_delta = round(srednee_arifm[0] - dover_interv,3)
plus_delta = round(srednee_arifm[0] + dover_interv,3)
print('-Δa',minus_delta,'≤ Δa',srednee_arifm[0], '≤ +Δa',plus_delta)

# Относительная погрешность %
otnos_pogresh = (dover_interv/srednee_arifm[0])*100.0
print('Относительная погрешность:', round(otnos_pogresh,2),'%')
print('~'*50)
