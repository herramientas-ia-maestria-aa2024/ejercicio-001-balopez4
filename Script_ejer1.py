file=open('informacion.txt','r')
read = file.readlines() 
modified =[]

#Esta parte es para quitar el \n al final de cada linea
for line in read:
   modified.append(line.strip())

#Imprimir de manera apropiada la información
for each in modified:
   print(each)