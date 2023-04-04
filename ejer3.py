import re
pattern="(.*)\\b(\d{4})-(\d{2})-(\d{2})\\b(.*)"
result=re.findall(pattern, input())
if result:
    print(result[0][0]+result[0][3]+"-"+result[0][2]+"-"+result[0][1]+result[0][4])
