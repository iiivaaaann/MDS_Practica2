import re
pattern="(\\b[0-9]{4}\\b)"
result=re.findall(pattern, input())

for i in result:
    print(str(i).replace(' ',''))