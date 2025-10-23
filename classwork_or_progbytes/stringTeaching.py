word = "Hello World, this is me, I am very cheerful. TODAY!!!"
name = "jahmai"
# concatenation
print(word+": "+name)

# string length
print( len(word) ) 

# uppercase
print( name.upper() )
# lowercase
print( word.lower() )

# capitalize
print( name.capitalize() )
print("hello".capitalize() )
print(word.capitalize() )
 
# ascii
letterAscii = ord("a")
print(letterAscii)
letterAscii = ord("b")
print(letterAscii)
letterAscii = ord("%")
print(letterAscii)
letterAscii = ord("5")
print(letterAscii)

numberAscii = chr(97)
print(numberAscii)


# first character
print("hello"[0])
print(name[0])
print(word[0].lower())

# last character

print( name[len(name) - 1] )

# substrings .substring(x , i)
print( "computer"[0:3] )
print( "computer"[3:4] ) # 

# .left(i) .right(i)

print( "computer"[:4] ) # left first 4 characters
print( "computer"[4:] ) # right last 4 characters

# split a string into an array/list
print( (word.split(",")) )