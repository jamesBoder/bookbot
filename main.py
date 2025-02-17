def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = string_number()
    print(chars_dict)

def get_num_words(text):
    words = text.split()
    return len(words)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        return (word_count)
        
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

total_words = count_words()

string_dict = string_number()

def sort_on(dict):
    return dict["num"]

def dictionary (string_dict):
    list_of_dicts = []
    for char, count in string_dict.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count} 
            list_of_dicts.append(char_dict)
    list_of_dicts.sort(key=sort_on, reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words()} words found in the document")
    for char_dict in list_of_dicts:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print ("--- End report ---")
        
 
    
    
            
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
if __name__ == "__main__":
    
    
	dictionary(string_dict)
