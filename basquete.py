def calcularPontos(cestas1, cestas2, cestas3):
    return cestas1 + (cestas2 * 2) + (cestas3 * 3)
    
def main():
    pontosTotais = 0
    for i in range(1, 5):
        cestas1 = int(input(f"Quarto {i}: Quantidade de cestas de 1 ponto: "))
        cestas2 = int(input(f"Quarto {2}: Quantidade de cestas de 2 pontos: "))
        cestas3 = int(input(f"Quarto {2}: Quantidade de cestas de 3 pontos: "))
        pontosQuarto = calcularPontos(cestas1, cestas2, cestas3)
        pontosTotais += pontosQuarto
        print(f"Quarto {i}: Pontos: {pontosQuarto}")
        
        print(f"Total: {pontosTotais}")
        
main()