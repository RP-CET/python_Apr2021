#This is to "split" the words in a String like "someWordsHere" into "some" "Words" "Here"

z = "findLongestWord"

words = []

start = 0
for i in z:
    if i.isupper() == True:
        pos = z.index(i)
        word = z[start:pos]
        start = pos 
        
        words.append(word)

word = z[start:]
words.append(word)

print (words)
        