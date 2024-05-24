def num_of_words(file):
    return len(file.split())

def num_of_times_character_appears(text):
    dict_of_characters = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in dict_of_characters:
                dict_of_characters[char] += 1
            else:
                dict_of_characters[char] = 1
    return dict_of_characters

def sort_on(dict):
    return dict["count"]

def main():
    print_report()
    
def print_report():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # Put into a dictionary the number of times each character appears in the document
    letter_dict = num_of_times_character_appears(file_contents)
    # Convert the dictionary into a list of dictionaries
    list_of_characters = []
    for char, count in letter_dict.items():
        list_of_characters.append({"char":char, "count": count})
    # Sort the list of dictionaries by the number of times the character appears
    list_of_characters.sort(reverse=True, key=sort_on)
    
    # Report items
    total_num_of_words = num_of_words(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_num_of_words} words found in the document.")
    print("")
    for item in list_of_characters:
        print(f"The '{item['char']}' character was found {item['count']} times.")


main()