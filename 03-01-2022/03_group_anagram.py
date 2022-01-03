print("""Given an array of strings strs, group the anagrams together. You can return the answer in any order.
         An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
         typically using all the original letters exactly once.""")

words=["eat","cat","ate","tab","tea","bat","tac",]
l=[]

def groupAnagrams(strs):
    result = {}
    for i in strs:
        x = "".join(sorted(i))
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]
    return list(result.values())
ga=groupAnagrams(words)
print(ga)