def generate_code(sentence):

    sentence = sentence.replace(" ", "").lower()
    
    code = ""
    for char in sentence:
        ascii_value = ord(char)
        random_number = ascii_value % 10
        code += str(ascii_value) + str(random_number)
    
    return code

def main():
    sentence = input("Enter a sentence: ")
    code = generate_code(sentence)
    print("Unique Code:", code)

if __name__ == "__main__":
    main()
