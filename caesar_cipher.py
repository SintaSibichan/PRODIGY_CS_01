def encode(text,key):
    encoded_text=""
    for char in text:
        if char.isupper():
            encoded_text+=chr((ord(char)-ord('A')+key)%26+ord('A'))
        elif char.islower():
            encoded_text+=chr((ord(char)-ord('a')+key)%26+ord('a'))

        else:
            encoded_text+=char
    return encoded_text
def decode(text,key):
    decoded_text=""
    for char in text:

        if char.isupper():
            decoded_text+=chr((ord(char)-ord('A')-key)%26+ord('A'))
        elif char.isupper():
            decoded_text+=chr((ord(char)-ord('a')-key)%26+ord('a'))
        else:
            decoded_text+=char
    return decoded_text        
text=input("enter text to encode")
key=int(input("enter the key value(1-25):"))
encoded_text=encode(text,key)
print("encrypted text ",encoded_text)
decoded_text=decode(text,key)
print("decoded text",decoded_text)
