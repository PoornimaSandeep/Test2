def unique_alphanum():
    print("Sort unique words alphanumerically")
    str=input("please enter the str")
    words=str.split()
    alpha_num_words =[]
    for i in words:
        if i.isalnum():
            if i not in alpha_num_words:
               alpha_num_words.append(i)
    alpha_num_words=sorted(alpha_num_words)
    print(alpha_num_words)


unique_alphanum()