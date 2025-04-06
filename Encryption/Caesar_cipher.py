print("Шифр Цезаря")
def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        # Проверяем, является ли символ буквой
        if char.isalpha():
            # Определяем, является ли символ заглавной буквой
            if char.isupper():
                # Получаем номер буквы в алфавите (A -> 0, Б -> 1, ...)
                char_num = ord(char) - ord('А')
                # Применяем сдвиг и берем остаток от деления на размер алфавита
                new_char_num = (char_num + shift) % 32
                # Получаем новую заглавную букву по номеру в алфавите
                new_char = chr(new_char_num + ord('А'))
            else:
                # Аналогично для строчных букв
                char_num = ord(char) - ord('а')
                new_char_num = (char_num + shift) % 32
                new_char = chr(new_char_num + ord('а'))
        else:
            # Если символ не является буквой, сохраняем его без изменений
            new_char = char
        
        # Добавляем символ к результату
        result += new_char
    
    return result

text = input("Введите текст ")
shift = int(input("Введите сдвиг "))
caesar_result = caesar_cipher(text, shift)

print("Шифр Цезаря:")
print(caesar_result)

print("*"*10,"Дешифровка", sep='\n')
text = input("Введите зашифрованный текст ")
shift = int(input("Введите сдвиг "))
caesar_decipher = caesar_cipher(text, -shift)
print("Расшифрованное сообщение:")
print(caesar_decipher)
input('')
