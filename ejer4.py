import re
pattern="\\b([a-z]{1,})\.([a-z]{2,})(?:\.)?(\d{4})?\@(alumnos\.)?(urjc.es)\\b"
result=re.findall(pattern, input())

for r in result:
    if r[3]:
        print("alumno "+r[1]+" matriculado en "+r[2])
    else:
        print("profesor "+r[0]+" apellido "+r[1])