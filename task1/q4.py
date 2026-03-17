word=input("enter word")
output=[]
for i in word:
    thing=ord(i)
    otherthing=(bin(thing)[2:])
    output+=otherthing
print(output)
