import re
pattern="(?:\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{3}\s+INFO\s+\d+ --- )(?:\[)(\w+)(?:\]\s+)(?:\w+\.){1,}(\w+)(?:\s+:\s+)(.*)"
result=re.findall(pattern, input())
for r in result:
    print("\"INFO\",\"" +r[0]+"\",\""+r[1]+"\",\""+r[2]+"\"")