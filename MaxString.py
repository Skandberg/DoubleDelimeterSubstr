def maxStringWithoutRepeat(word):

    word_to_chars_list=[char for char in word.lower()]
    max_size=0
    while len(word_to_chars_list)!=0:
        alphabet=set(word_to_chars_list)
        min_pos=len(word_to_chars_list)-1

        count=0
        for index1, value1 in enumerate(alphabet):
            count=0
            for index2, value2 in enumerate(word_to_chars_list):
                if value1==value2:
                    count+=1
                    if count>1:
                        if index2<min_pos:              
                            min_pos=index2-1
            
                            break
        if min_pos+1>max_size:
            max_size=min_pos+1
        del word_to_chars_list[0]
        
            
    return max_size
    

