def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents

def sort_on(items):
    return items["num"]

def count_chars(text):
	char_count = {}
	items = []

	for text_char in text:
		if text_char.isalpha():
			char_count[text_char] = char_count.get(text_char, 0) + 1
	for ch, n in char_count.items():
		items.append({"char": ch, "num": n})

	items.sort(key=sort_on, reverse=True)
	return items
