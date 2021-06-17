palabras ={}
def iniciarContador():
  archivo= open('SAO PROGRESSIVE 4.txt')
  linea = archivo.readline()
  lineas = linea.split()
  while linea!="":
     for palabraa in lineas:
      if palabraa in palabras:
        x=int(palabras[palabraa])
        palabras[palabraa]=x+1
      else:
        palabras[palabraa]=1
     linea = archivo.readline()
     lineas = linea.split()
  archivo.close()

def imprimir():
  for a in palabras:
    num = str(palabras[a])
    print(a+"= "+num)

iniciarContador()
print("Las palabras repetidas son ")
imprimir()