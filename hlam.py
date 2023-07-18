
# def new_func():
#     def encrypt_number(number, key):
#         encrypted_number = number ^ key
#         return encrypted_number

#     def decrypt_number(encrypted_number, key):
#         decrypted_number = encrypted_number ^ key
#         return decrypted_number

# # Пример использования:
#     number = 67
#     key = "1#42d"  # Произвольный ключ произвольной длины

# # Преобразование ключа в числовой формат
#     key_as_int = int.from_bytes(key.encode(), 'big')

# # Шифрование числа
#     encrypted_number = encrypt_number(number, key_as_int)
#     print("Зашифрованное число:", encrypted_number)

# # Дешифрование числа
#     decrypted_number = decrypt_number(encrypted_number, key_as_int)
#     print("Расшифрованное число:", decrypted_number) 

# # new_func()

# # def new_func():
# #     def encrypt_number(number, key):
# #         encrypted_char = chr(number ^ key)
# #         return encrypted_char,'&'

# #     def decrypt_number(encrypted_char, key):
# #         decrypted_number = ord(encrypted_char) ^ key
# #         return decrypted_number

# # # Пример использования:
# #     number = 42
# #     key = 7

# # # Шифрование числа
# #     encrypted_char, simbol_number = encrypt_number(number, key)
# #     print("Зашифрованный символ:", simbol_number)

# # # Дешифрование символа
# #     decrypted_number = decrypt_number(encrypted_char, key)
# #     print("Расшифрованное число:", decrypted_number)


def encrypt_string(string):
    encrypted_chars = []
    for char in string:
        encrypted_char = chr(ord(char) + 1)  # Прибавляем 1 к коду символа
        encrypted_chars.append(encrypted_char)
    encrypted_string = ''.join(encrypted_chars)
    return encrypted_string

def decrypt_string(string):
    decrypted_chars = []
    for char in string:
        decrypted_char = chr(ord(char) - 1)  # Вычитаем 1 из кода символа
        decrypted_chars.append(decrypted_char)
    decrypted_string = ''.join(decrypted_chars)
    return decrypted_string

# Пример использования:
# string1 = "0hello987 how are you?"
# encrypted_string1 = encrypt_string(string1)
# print("Зашифрованная строка:", encrypted_string1)

# decrypted_string1 = decrypt_string(encrypted_string1)
# print("Расшифрованная строка:", decrypted_string1)


