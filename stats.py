

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


    