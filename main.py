def main():
    book_path = "books/frankenstein.txt"
    text = getBookText(book_path)

    count_words = getNumWords(text)
    print(f"{count_words} words found in the book")

    char_freq = character_frequency(text.lower())
    print("Character frequency in the book:")
    for char, freq in char_freq.items():
        print(f"'{char}': {freq}")

def getBookText(path):
    with open(path) as f:
        return f.read()

def getNumWords(text):
    words = text.split()
    return len(words)

def character_frequency(text):
    freq_dict = {}
    
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    return freq_dict
        
main()