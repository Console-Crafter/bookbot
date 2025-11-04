from stats import char_count_from_text, get_book_text, book_text_counter, book_character_counter

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = book_text_counter(text)
    num_characters = book_character_counter("books/frankenstein.txt")
    print(text)
    print(f"Found {num_words} total words.")

    # Character frequency count
    char_counts = char_count_from_text(text)
    print("Character frequencies:")
    for char, count in char_counts.items():
        print(f"'{char}': {count}")
    
    print(char_counts)

if __name__ == "__main__":
    main()