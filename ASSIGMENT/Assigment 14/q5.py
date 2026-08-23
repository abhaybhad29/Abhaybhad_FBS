#Write a Python program to find the longest common prefix of all strings. Use the Python set.
def longest_common_prifix(strings):
    if not strings:
        return ""
    prifix = "" 
    for i  in range(len(strings[0])):
        char = set()

        for strig in strings:
            if i < len(strings):
                char.add(strings[i])

        if len(char) == 1:
            prifix = prifix + strings[0][i]        
        else:
            break

    return prifix
strings = ["flower","flow","flight"]

result = longest_common_prifix(strings)

print("Longest common  prefix:",result)