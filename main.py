from stats import get_word_count, get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()
    return book_string

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"{get_word_count(book_text)} words found in the document")
    print(get_char_count(book_text))

main()