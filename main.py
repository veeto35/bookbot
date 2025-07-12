from stats import get_num_words
from stats import get_num_per_letter
from stats import get_sorted_char_list
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = get_num_per_letter(text)
    t = get_sorted_char_list(letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for pair in t:
        if pair['char'].isalpha():
            print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
