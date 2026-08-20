#Python Program to Calculate the Number of Words and the Number of
#Characters Present in a String
def count_words_characters(s):
    words = 0
    characters = 0
    in_word = False

    for ch in s:
        if ch != " ":
            characters += 1

            if not in_word:
                words += 1
                in_word = True
        else:
            in_word = False

    return words, characters


string = input("Enter a string: ")

words, characters = count_words_characters(string)

print("Number of words:", words)
print("Number of characters:", characters)