#Write a Python program to find all the anagrams and group them together from a given list of strings.
def group_anagrams(words):
    group = {}


    for word in words:
        key = ''.join(sorted(word))


        if key not in group:
            group[key]=[]

        group[key].append(word)
    return list(group.values())
words = ["eat","tan","tea","ate","nat","bat","listen","silent"]
result = group_anagrams(words)
print("Anagram group:")
for group in result:
    print(group)