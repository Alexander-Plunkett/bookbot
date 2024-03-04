def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    characters = char_count(text)
    print(characters)

def get_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return len(words)

def char_count(book):
    char_dict = {}
    lower_string = book.lower()
    for char in lower_string:
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


main()
    
