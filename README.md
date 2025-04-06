## 🔐 Шифрование (`/Encryption`)
- [Шифр Цезаря](Encryption/Caesar_cipher.py) - симметричное шифрование для русского алфавита
- [DES ECB](Encryption/DES.py) - GUI-реализация стандарта шифрования данных 
- [Трисемус](Encryption/Trisemus%20encryption%20system.py) - табличный шифр подстановки
- [Документация](Encryption/README.md) - подробное описание всех методов

## 🧮 Нечеткая логика (`/Fuzzy_logic`)
- [Калькулятор матриц](Fuzzy_logic/Fuzzy_Calc.py) - операции над нечеткими множествами:
  - Максиминная композиция
  - Минимаксная композиция  
  - Максимультипликативная
- [Руководство](Fuzzy_logic/README.md) - форматы ввода и примеры использования

## 🤖 Машинное обучение (`/ML`)
### Классификация
- **[Naive Bayesian classifier](ML/Naive_Bayesian_classifier.py)**  
Наивный Байесовский классификатор для прогнозирования игры в теннис:
  - Расчет условных вероятностей для 4 параметров
  - Автоматическая обработка категориальных данных
  - Пример использования: Sunny, Cool, High Humidity, Strong Wind

- **[KNN Classifier](ML/Euvklid_and_Mahattan_distance.py)**  
Алгоритм k-ближайших соседей:
  - Поддержка двух метрик расстояния: Манхэттенское и Евклидово
  - Тестовые данные: рост (167-182 см), вес (51-69 кг)
  - Визуализация топ-2 ближайших соседей

### Методы опорных векторов (SVM)
- **[Линейный SVM](ML/final_SVM_Linear.py)**  
  - Ручной выбор 3 опорных векторов
  - Расчет:
    - Коэффициенты α (alpha1-α3)
    - Параметры разделяющей гиперплоскости
    - Ширина максимальной разделяющей полосы
  - Визуализация с matplotlib

- **[Нелинейный SVM](ML/final_SVM_Non_Line.py)**  
  - Ядерное преобразование для точек вне радиуса 2
  - Матричное решение системы уравнений
  - Двойная визуализация: исходные/трансформированные данные

### Данные
- **[Tennis Dataset](ML/Tennis_dataset.csv)**  
Датасет погодные условия для классификации:
  ```csv
  Day,Outlook,Temperature,Humidity,Wind,PlayTennis
  D1,Sunny,Hot,High,Weak,No
  ...
  D14,Rain,Mild,High,Strong,No
  ```