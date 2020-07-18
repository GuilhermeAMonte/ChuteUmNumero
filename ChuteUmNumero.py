from random import randint

numer = randint(0,10)

user = int(input("Digite um numero até acha o valor sorteado: "))

if(user == numer):
    print("É isso ai seu sortudo")
elif(user != numer):
    print("Que azar, tente mais uma vez o numero sorteado foi {}".format(numer))

#Este foi meu segundo projeto em Python (Guilherme Alves do Monte)