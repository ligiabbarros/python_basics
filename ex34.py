#criar um loop que identifica numero primo

numero = int(input("Bota numero aqui:"))

divisao = 0

contador = numero

while contador > 0:
    if (numero % contador == 0):
        divisao += 1
    
    contador -= 1
    
    
if (divisao == 2):
    print("O número %d é primo" % numero)
else:
    print("O número %d NÃO é primo" % numero)
    
  