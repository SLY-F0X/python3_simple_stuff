```Fuzzy_Calc.py  
Калькулятор операций над нечеткими матрицами

Алгоритмы:
- Максиминная композиция (min-max)
- Минимаксная композиция (max-min)
- Максимультипликативная композиция (max-product)

Особенности:
- GUI-интерфейс на Tkinter
- Поддержка двух форматов ввода:
  1. Традиционная матричная запись
  2. Специальный формат для Word: ■(a&b@c&d)
- Автоматическая валидация входных данных
- Преобразование результатов для экспорта в MS Word

Интерфейс:
- Два текстовых поля для матриц A и B
- Цветные кнопки операций
- Область вывода результатов
- Инструменты:
  - Копирование в буфер обмена
  - Генерация Word-совместимого формата

Функционал:
- Вычисление композиций для матриц 3x3
- Обработка десятичных чисел (запятые/точки)
- Визуальное выделение ошибок ввода
- Поддержка прозрачности окна (alpha=0.95)

Входные данные:
- Матрицы в формате:
  ■(0.1&0.2&0.3@0.4&0.5&0.6@0.7&0.8&0.9)
  или
  0.1 0.2 0.3
  0.4 0.5 0.6
  0.7 0.8 0.9
```
