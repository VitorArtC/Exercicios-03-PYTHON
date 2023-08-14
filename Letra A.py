import re

palavra = input("Digite uma frase: ")

letra_a = re.findall(r"[aA]", palavra)

n = len(letra_a)

primeira = letra_a[0]
primeira_psi = palavra.find(primeira)

ultima = letra_a[-1]
ultima_psi = palavra.rfind(ultima)

print("A letra A aparece {} vez(es) nesta(s) palavra(s).".format(n))
print("A primeira letra A aparece na posição {}.".format(primeira_psi))
print("A última letra A aparece na posição {}.".format(ultima_psi))