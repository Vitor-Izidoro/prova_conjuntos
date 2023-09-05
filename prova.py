#  giancarlo perli e Vitor Rodrigues Izidoro
conjunto1 = []
conjunto2 = []

num = int(input("Digite a quantidade de elementos que você deseja inserir no primeiro conjunto: "))
for x in range(num):
    elemento = str(input("Digite o valor: "))
    conjunto1.append(elemento)

print("Conjunto 1:", conjunto1)

num2 = int(input("Digite a quantidade de elementos do segundo conjunto: "))
for x in range(num2):
    elemento2 = str(input("Digite o valor: "))
    conjunto2.append(elemento2)

print("Conjunto 2:", conjunto2)

select = int(input("Digite 1 para união, 2 para intersecção, 3 para diferença e 4 para cartesiano: "))

if select == 1:
    # União de conjuntos
    resultado = set(conjunto1).union(conjunto2)
    print("União dos conjuntos:", resultado)
    
elif select == 2:
    # Interseção de conjuntos
    resultado = set(conjunto1).intersection(conjunto2)
    print("Interseção dos conjuntos:", resultado)
    
elif select == 3:
    # Diferença de conjuntos (Complemento)
    resultado1 = set(conjunto1) - set(conjunto2)
    resultado2 = set(conjunto2) - set(conjunto1)
    print("Diferença do Conjunto 1 - Conjunto 2:", resultado1)
    print("Diferença do Conjunto 2 - Conjunto 1:", resultado2)
    
elif select == 4:
    # Produto cartesiano não é diretamente suportado por conjuntos em Python
    produto_cartesiano = [(x, y) for x in conjunto1 for y in conjunto2]

    print("Produto cartesiano dos conjuntos:", produto_cartesiano)

else:
    print("Seleção inválida.")
