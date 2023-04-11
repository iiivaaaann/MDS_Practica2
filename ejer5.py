import re
pattern="\\b(?:C\/|Calle) (\\b[A-ZÑÁÉÍÓÚ]{1}[a-zñíéáóüú]+\\b)(?:,)?(?:\s*)(?:Nº|nº|n|N)?\s*(\d+),\s*(\d{5})\\b"
result=re.findall(pattern, input())
for r in result:
    print(r[2]+"-"+r[0]+"-"+r[1])