import hashlib

def generate_unique_code(sentence):
   
    sentence = sentence.replace(" ", "").lower()
   
    unique_code = hashlib.sha256(sentence.encode()).hexdigest()
    
    return unique_code

sentence = input("Enter a sentence: ")
print("Unique code:")
print(generate_unique_code(sentence))
