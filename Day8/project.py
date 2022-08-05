alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art
print(art.logo)

def cypher(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction.lower() == "decode":
        shift_amount *= -1
    for i in range(len(start_text)):
        if start_text[i] not in alphabet:
            end_text += start_text[i]
        else:
            char_loc = alphabet.index(start_text[i])
            shift_index = (char_loc + shift_amount) % 26
            end_text += alphabet[shift_index]
    print(f"The {cipher_direction}d text is {end_text}")

user_input = "yes"
while(user_input.lower() == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cypher(start_text=text, shift_amount=shift, cipher_direction=direction)
    user_input = input("Do you want to continue: ")