#Python Program to Detect if Two Strings are Anagrams
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    count1 = {}
    count2 = {}

    for ch in str1:
        count1[ch] = count1.get(ch, 0) + 1

    for ch in str2:
        count2[ch] = count2.get(ch, 0) + 1

    return count1 == count2


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if is_anagram(str1, str2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")