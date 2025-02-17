def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print (word_count)
        
def string_number():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        case_lower = file_contents.lower()
        char_count = {}
        for i in case_lower:
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
    return char_count

string_dict = string_number()
            
        
    
if __name__ == "__main__":
    
    print(string_dict)
