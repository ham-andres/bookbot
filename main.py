import sys
from stats import word_in_book, count_characters,sort_report

def get_book_text(path):
    with open(path) as f:
        return f.read()



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    # print(text)
    number_of_word = len(word_in_book(text))
    
    # print(f"Found {number_of_word} total words")
    count_of_char = count_characters(text)
    # print(count_of_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_word} total words")
    print("--------- Character Count -------")
    body = sort_report(count_of_char)
    for item in body:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    print("============= END ===============")
    

main()