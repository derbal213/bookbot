def get_word_count(book_text):
    words = book_text.split()
    return len(words)


#Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
#Convert any character to lowercase using the .lower() method, we don't want duplicates.
#Use a dictionary of String -> Integer. The returned dictionary should look something like this:
def get_letter_count(book_text):
    letter_counts = {}
    #letters = list(book_text)
    for l in book_text:
        l = l.lower()
        if l.isalpha():
            if l in letter_counts:
                letter_counts[l] += 1
            else:
                letter_counts[l] = 1
    return letter_counts

def sort_on(items):
    return items["num"]

def sort_letters(letter_counts):
    letter_dicts = []
    for l in letter_counts:
        char = l
        num = letter_counts[l]
        letter = {
            "char": l,
            "num": num
        }
        letter_dicts.append(letter)
    letter_dicts.sort(reverse=True, key=sort_on)
    return letter_dicts
    r#eturn sorted(letter_dicts, reverse=True, key=lambda d: d["num"])