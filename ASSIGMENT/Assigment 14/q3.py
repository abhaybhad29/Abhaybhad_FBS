#Write a Python program to find all the unique words and count the
#frequency of occurrence from a given list of strings. Use Python set
#data type.
def find_words(strings):
    words = set()

    for string in strings:
        for word in string.split():
            words.add(word)


    for word in words:
        count = 0

        for string in strings:
            for w in string.split():
                if w == word:
                    count +=1

        print(word,":",count)


strings = [
    "python is easy",
    "python is powerfull",
    "python is easy"

]                            
find_words(strings)

