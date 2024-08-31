str1='HackerRank.com presents "Pythonist 2".'
str2=[]
str3=''
for i in str1:
    if(i.isupper()):
        str2.append(i.lower())
    else:
        str2.append(i.upper())

for j in str2:
    str3+=j 
print("".join(str2))
   