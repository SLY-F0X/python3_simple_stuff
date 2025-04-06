from tkinter import Tk, Label, Button, filedialog, Entry, StringVar
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

BLOCK_SIZE = 8  # Размер блока для DES
KEY_SIZE = 8    # Размер ключа для DES

class EncryptionApp:
    def __init__(self, window):
        self.window = window
        window.title("DES ECB")
        # Генерация ключа и создание полей ввода в графическом интерфейсе
        self.key = StringVar(window, value=get_random_bytes(KEY_SIZE).hex())
        self.label_block_size = Label(window, text="Размер блока: {} байт".format(BLOCK_SIZE))
        self.label_block_size.pack(pady=4)
        self.label_key_size = Label(window, text="Размер ключа: {} байт".format(KEY_SIZE))
        self.label_key_size.pack(pady=4)
        self.label_key = Label(window, text="Ключ (в HEX формате):")
        self.label_key.pack(pady=4)
        self.entry_key = Entry(window, textvariable=self.key, width=35, borderwidth=1, relief="groove", justify="center")
        self.entry_key.pack(pady=4, anchor='center', expand=True)
        self.generate_key_button = Button(window, text="Сгенерировать новый ключ", command=self.generate_new_key, bg="#4CAF50", fg="white", relief="groove")
        self.generate_key_button.pack(pady=5)
        self.encrypt_button = Button(window, text="Зашифровать файл", command=self.encrypt, bg="#B00000", fg="white", relief="groove")
        self.encrypt_button.pack(pady=5)
        self.decrypt_button = Button(window, text="Расшифровать файл", command=self.decrypt, bg="#FF6800", fg="white", relief="groove")
        self.decrypt_button.pack(pady=5)

    # Генерация нового ключа
    def generate_new_key(self):
        new_key = get_random_bytes(KEY_SIZE).hex()
        self.key.set(new_key)

    # Функция для шифрования файла
    def encrypt(self):
        # Запрос файла для шифрования
        input_file = filedialog.askopenfilename(title="Выберите файл для шифрования")
        # Разделяем путь к файлу на имя и расширение
        input_filename, input_extension = os.path.splitext(input_file)
        # Формируем имя для зашифрованного файла
        suggested_output = input_filename + "_DES" + input_extension
        # Запрашиваем куда сохранить зашифрованный файл
        output_file = filedialog.asksaveasfilename(title="Сохранить зашифрованный файл как", initialfile=suggested_output)
        # Преобразуем ключ из шестнадцатеричного формата в байты
        key = bytes.fromhex(self.key.get())
        # Создаем объект шифрования DES с указанным ключом и режимом ECB
        cipher = DES.new(key, DES.MODE_ECB)
        # Открываем исходный файл для чтения в бинарном режиме
        with open(input_file, 'rb') as f:
            plaintext = f.read()
        # Шифруем содержимое файла и дополняем его до нужного размера блока
        ciphertext = cipher.encrypt(pad(plaintext, BLOCK_SIZE))
        # Записываем зашифрованные данные
        with open(output_file, 'wb') as f:
            f.write(ciphertext)

    # Функция для дешифрования файла
    def decrypt(self):
        input_file = filedialog.askopenfilename(title="Выберите файл для дешифровки")
        input_filename, input_extension = os.path.splitext(input_file)
        suggested_output = input_filename.replace("_DES", "") + input_extension
        output_file = filedialog.asksaveasfilename(title="Сохранить расшифрованный файл как", initialfile=suggested_output)
        key = bytes.fromhex(self.key.get())
        # Создаем объект дешифрования DES с указанным ключом и режимом ECB
        cipher = DES.new(key, DES.MODE_ECB)
        # Открываем зашифрованный файл для чтения в бинарном режиме
        with open(input_file, 'rb') as f:
            ciphertext = f.read()
        # Расшифровываем содержимое файла и удаляем дополнительные байты
        plaintext = unpad(cipher.decrypt(ciphertext), BLOCK_SIZE)
        # Записываем расшифрованные данные
        with open(output_file, 'wb') as f:
            f.write(plaintext)

if __name__ == '__main__':
    root = Tk()
    app = EncryptionApp(root)
    root.mainloop()
