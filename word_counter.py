sentence = input("Enter a sentence: ")
word_count = 0
for char in sentence:
    if char == " ":
        word_count += 1
word_count += 1
print("The number of words in the sentence is:",word_count)