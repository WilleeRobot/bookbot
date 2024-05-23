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

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(num_of_words(file_contents))
    print(num_of_times_character_appears(file_contents))
    



main()