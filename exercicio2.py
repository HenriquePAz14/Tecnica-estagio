valor = int(input("Digite um valor: "))

primeiro = 0
segundo = 1
intermed = 0

foi = False

if valor == 0:
    foi = True
    
while foi == False:
    if valor > segundo:
        intermed = primeiro
        primeiro = segundo
        segundo  += intermed
    elif valor == segundo:
        foi = True
    else:
        break

if foi == False:
    print("O número não pertence a sequência de Fibonacci")
else:
    print("O número pertence a sequência de Fibonacci")