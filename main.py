import sys
from stats import get_book_text, count_chars

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_text = get_book_text(sys.argv[1]) 
	num_words = len(book_text.split())
	num_chars = count_chars(book_text.lower())

	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char_info in num_chars:
		print(f"{char_info.get('char')}: {char_info.get('num')}")

main()
