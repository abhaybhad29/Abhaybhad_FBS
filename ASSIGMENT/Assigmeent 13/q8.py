#Python Program to Count the Frequency of Words Appearing in a String Using
#a Dictionary
def word_frequency(string):
    words = string.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    return frequency


string = input("Enter a string: ")

result = word_frequency(string)

print("Word Frequency:", result)