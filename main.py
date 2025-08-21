import sys
from stats import get_word_count
from stats import get_letter_count
from stats import sort_letters

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    letter_count = get_letter_count(book_text)
    sorted_letters = sort_letters(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_letters:
        char = letter["char"]
        num = letter["num"]
        print(f"{char}: {num}")
    print("============= END ===============")
main()