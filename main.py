from encrypto import EnigmaEncrypto
from decrypto import EnigmaDecrypto

def main():
    # plaintext = "&kjf bkj0000000123456789hello987 how are you?"
    # print(f"Исходное значение:____{plaintext}")
    with open("test_text.txt", "r") as f:
        plaintext = f.read().replace('\n', '').replace('\r', '')
    print(plaintext)

    key = "1#jlgukijnf97439hiore0w8@@@@"
    rotor_positions = int.from_bytes(key.encode(), 'big')
    encrypto = EnigmaEncrypto(rotor_positions)

    decrypto = EnigmaDecrypto(rotor_positions)
    
    ciphertext = encrypto.encrypt(plaintext)
    plaintext2 = decrypto.decrypt(ciphertext)
    print("Зашифрованное:", ciphertext)
    print("Расшифрованное:", plaintext2)

if __name__=="__main__":
    main()
