print('Система шифрования Трисемуса')

def create_trisemus_table(table_key):
    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    table_key = table_key.lower()
    table = ""

    for char in table_key:
        if char not in table and char in alphabet:
            table += char
            alphabet = alphabet.replace(char, '')

    table += alphabet

    return [table[i:i + 8] for i in range(0, 32, 8)] # Меняем размер строки 8

def trisemus(text, table_key, encryption=True):
    table = create_trisemus_table(table_key)
    result = ""

    for char in text.lower():
        if char == " ":
            result += " "
            continue
        
        found = False
        for i, row in enumerate(table):
            if char in row:
                if encryption:
                    new_row_index = (i + 1) % len(table)
                else:  # Для дешифрования
                    new_row_index = (i - 1) % len(table)

                result += table[new_row_index][row.index(char)]
                found = True
                break
        
        if not found:
            result += char
            # Если символа нет в таблице, просто добавляем его к результату

    return result

print(" 1 - Зашифровать сообщение по системе Трисемуса")
print(" 2 - Расшифровать по ключу")

choose_your_destiny = int(input("ВЫБОР №: "))

if choose_your_destiny == 1:
    text = input("Введите текст: ")
    table_key = input("Введите ключ-слово: ")
    encrypted_text = trisemus(text, table_key)
    print(f'Таблица Трисемуса: {create_trisemus_table(table_key)}')
    print(f'Зашифрованный текст: {encrypted_text.upper()}')
    decrypted_text = trisemus(encrypted_text, table_key, encryption=False)
    print(f'Оригинальный текст: {decrypted_text.upper()}')
    input("")
    
if choose_your_destiny == 2:
    text = input("Введите шифрованный текст: ")
    table_key = input("Введите ключ-слово: ")
    decyph_text = trisemus(text, table_key, encryption=False)
    print(f'Расшифровка: {decyph_text.upper()}')
    input("")
else:
    exit()
