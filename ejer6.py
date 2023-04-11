import re
pattern="(?:\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{3}\s+)(\w+)(?:\s+\d+ --- )(?:\[)(\w+)(?:\]\s+)(?:\w+\.){0,}(\w+)(?:\s+:\s+)(.*)"
result=re.findall(pattern, input())
for r in result:
    print("\""+r[0]+"\",\"" +r[1]+"\",\""+r[2]+"\",\""+r[3]+"\"")