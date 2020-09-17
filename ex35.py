valor = int(input("Saque: "))

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0

while valor > 0:
    while valor > 100:
        nota100 += 1
        valor -= 100
    while valor > 50:
        nota50 += 1
        valor -= 50
    while valor > 20:
        nota20 += 1
        valor -= 20
    while valor >= 10:
        nota10 += 1
        valor -= 10
    while valor >= 1:
        nota1 += 1
        valor -= 1
    
   

print("Receba %d notas de $100, %d notas de $50, %d notas de $20, %d notas de $10 e %d notas de $1." % (nota100, nota50, nota20, nota10, nota1))





