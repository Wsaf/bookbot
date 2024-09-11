def main():
    book_path = "books/frankenstein.txt"
    text = getBookText(book_path)
    print(text)

def getBookText(path):
    with open(path) as f:
        return f.read()

main()