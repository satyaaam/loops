word = input("Enter a character: ")
vowels = 0
consonents = 0
for s in word:
    if s.isalpha():
        if s in "aeiouAEIOU":
            vowels += 1
        else:
            consonents += 1
print("Vowels:", vowels)
print("Consonents:", consonents)
