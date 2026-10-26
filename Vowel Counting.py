#Part a(i):
def IterativeVowels(value):
    count = 0
    for char in value:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count = count + 1
    return count

#Part a(ii):
print(IterativeVowels("house"))

#Part b(i):
def RecursiveVowels(value):
    if value == "":
        return 0
    FirstCharacter = value[0]
    if FirstCharacter == "a" or FirstCharacter == "e" or FirstCharacter == "i" or FirstCharacter == "o" or FirstCharacter == "u":
        return 1 + RecursiveVowels(value[1:])  # value[1:] will return the entire string without the first character in the sring and this will go on until last string is ""
    else:
        return RecursiveVowels(value[1:])

#Part b(ii):
print(RecursiveVowels("imagine"))
