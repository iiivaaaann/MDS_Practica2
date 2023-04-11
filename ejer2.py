import re
pattern= "\\b(E[-]?)?(\d{4})(\s|\-|)([A-Z]{3})\\b"
result=re.findall(pattern, input())
s=""
for i in result:
    print(s.join(i))
