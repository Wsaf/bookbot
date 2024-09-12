from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = read_book_text(book_path)

    count_words = count_words_in_text(text)
    char_freq = get_character_frequency(text.lower())
    
    char_list = [{"char": char, "num": count} for char, count in char_freq.items()]
    char_list.sort(reverse=True, key=lambda d: d["num"])

    # The Report output
    print(f"Total number of words: {count_words}")
    print("\nCharacter frequency report (sorted by frequency):")
    for entry in char_list:
        print(f"'{entry['char']}': {entry['num']}")

def read_book_text(path):
    with open(path) as f:
        return f.read()

def count_words_in_text(text):
    words = text.split()
    return len(words)

def get_character_frequency(text):
    return Counter(char for char in text if char.isalpha())
        
main()