encrypted_string = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
reversed_alphabet = alphabet[::-1]
decryption_dict = {alphabet[i]: reversed_alphabet[i] for i in range(len(alphabet))}

decrypted_string = ''.join(decryption_dict[char] for char in encrypted_string)

print(decrypted_string) 
