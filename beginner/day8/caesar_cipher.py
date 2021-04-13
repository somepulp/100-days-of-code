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

original_alphabet = ['a', 'b', 'c', 'd', 'e']
shift = 1
shifted_alphabet = ['', '', '', '', '']

for i in range(shift, len(original_alphabet)):
    # pos = 5 % shift 
     shifted_alphabet[i-shift] = original_alphabet[i]