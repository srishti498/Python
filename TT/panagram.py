import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase) 
    return alphabet.issubset(set(sentence.lower())) 

print(is_pangram("The quick brown fox jumps over the lazy dog")) 
print(is_pangram("Hello World"))  
