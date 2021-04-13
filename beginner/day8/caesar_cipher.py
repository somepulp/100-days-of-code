# This is a method of encoding text, by shifting each letter of the alphabet by a pre-determined amount

#instructions for using: 
# ask user whether they want to 'encode' or 'decode' a message
# ask user to type the message
# print the result of your encryption or decryption
# allow them to continue the program if they choose

# Part 1 - Encryption
# initial ideas:
#- % 26 is essential for shifts > 26
#- while loop - to allow the user ot continue -- while continue = yes.. continue.. 
#- need two alphabets? one is the original, one is the shifted.. they both should have the same length..

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        cipher_text += alphabet[(alphabet.index(letter) + (shift % 26)) % 26]
    print(f"The encoded text is {cipher_text}")
     #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

encrypt("hello", 5)