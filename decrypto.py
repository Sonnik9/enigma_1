
class EnigmaDecrypto:
    def __init__(self, rotor_positions):
        self.rotor_positions = rotor_positions
        
    def decrypt_number(self, dijit):
        leading_zeros = ""
        remaining_digits = ""

        while len(dijit) > 0 and dijit[0] == "0":
            leading_zeros += dijit[0]  
            dijit = dijit[1:] 

        remaining_digits = dijit
        decrypted_number = int(remaining_digits) ^ self.rotor_positions
        return leading_zeros + str(decrypted_number) 

    def decrypt(self, ciphertext):
        plaintext = ""
        dijit = ''
        simbols_slash = ["@"]
        simbols_qw = ["^", "*"]
        simbols_dott = ["~"]
        simbol_dijit = ["0","1","2","3","4","5","6","7","8","9"]
       
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                char = char.upper()
                position = ord(char) - ord('A')
                decrypted_position = (position - self.rotor_positions) % 26
                decrypted_char = chr(decrypted_position + ord('A'))
                plaintext += decrypted_char
            elif char in simbols_slash:
                plaintext += " "
            elif char in simbols_qw:
                plaintext += "?"
            elif char in simbols_dott:
                plaintext += "."

            elif char in simbol_dijit:              
                dijit += char
                try:
                    if ciphertext[i+1] not in simbol_dijit:
                        plaintext += self.decrypt_number(dijit)
                        dijit = ''
                except:
                    # print(dijit)
                    plaintext += self.decrypt_number(dijit)

            else:
                plaintext += char

        return plaintext

# rotor_positions = 5
# enigma = EnigmaDecrypto(rotor_positions)
# ciphertext = "MJQQT"
# plaintext = enigma.decrypt(ciphertext)
# print(plaintext)  # Output: HELLO