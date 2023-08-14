
notas01 = float(input("Nota do 1 Bimestre: "))
notas02 = float(input("Nota do 2 Bimestre: "))
notas03 = float(input("Nota do 3 Bimestre: "))
notas04 = float(input("Nota do 4 Bimestre: "))

media = (notas01 + notas02 + notas03 + notas04)/4


if media >= 7:
    print("Aprovado =D sua média é: ", media)



elif media < 6:
     print("Reprovado!! Você vai estudar com o Tijolo, sua média é:", media)