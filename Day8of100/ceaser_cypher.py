#! /usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# -----------------------------------------------------------------------------------------------------------------
# FIXME-1: Solution to all todo's
# TODO-1 nd 2...

def encrypt(text="text", shift="shift"):
    cypher_text = []
    for each_text in text:
        for each_letter in range(len(alphabet)):
            if each_text == alphabet[each_letter]:
                encryption = each_letter + shift
                if encryption >= len(alphabet):
                    encryption -= (len(alphabet) - 1 + 1)
                cypher_text += alphabet[encryption]
                pass
    print("The encoded text is " + "".join(cypher_text))

# TODO-3...
encrypt(text, shift)
