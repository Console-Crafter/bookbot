

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()
    
def book_text_counter(book_text):
    words = book_text.split()
    return len(words)

def book_character_counter(filepath):
    with open(filepath, "r") as file:
        return file.read()
    
def char_count_from_text(book_text):
    
    counts = {}
    if book_text is None:
        return counts
    book_text = book_text.lower()
    for char in book_text:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sorted_alpha_counts(counts_dict):

    result = []
    if not counts_dict:
        return result

    for ch, num in counts_dict.items():

        if isinstance(ch, str) and ch.isalpha():
            result.append({"char": ch, "num": num})

    # helper
    def _get_num(entry):
        return entry["num"]

    # sort in-place from greatest to lowest
    result.sort(key=_get_num, reverse=True)
    return result

def report_printout(book_path, text):
    # Word count
    num_words = book_text_counter(text)

    # Character counts
    char_counts = char_count_from_text(text)
    sorted_report = sorted_alpha_counts(char_counts)

    # Print header and word count
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_report:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")