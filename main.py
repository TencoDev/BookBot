import sys

from stats import count_words
from stats import count_letters
from stats import sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    # file_path = "books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = count_words(file_contents)
    character_count_list = count_letters(file_contents)
    sorted_dict = sort_dict(character_count_list)
    
    
    print("="*28 + "BOOKBOT" + "=" * 28)
    print(f"Analyzing book found at {file_path}... \n")
    print("-" * 11 + " Word Count " + "-" * 11)
    print(f"Found {word_count} total words\n")
    print("-" * 10 + " Character Count " + "-" * 10)
    
    for letter, count in sorted_dict.items():
        if letter.isalpha():
            print(f"{letter}: {count}")
        
    print("=" * 13 + " END " + "=" * 13)
    
    print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()