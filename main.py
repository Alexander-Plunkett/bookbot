import sys
from stats import get_word_count, get_char_count, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()
    return book_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    sorted_char_count = sort_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()