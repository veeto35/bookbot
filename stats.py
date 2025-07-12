def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_per_letter(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(items):
    return items['num']


def get_sorted_char_list(letters):
    final = []
    for letter in letters:
        final.append({'char': letter, 'num': letters[letter]})
    final.sort(reverse=True, key=sort_on)
    return final