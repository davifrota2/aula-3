palavra = str(input("digite uma palavra para indentificar se ela contem a letra a")) .lower()

tem_a_letra_a = 0

for letra in palavra :
    if letra == "a":
        print("possui a letra a")
        tem_a_letra_a +=1

if  tem_a_letra_a > 0:
    print("sua palavra tem A", tem_a_letra_a)
else:
    print("sua palavra não tem a letra A")