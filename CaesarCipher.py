alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    answer = ""
    if direction == "encode":
        for char in text:
            if char not in alphabet:
                answer += char
            else:
                answer += alphabet[alphabet.index(char) + shift]
        print(f"The encoded text is {answer}")
    elif direction == "decode":
        for char in text:
            if char not in alphabet:
                answer += char
            else:
                answer += alphabet[alphabet.index(char) - shift]
        print(f"The decoded text is {answer}")
    else:
        print("Enter a proper direction")


yes = True
while yes:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift %= 26

    caesar(text=text, direction=direction, shift=shift)
    option = input("Would you like to decipher another message? Type 'yes' or 'no' ")
    if option == "no":
        yes = False
    else:
        pass
