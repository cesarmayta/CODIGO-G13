dias = ("lunes","martes","miercoles","jueves","viernes")

print(dias)
dias = list(dias)
dias.append("sabado")
print(dias)
dias = tuple(dias)
print(dias)
print(dias[1:4])
for dia in dias:
    print(dia)