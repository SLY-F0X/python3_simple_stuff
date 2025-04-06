import tkinter as tk
import numpy as np
import sys
import os


def parse_matrix(text):
    try:
        matrix = np.array([[float(num) for num in row.split()]
                           for row in text.strip().split('\n')])
        return matrix
    except ValueError:
        entry = text.strip("■()\n")
        rows = entry.split("@")
        matrixW = [row.replace(',', '.').split("&") for row in rows]
        matrixW = [[float(value) for value in row] for row in matrixW]
        return np.array(matrixW)


def maximal_operation():
    A = parse_matrix(entry_a.get("1.0", "end-1c"))
    B = parse_matrix(entry_b.get("1.0", "end-1c"))
    if A is None or B is None:
        result_label.config(text="Данные не введены")
        return
    R0 = np.zeros_like(A)
    for i in range(len(A)):
        for e in range(len(A)):
            R = [min(A[i][g], B[g][e]) for g in range(len(A))]
            R0[i][e] = max(R)
    result_label.config(text=f"Максимильное:\n{R0}")


def minimax_operation():
    A = parse_matrix(entry_a.get("1.0", "end-1c"))
    B = parse_matrix(entry_b.get("1.0", "end-1c"))
    if A is None or B is None:
        result_label.config(text="Данные не введены")
        return
    R0 = np.zeros_like(A)
    for i in range(len(A)):
        for e in range(len(A)):
            R = [max(A[i][g], B[g][e]) for g in range(len(A))]
            R0[i][e] = min(R)
    result_label.config(text=f"Минимаксное:\n{R0}")


def max_multiplicative_operation():
    A = parse_matrix(entry_a.get("1.0", "end-1c"))
    B = parse_matrix(entry_b.get("1.0", "end-1c"))
    if A is None or B is None:
        result_label.config(text="Данные не введены")
        return
    R0 = np.zeros_like(A)
    for i in range(len(A)):
        for e in range(len(A)):
            R = [A[i][g] * B[g][e] for g in range(len(A))]
            R0[i][e] = max(R)
    result_label.config(text=f"Максимультипликативное:\n{R0}")


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))


def change_format():
    current_text = result_label.cget("text")
    try:
        matrix_str = current_text.split('\n', 1)[1]
        matrix = np.fromstring(matrix_str.replace(
            '\n', ' ').replace('[', '').replace(']', ''), sep=' ')
        matrix = matrix.reshape((3, 3))
        formatted_matrix = '■(' + '@'.join('&'.join(
            f'{num:.1f}'.replace('.', ',') for num in row) for row in matrix) + ')'
        result_label.config(text=f"\n{formatted_matrix}")

        root.clipboard_append(result_label.cget("text"))
    except Exception:
        return


root = tk.Tk()
root.title("Калькулятор нечетких множеств")
root.geometry("370x440")
root.attributes('-alpha', 0.95)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

label_a = tk.Label(root, text="Множетсво A:",fg="black", bg="#fffff0")
label_a.pack()
entry_a = tk.Text(root, height=5, width=40, bg="#fffff0", fg="black")
entry_a.pack()

label_b = tk.Label(root, text="Множество B:",fg="black", bg="#fffff0")
label_b.pack()
entry_b = tk.Text(root, height=5, width=40, bg="#fffff0", fg="black")
entry_b.pack()

button_maximal = tk.Button(root, text="Максиминное",
                           command=maximal_operation, bg="#4CAF50", fg="white", relief="groove")
button_maximal.pack(fill='x', expand=True)

button_minimax = tk.Button(root, text="Минимаксное",
                           command=minimax_operation, bg="#B00000", fg="white", relief="groove")
button_minimax.pack(fill='x', expand=True)

button_max_multiplicative = tk.Button(
    root, text="Максимультипликативное", command=max_multiplicative_operation, bg="#FF6800", fg="white", relief="groove")
button_max_multiplicative.pack(fill='x', expand=True)

result_label = tk.Label(root, text="Здесь будет результат расчетов",fg="black")
result_label.pack(fill='x')

copy_button = tk.Button(root, text="Скопировать результат",
                        command=copy_to_clipboard, bg="light grey", fg="chocolate", relief="groove")
copy_button.pack(fill='x')

format_button = tk.Button(
    root, text="Вставка в WORD \n Вставить уравнение в проефссиональном виде в ворд", command=change_format, bg="#EB0C0C", fg="white", relief="groove")
format_button.pack(fill='x')

root.mainloop()
