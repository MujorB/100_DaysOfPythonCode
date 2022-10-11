#! /usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def ceaser(direction="direction", text="text", shift="shift"):
    cypher_text, message = "", ""
    for each_text in text:
        position = alphabet.index(each_text)
        if direction == "encode":
            message = "The encoded text is "
            position += shift
        elif direction == "decode":
            message = "The decoded test is "
            position -= shift
        cypher_text += alphabet[position]
    print(message + cypher_text)
    
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

ceaser(direction=direction, text=text, shift=shift)