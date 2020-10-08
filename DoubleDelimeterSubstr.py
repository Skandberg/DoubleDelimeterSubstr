def doubleCharDelimeter(word):
    word_list=[char for char in word]
    substr_list=[]
    substr=''
    for index, value in enumerate (word_list):
        substr=substr+value
        if index!=len(word_list)-1:
            
            if value==word_list[index+1]:
                substr_list.append(substr)
                substr=''
        else:
            substr_list.append(substr)
    return max(substr_list,key=len)