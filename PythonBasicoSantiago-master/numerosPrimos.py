
num = int(input("Escriba el numero: "))
n = 1
d = 0
while n <= num:
    if num % n == 0:
        d = d + 1
    n = n + 1
if d == 2:
    print("Si es primo ")
else:
    print("No es primo") 