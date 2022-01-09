print("Write a recursive function that takes an list of words and returns "
      "an list that contains all the words capitalized.")
l=['poornima','Suma','sandeep','sowmya']

def capitalizeWords(l):
    if len(l) == 0:
        return []
    else:
        return [l[0].upper()]+capitalizeWords(l[1:])

a=capitalizeWords(l)
print(a)