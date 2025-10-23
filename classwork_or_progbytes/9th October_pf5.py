#word = input("Please enter a string: ")
#for count in range(len(word)-1):
    #while len(word[count:]) <= 2 and len(word[:count]) <=2:
        #print(word[count:])


word = input("Please enter a string: ")
word2 = input("Please enter another string: ")

if word > word2:
    print(word + " is greater than " + word2)

if word2 > word:
    print(word2 + " is greater than " + word)

elif word == word2:
    print("These are the same value :c")

