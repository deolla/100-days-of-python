from art import logo

print(logo)
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
print("Welcome to Caesar Cipher!")


def caesar(texts, shifts):
    """encrypt or decrypt message"""
    cipher = ""
    if direction == "encode":
        for i in texts:
            if i in alphabet:
                alphabet_index = alphabet.index(i)
                new_index = alphabet_index + shifts
                cipher += alphabet[new_index]
            else:
                cipher += i
        print(f"The encoded text is {cipher}")

    elif direction == "decode":
        for i in texts:
            if i in alphabet:
                alphabet_index = alphabet.index(i)
                new_index = alphabet_index - shifts
                cipher += alphabet[new_index]
            else:
                cipher += i
        print(f"The decoded text is {cipher}")
    else:
        print("Invalid input")


# or
# def ceasar(texts=text, shifts=shift, cipher_direction):
#     """encrypt or decrypt message"""
#     end_text = ""
#     if cipher_direction == "decode":
#         shifts *= -1
#     for i in texts:
#         alphabet_index = alphabet.index(i)
#         new_index = alphabet_index + shifts
#         end_text += alphabet[new_index]
#     print(f"The {cipher_direction}d text is {end_text}")


continues = True
while continues:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(texts=text, shifts=shift)
    shift = shift % 26

    cont = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if cont == "no":
        continues = False
        print("Goodbye")
