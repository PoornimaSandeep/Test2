def count_word():
    print("Count words in a string")
    str=input("Enter the string")
    word=str.split()
    search_str=input("enter the word which you want to count")
    print(word.count(search_str))

count_word()