from morse_code_dict import morse_code_dict

def text_to_morse(text):
    return ' '.join([morse_code_dict.get(char.upper(), char) for char in text])



if __name__ == "__main__":
    message = input("Enter a word or sentence to convert into Morse Code: ")
    print(text_to_morse(message))
