print("""Given a sentence text (A sentence is a string of space-separated words) in the following format:
          First letter is in upper case.
          Each word in text are separated by a single space.
          Your task is to rearrange the words in text such that all words are rearranged in an increasing order of 
          their lengths. If two words have the same length, arrange them in their original order.""")
str=input("please enter the string")


def rearrange_words(str):
    l=str.split()
    d={}
    l2=[]
    for i in l:
        v=len(i)
        d[i]=v

    for i in sorted(d.values()):
        for k,j in d.items():
            if i==j:
               if k not in l2:
                   l2.append(k)
    for i in l2:
        print(i,end=" ")


rearrange_words(str)