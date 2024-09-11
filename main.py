def main():
    book_path = "books/frankenstein.txt"
    text = getBookText(book_path)

    count_words = getNumWords(text)
    char_freq = character_frequency(text.lower())
    
    char_list = [{"char": char, "num": count} for char, count in char_freq.items()]
    char_list.sort(reverse=True, key=lambda d: d["num"])

    # The Report output
    print(f"Total number of words: {count_words}")
    print("\nCharacter frequency report (sorted by frequency):")
    for entry in char_list:
        print(f"'{entry['char']}': {entry['num']}")

def getBookText(path):
    with open(path) as f:
        return f.read()

def getNumWords(text):
    words = text.split()
    return len(words)

def character_frequency(text):
    freq_dict = {}
    
    for char in text:
        if char.isalpha():
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    
    return freq_dict
        
main()