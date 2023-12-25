import pandas as pd 
tennis = pd.read_csv('Tennis_dataset.csv', header = 1)
tennis.columns
#Явное указание столбцов, которые являются категориями, с помощью метода .astype().
for column in tennis.columns:
    tennis[column] = tennis[column].astype('category')
print('Условие задачи',tennis,'',sep='\n')
print('Таблица с описанием количества данных в датасете \
и частотой их повторяемости',tennis.describe(),'',sep='\n')

print('Количество ответов игры в теннис', tennis['PlayTennis'].value_counts(),'',sep='\n')

base = tennis.groupby('PlayTennis').size().div(len(tennis))
print('Отношение вероятности игры:', base,'',sep='\n')

print('Группировка и подсчет количества данных в зависимости от No или Yes',\
      tennis.groupby(['PlayTennis', 'Outlook']).size(),tennis.groupby(['PlayTennis', 'Temperature']).size(),\
      tennis.groupby(['PlayTennis', 'Humidity']).size(),tennis.groupby(['PlayTennis', 'Wind']).size(), sep='\n')

NB_dict={}
NB_dict['Outlook'] = tennis.groupby(['PlayTennis', 'Outlook']).size().div(len(tennis)).div(base)
NB_dict['Temperature'] = tennis.groupby(['PlayTennis', 'Temperature']).size().div(len(tennis)).div(base)
NB_dict['Humidity'] = tennis.groupby(['PlayTennis', 'Humidity']).size().div(len(tennis)).div(base)
NB_dict['Wind'] = tennis.groupby(['PlayTennis', 'Wind']).size().div(len(tennis)).div(base)

print('Расчет вероятности для категорий', NB_dict,'',sep='\n')
print('Нужно узнать будет ли человек играть в теннис,если на улице',
      'будет солнечно, прохладно, высокая влажность и сильный ветер','',sep='\n')

NB_yes = NB_dict['Outlook']['Yes']['Sunny']*NB_dict['Temperature']['Yes']['Cool']*\
         NB_dict['Humidity']['Yes']['High']*NB_dict['Wind']['Yes']['Strong'] * base['Yes']

NB_no = NB_dict['Outlook']['No']['Sunny']*NB_dict['Temperature']['No']['Cool']*\
        NB_dict['Humidity']['No']['High']*NB_dict['Wind']['No']['Strong'] * base['No']

# Нормализация данных
total = NB_yes + NB_no
yes_norm = NB_yes / total
no_norm = NB_no / total

print(f'Вероятность что игра состоится: {round(yes_norm,4)}')
print(f'Вероятность что игра не состоится: {round(no_norm,4)}')
print(f'Проверка: {round(yes_norm,4)+round(no_norm,4)}, равна ли сумма 1')

if yes_norm > no_norm:
    print('Игра точно сотоится')
else:
    print('Увы, не судьба поиграть')

input('')
