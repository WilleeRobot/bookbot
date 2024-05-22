def num_of_words(file):
    return len(file.split())

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(num_of_words(file_contents))
    



main()