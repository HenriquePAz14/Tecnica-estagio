palavra = input("Escreva uma palavra: ")
for n in range(len(palavra)):
    print(palavra[(len(palavra)-1)-n], end="")