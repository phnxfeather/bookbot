import stats 
import sys

# Define get_book_text function

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()


# Define the main function
def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    # Get the book path from command-line arguments
    book_path = sys.argv[1]
    
    # Use your existing get_book_text function instead of opening the file directly
    file_contents = get_book_text(book_path)

    # Get the statistics
    word_count = stats.word_count(file_contents)
    char_counts = stats.char_count(file_contents)
    sorted_chars = stats.sort(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print each character count, skipping non-alphabetical characters
    for char_data in sorted_chars:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['count']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()