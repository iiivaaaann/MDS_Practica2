import re
pattern= "\\b(E[-]?)?(\d{4})(\s|\-|)([A-Z]{3})\\b"
result=re.findall(pattern, input())
print(result)
for i in result:
    s=""
    print(s.join(i))
