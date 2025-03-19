# Define a function to count words in the book
def word_count(text):
    words = text.split()
    return len(words)

char = {}
def char_count(text):
    for character in text.lower():
        if character in char:
            char[character] += 1
        else:
            char[character] = 1
    return char

def sort(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    def sort_on(dict_item):
        return dict_item["count"]

    chars_list.sort(reverse=True, key=sort_on)
    return chars_list