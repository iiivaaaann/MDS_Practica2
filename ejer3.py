import re
pattern="\\b(\d{4})-(\d{2})-(\d{2})\\b"
frase=input()
result=re.findall(pattern, frase)
for i in result:
    oldDate=str(i[0])+'-'+str(i[1])+'-'+str(i[2])
    newDate=str(i[2])+"."+str(i[1])+"."+str(i[0])
    frase=frase.replace(oldDate, newDate)
print(frase)

