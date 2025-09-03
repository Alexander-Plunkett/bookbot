def get_word_count(string):
    word_count = string.split()
    return len(word_count)

def get_char_count(string):
    char_count = {}
    lower_string = string.lower()
    for char in lower_string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count