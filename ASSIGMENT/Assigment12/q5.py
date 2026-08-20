#Python Program to Count the Number of Vowels in a String
def count_vowels(s):
    count = 0

    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1

    return count


string = input("Enter a string: ")

print("Number of vowels:", count_vowels(string))        