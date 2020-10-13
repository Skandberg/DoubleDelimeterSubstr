def maxStringWithoutRepeat(word):
    temp_word1= word.lower()
    temp_word2=[]
    for i in temp_word1:
        if i not in temp_word2:
            temp_word2.append(i)
    temp_word1 = ''.join(temp_word2)
    del temp_word2
    return (len(temp_word1))
    

