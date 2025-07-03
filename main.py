import sys
from stats import word_count, ch_count, dict_sort, sort_on



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]


    result = get_book_text(filepath)
    result1 = word_count(result)
    result2 = ch_count(result)
    
        
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(result1)
    print("--------- Character Count -------")
    result3 = dict_sort(result2)
    for i in result3:
        if i["char"].isalpha():
            print(i["char"] + ": " + str(i["num"]))
    print("============= END ===============")


main()