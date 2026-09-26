# ==============================================================
# PROJETO: Pesquisa de Satisfação - TudoWeb
# CURSO: Técnico em Desenvolvimento de Sistemas
# ALUNO: Bianca Weiss
# DESCRIÇÃO: Coleta nome, idade e opinião de 50 entrevistados
#            e exibe quantas respostas foram EXCELENTE e RUIM.
# ==============================================================

# Variáveis que vão guardar os contadores
excelente = 0
ruim = 0

# Exibe o título do programa
print("----------------------------------------")
print("  PESQUISA DE SATISFAÇÃO - TUDOWEB")
print("----------------------------------------")
print("Opiniões: 1 = EXCELENTE | 2 = BOM | 3 = RUIM")
print("----------------------------------------")

# Laço que repete 50 vezes (uma para cada entrevistado)
for i in range(1, 51):

    print("")
    print("Entrevistado número:", i)
    print("")

    # Solicita o nome do entrevistado
    nome = input("Digite o nome: ")

    # Solicita a idade do entrevistado
    idade = int(input("Digite a idade: "))

    # Solicita a opinião do entrevistado
    opiniao = int(input("Digite a opinião (1-EXCELENTE / 2-BOM / 3-RUIM): "))

    # Verifica a opinião e atualiza o contador correto
    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 3:
        ruim = ruim + 1

# Exibe o resultado final da pesquisa
print("")
print("----------------------------------------")
print("     RESULTADO DA PESQUISA")
print("----------------------------------------")
print("Total de entrevistados :", 50)
print("Respostas EXCELENTE    :", excelente)
print("Respostas RUIM         :", ruim)
print("----------------------------------------")