print("Mas sobre funciones")
#Aqui se escriben las funciones
def suma_ab(a,b):
    s= a+b
    return s

def resta_ab(c,d):
    r= c-d
    return r

def multi_ab(e,f):
    m= e*f
    return m

def div_ab(g,h):
    d= g/h
    return d

#Llamando a las funciones
print("Calculando suma")
n1=int(input("Ingresa el primer numero: "))
n2=int(input("Ingresa el segundo numero: "))
suma= suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es: {suma}")
#--------------------------------------------
print("Calculando resta")
num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))
resta=resta_ab(num1,num2)
print(f"La resta de {num1} - {num2} es: {resta}")
#--------------------------------------------
print("Calculando multiplicacion")
nume1=int(input("Ingresa el primer numero: "))
nume2=int(input("Ingresa el segundo numero: "))
multi=multi_ab(nume1,nume2)
print(f"La multiplicacion de {nume1} x {nume2} es: {multi}")
#--------------------------------------------
print("Calculando division")
numer1=int(input("Ingresa el primer numero: "))
numer2=int(input("Ingresa el segundo numero: "))
div=div_ab(numer1,numer2)
print(f"La division de {numer1} / {numer2} es: {div}")