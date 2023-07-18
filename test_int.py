number = "0004"
print(int(number))
key = "0001#42d"  # Произвольный ключ произвольной длины

# Преобразование ключа в числовой формат
key_as_int = int.from_bytes(key.encode(), 'big')

print(key_as_int)


enc = 0 ^ key_as_int

print(enc)