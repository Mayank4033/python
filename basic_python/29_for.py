line=input("enter one line of text : ")

word=1
for j in line:
    if j==" ":
        word+=1
print("words are : ",word)

vowel=0
for j in line:
    if j=="a" or j=="e" or j=="i" or j=="o" or j=="u" or j=="A" or j=="E" or j=="I" or j=="O" or j=="U":
        vowel+=1
print("vowels are : ",vowel)