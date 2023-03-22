import numpy as np
print('Ingresar frase: ',end='')
frase=input()
print('Ingresar numero de filas: ',end='')
row=input()
print('Ingresar numero de columnas: ',end='')
column=input()
cifrado=np.zeros((int(row),int(column)),dtype=str)
c=1
print('Mensaje: ',end='')
for i in range(0,int(row)):
    for j in range(0,int(column)):
        cifrado[i][j]=frase[j*int(row)+i:j*int(row)+c+i]
        print(cifrado[i][j],end='')
    c+=1
print()
print(cifrado)