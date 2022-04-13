dias = ["lunes","martes","miercoles"]
print(dias)
#pop - elimina el ultimo valor de lista
dias.pop()
print(dias)
#append - agrega un nuevo valor a la lista
dias.append("miercoles")
print(dias)
dias[0] = "domingo"
print(dias)

for dia in dias:
    print("hoy es " + dia)
