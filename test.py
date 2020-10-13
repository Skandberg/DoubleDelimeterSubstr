test_word = 'Bob Marley'
test_word=test_word.lower()
test_word2 = []
for i in test_word:
    if i not in test_word2:
        test_word2.append(i)
test_word1 = ''.join(test_word2)
del test_word2
print(len(test_word1))