def numeros(div,divisor,pro=0):
    hola = []
    cociente = div//divisor
    resto = div % divisor
    a=10
    b=5
    hola.append(a)
    hola.append(b)
    return cociente,resto,div,hola

e,f,d,h= numeros(14,4)

print("e: ",e)

print("f: ",f)

print("div",d)

print("h",h[0])
print("h",h[1])



x=1
y=2

x,y = y,x

print(x)
print(y)
