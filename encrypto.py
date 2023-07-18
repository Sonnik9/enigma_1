from random import choice
class EnigmaEncrypto:
    def __init__(self, rotor_positions):
        self.rotor_positions = rotor_positions

    def encrypt_number(self, dijit):
        leading_zeros = ""
        remaining_digits = ""

        while len(dijit) > 0 and dijit[0] == "0":
            leading_zeros += dijit[0]  
            dijit = dijit[1:] 

        remaining_digits = dijit
        encrypted_number = int(remaining_digits) ^ self.rotor_positions
        return leading_zeros + str(encrypted_number)   

    def encrypt(self, plaintext):
        ciphertext = ""
        dijit = ""
        simbols_slash = ["@"]
        simbols_qw = ["^", "*"]
        simbols_dott = ["~"]
        simbol_dijit = ["0","1","2","3","4","5","6","7","8","9"]
        for i, char in enumerate(plaintext):
            if char.isalpha():
                char = char.upper()
                position = ord(char) - ord('A')
                encrypted_position = (position + self.rotor_positions) % 26
                encrypted_char = chr(encrypted_position + ord('A'))
                ciphertext += encrypted_char
            elif char==" ":
                ciphertext += choice(simbols_slash)
            elif char=="?":
                ciphertext += choice(simbols_qw)
            elif char==".":
                ciphertext += choice(simbols_dott)
    
            elif char in simbol_dijit:              
                dijit += char
                try:
                    if plaintext[i+1] not in simbol_dijit:
                        
                        ciphertext += self.encrypt_number(dijit)
                        dijit = ''
                except:
                    ciphertext += self.encrypt_number(dijit)
            else:
                ciphertext += char

        return ciphertext

# rotor_positions = 87
# enigma = EnigmaEncrypto(rotor_positions)
# plaintext = "HELLO"
# ciphertext = enigma.encrypt(plaintext)
# print(ciphertext)  # Output: MJQQT