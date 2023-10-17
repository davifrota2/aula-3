frase = int(input("digite uma frase"))

for caracter in frase: 
  if caracter in '0123456789':
    print(f"numero encontrado: {caracter}")