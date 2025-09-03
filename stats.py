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

def sort_on(items):
    return items["num"]

def sort_char_count(dict):
    char_count = []
    for char in dict:
        count = dict[char]
        char_count.append({"char": char, "num": count})
    char_count.sort(reverse=True, key=sort_on)
    return char_count

