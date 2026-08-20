#Python Program to count the occurrences of ach word in a string.
def countWord(string):
    words = string.split()
    count = {}

    for word in words :
        if word in count:
            count[word] +=1
        else:
            count[word] = 1

    return count

str1 = input("Enter the string : ")
result = countWord(str1)
print("word occurrences : ")
for word in result:
    print(word,":",result[word])             