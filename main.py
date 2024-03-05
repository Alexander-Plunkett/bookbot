def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = word_count(text)
    characters_dict = char_count(text)
    characters_list = dict_convert(characters_dict)
    create_report(book_path, num_words, characters_list)

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
        if char in char_dict:
            char_dict[char] += 1
        elif char.isalpha():
            char_dict[char] = 1
    return char_dict

def dict_convert(dict):
    list = []
    for char in dict:
        list.append({"character": char, "occurences": dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list
            
def sort_on(dict):
    return dict["occurences"]

def create_report(path, words, characters):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    for char in characters:
        print(f"The character {char["character"]} was found {char["occurences"]} times")
    print("--- End of report ---")

main()
    
