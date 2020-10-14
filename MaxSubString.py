def maxSubStringWithoutRepeat(word):
    temp_word=[]
    for i in list(word.lower().strip()):
        if i not in temp_word:
            temp_word.append(i)    
    return (len(temp_word))
    

