def numeros(div,divisor):
    cociente = div//divisor
    resto = div % divisor
    return cociente,resto,div

e,f,d = numeros(14,4)

print("e: ",e)

print("f: ",f)

print("div",d)

x=1
y=2

x,y = y,x

print(x)
print(y)
