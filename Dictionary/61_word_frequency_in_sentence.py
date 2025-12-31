# 61. Word Frequency in Sentence
# Input: "this is a test this is"
# Output: {'this':2, 'is':2, 'a':1, 'test':1}

sentence = "this is a test this is"
words = sentence.split()
d = {}
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)

