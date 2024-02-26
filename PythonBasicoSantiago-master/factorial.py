numero = int(input("Introduzca el número: "))
factorial = 1
d = 1
while (d <= numero):
    factorial = factorial * d
    d = d + 1
print ("El factorial es " + str(factorial))