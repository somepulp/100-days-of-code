# This program enables the user to encode or decode text, by shifting each letter of the alphabet by a pre-determined amount

from art import logo 

# Part 1 - Encryption
# initial ideas:
#- % 26 is essential for shifts > 26 - right
#- while loop - to allow the user ot continue -- while continue = yes.. continue.. 
#- need two alphabets? one is the original, one is the shifted.. they both should have the same length.. - not needed..

def caesar(text, shift, direction):
        if not (direction == "encode" or direction == "decode"):
            print("I dont know what you want to do. Select either 'encode' or 'decode' for the direction ")

        else:
            new_text = ""
            modulo_shift = shift % 26
            if direction == "decode":
                modulo_shift *= -1
            
            for letter in text:
                position = alphabet.index(letter)
                new_text += alphabet[(position + modulo_shift) % 26]
                
            print(f"The {direction}d text is {new_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Import and print the logo from art.py when the program starts.
print(logo)

caesar(text,shift,direction)

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
# --- already done this xD 

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
# - validated while loop idea 

