import sys

from stats import (
    char_count_from_text,
    sorted_alpha_counts,
    get_book_text,
    book_text_counter,
    book_character_counter,
    report_printout,
)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    num_words = book_text_counter(text)
    num_characters = book_character_counter(book)

    # Character frequency count
    char_counts = char_count_from_text(text)             
    sorted_report = sorted_alpha_counts(char_counts)       

    # Existing output

    print(text)
    print(f"Found {num_words} total words.")

    # Print the sorted character report
    print("Character report")
    print(sorted_report)


    report_printout(book, text)

    print(sys.argv)

if __name__ == "__main__":
    main()