import re

#Ejer 1

"""p=re.compile('([^0-9]|^)([0-9]{4})([^0-9]|$)')
a=input()
years=p.findall(a)
for year in years:
    print(year[1])"""

#Ejer 2

"""
p=re.compile('\\b(E{0,1})(\s|[-]|)([0-9]{4})(\s|[-]|)([A-Z]{3})\\b')
a=input()
licenses=p.findall(a)
for l in licenses:
    print(l[1]+l[2]+l[3]+l[4]+l[5]) """

"""#Ejer 3
#p=re.compile('(\s|^)([0-9]{4})[-]([0-9]{2})[-]([0-9]{2})(\s|$)')
a=input()
dates=re.search(r'([^0-9]|^)([0-9]{4})[-]([0-9]{2})[-]([0-9]{2})([^0-9]|$)',a)
while dates:
    if dates:
        dates = dates.group()
        aux=''
        if dates[0]==' ':
            aux+=' '
        aux += dates[9:11] + '.' + dates[6:8] + '.' + dates[1:5]
        if dates[-1]==' ':
            aux+=' '
        a = a.replace(dates, aux)
    dates = re.search(r'(\s|^)([0-9]{4})[-]([0-9]{2})[-]([0-9]{2})(\s|$)', a)

print(a)"""

"""dates=p.findall(a)
#print(dates)
original=""
new=""

for date in dates:
    original=date[1]+'-'+date[2]+'-'+date[3]
    new = date[3] + '.' + date[2] + '.' + date[1]
    a=a.replace(original,new)

print(a)"""

"""#Ejer 4

p=re.compile('\\b([a-z])\.([a-z]{2,})\.(\d{4})(@alumnos\.urjc\.es)|([a-z]{1,})\.([a-z]{2,})(@urjc\.es)\\b')
a=input()
emails=p.findall(a)
print(emails)

for email in emails:
    if email[1]!='':
        print("alumno "+email[1]+" matriculado en "+email[2])
    else:
        print("profesor "+email[4]+" apellido "+ email[5])"""
"""
import re
p=re.compile('\\b(C\/|Calle)\s([A-ZÑÁÉÍÓÚ][a-zñíéáóüú]+\\b),?\s*(Nº|N|n|nº|)\s*(\d{1,}),\s*(\d{5})\\b')
a=input()
directions=p.findall(a)
#print(directions)
for dir in directions:
    print(dir[4]+"-"+dir[1]+"-"+dir[3])"""

#Ejer 6

#p=re.compile('\s([A-Z]*)\s\d*\s[-]{3}\s[\[]([a-z]{0,})[\]]\s[a-zA-Z]{0,}\s[:]\s([.]{0,})')
p=re.compile('(\w+)(?:\s+\d+ --- )\[(\w+)\]\s+(?:\w+\.){0,}(\w+)\s+:\s+(.*)')

a=input()
logs=p.findall(a)
#print(logs)
for log in logs:
   print('"'+log[0]+'","'+log[1]+'","'+log[2]+'","'+log[3]+'"')
