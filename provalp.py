# Inicialização das variáveis
numeros = []
soma = 0
quantidade = 0

# Leitura dos números
while True:
    numero = int(input("Digite um número inteiro (ou 0 para sair): "))
    if numero == 0:
        break
    numeros.append(numero)
    soma += numero
    quantidade += 1

# Verifica se houve pelo menos um número digitado
if quantidade > 0:
    # Cálculo da média
    media = soma / quantidade
    
    # Exibição dos resultados
    print(f"\nQuantidade de números digitados: {quantidade}")
    print(f"Soma dos números digitados: {soma}")
    print(f"Média dos números digitados: {media:.2f}")
else:
    print("\nNenhum número foi digitado.")
