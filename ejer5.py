import re
pattern="\\b(?:C\/|Calle) (\\b[A-Z]{1}[a-zñ]+\\b)(?:,)?(?:\s+)(?:N|n)?(?:º\s*)?(\d+)(?:,)(?:\s+)(\d{5})\\b"
result=re.findall(pattern, input())
for r in result:
    print(r[2]+"-"+r[0]+"-"+r[1])