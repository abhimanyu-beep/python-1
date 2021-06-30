name = input("Enter Your Introduction :")
print(name)

charectercount=0
wordcount=1
for i in name :
    charectercount=charectercount+1
    

    if(i==" "):
        wordcount=wordcount+1

print("number of word in the string:")
print(wordcount)
print("number of charecter in the string")
print(charectercount)