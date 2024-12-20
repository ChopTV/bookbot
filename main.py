# The brains of the operation.
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    words = count_the_words(text)
    # print(words)
    letters = count_the_letters(text)
    # print(letters)
    report(book_path, words, letters)

# Getting the text from the file and returning it as a useable variable
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Calculating the number of words within the given text file
def count_the_words(text):
    book = str(text).split()
    words = 0
    for word in book:
        words += 1
    return words

# Calculating the distribution of characters within a given text file
def count_the_letters(text):
    book = str(text).lower()
    letter_count = {}
    for letter in book:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

# Generate a report on the analysis of the given text file.
def report(path, words, letters):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document\n")
    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
    for letter in sorted_letters:
        if letter[0].isalpha():
            print("The '" + letter[0] + "' character was found " + str(letter[1]) + " times")
    print("--- End report ---")

main()
