from stats import get_num_words
from stats import count_characters
from stats import sort_characters
import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        return f.read()

def print_report(path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) == 1 :
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    path = sys.argv[1]
    print(path)

    text = get_book_text(path)
    num_words = get_num_words(text)
    character_counts = count_characters(text)
    print_report(path, num_words, sort_characters(character_counts))

if __name__ == "__main__":
    main()
