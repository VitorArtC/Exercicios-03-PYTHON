velo = float(input("velocidade detectada: "))

multa = velo - 80

valorpg = multa * 7

if velo <= 80:
    print("Sem multa")
    print("Valor da Multa: ", valorpg, "R$")


elif velo >= 81:
    print("Multado")
    print("Valor da Multa: ",valorpg,"R$")
