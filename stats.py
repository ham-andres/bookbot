def word_in_book(text):
    words = text.split()
    return words

def count_characters(text):
    char_count = {}
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch in char_count:
            char_count[lower_ch] +=  1

        else:
            char_count[lower_ch] = 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_report(char_dict):
    chars_list = []
    for ch,count in char_dict.items():
        small_dict = {"char": ch, "num": count}
        chars_list.append(small_dict)
    chars_list.sort(reverse=True, key= sort_on)
    return chars_list