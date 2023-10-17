soma = 0
for i in range(1,11):
    numero = float(input(f"Digite o {i}º número: "))
    soma = soma + numero

media = soma / 10

print(f"A média dos números é {media}")
