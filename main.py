def letter_counts(file_contents):
    counts = {}
    lowered_string = file_contents.lower()

    for char in lowered_string:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def sort_on(dict):
    return dict["num"]

characters =[]
dictionary = {}




def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    words = file_contents.split()
    word_count = len(words)

    result = letter_counts(file_contents)

    char_list = []
    for char, num in result.items():
        char_list.append({"char": char, "num": num})

    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict["num"]} times")

    print("--- End Report ---")




main()



