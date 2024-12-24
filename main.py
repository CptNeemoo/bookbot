from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
    char_map = get_character_map(text)
    sorted_dict = sort_dict(char_map)
    
    for k, v in sorted_dict.items():
        print(f"The '{k}' character was found {v} times")

def get_num_words(text):
    return len(text.split())

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def get_character_map(text):
    return Counter(c.lower() for c in text if c.isalpha())

def sort_dict(dictionary):
    return dict(dictionary.most_common())

main()
