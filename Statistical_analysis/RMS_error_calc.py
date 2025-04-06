import random
import math

def print_separator(char='~', length=50):
    """Печатает разделитель заданной длины"""
    print(char * length)

def calculate_mean(data):
    """Вычисляет среднее арифметическое с округлением до 2 знаков"""
    return round(sum(data) / len(data), 2)

def calculate_standard_error(data, mean):
    """Вычисляет стандартную ошибку среднего"""
    squared_errors = [(x - mean)**2 for x in data]
    return math.sqrt(sum(squared_errors) / (len(data) * (len(data)-1)))

def main():
    # Ввод параметров
    try:
        n = int(input("Введите количество измерений: "))
        if n < 2:
            raise ValueError("Количество измерений должно быть не менее 2")
            
        student_coef = float(input("Введите коэффициент Стьюдента: "))
        base_value = float(input("Введите базовое значение: "))
        confidence = float(input("Введите уровень надежности (0-1): "))
        
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
        return

    print_separator()
    print(f"{'Параметры измерений:':<25}\n"
          f"Количество измерений: {n}\n"
          f"Коэффициент Стьюдента: {student_coef}\n"
          f"Базовое значение: {base_value}\n"
          f"Уровень надежности: {confidence:.0%}")
    print_separator()

    # Генерация случайных данных
    measurements = [random.randint(-5, 5) + base_value for _ in range(n)]
    print("Результаты измерений:", *measurements, sep='\n- ')

    # Статистические расчеты
    mean = calculate_mean(measurements)
    std_error = calculate_standard_error(measurements, mean)
    margin_of_error = student_coef * std_error
    
    # Округление результатов
    std_error = round(std_error, 3)
    margin_of_error = round(margin_of_error, 3)
    rel_error = round((margin_of_error / mean) * 100, 2) if mean != 0 else 0

    # Вывод результатов
    print_separator()
    print(f"Среднее арифметическое: {mean}")
    print(f"Стандартная ошибка (σ): {std_error}")
    print(f"Доверительный интервал (±Δa): {margin_of_error}")
    print(f"Границы доверительного интервала:\n"
          f"- {mean - margin_of_error:.3f} ≤ μ ≤ {mean + margin_of_error:.3f}")
    print(f"Относительная погрешность: {rel_error}%")
    print_separator()

if __name__ == "__main__":
    main()