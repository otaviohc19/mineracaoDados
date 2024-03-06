numero_repeticoes = int(input("Digite a quantidade de repetições: "))
numero_tabuada = int(input("Digite o número da tabuada inicial: "))

contador_repeticoes = 0

for _ in range(numero_repeticoes):
    print(f"Repetição {contador_repeticoes + 1}:")
    print(f"Tabuada do {numero_tabuada}:")
    
    multiplicador = 25
    while multiplicador <= 40:
        resultado = numero_tabuada * multiplicador
        print(f"{numero_tabuada} x {multiplicador} = {resultado}")
        multiplicador += 1

    numero_tabuada += 1
    contador_repeticoes += 1

print("Tabuada finalizada!")
