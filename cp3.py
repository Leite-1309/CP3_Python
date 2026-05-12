# Importa a biblioteca usada para ler e gerar arquivos JSON
import json


# Lê os arquivos TXT e JSON e junta todos os alunos em uma lista única, assim, as outras funções não precisam abrir os arquivos de novo.
def ler_txt_json():
    alunos = []

    # Abre o TXT em modo leitura.
    with open("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        for linha in arquivo_txt:
            # Remove quebra de linha e espaços sobrando no começo/fim.
            linha = linha.strip()

            # Divide a linha usando o hífen.
            partes = linha.split("-")

            # Monta um dicionário para deixar os dados do TXT organizados.
            # A nota vem depois dos dois pontos, por isso uso split(":").
            aluno = {
                "id": partes[0].strip(),
                "nome": partes[1].strip(),
                "curso": partes[2].strip(),
                "nota": float(linha.split(":")[1])
            }

            alunos.append(aluno)

    # Abre o JSON e transforma o conteúdo em uma lista de dicionários Python.
    with open("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        alunos_json = json.load(arquivo_json)

        for aluno in alunos_json:
            # No JSON o id vem como número, aqui ele vira texto com três dígitos, tipo 006, 007, 008.
            aluno_formatado = {
                "id": f"{aluno['id']:03d}",
                "nome": aluno["nome"],
                "curso": aluno["curso"],
                "nota": aluno["nota"]
            }

            alunos.append(aluno_formatado)

    # Retorna todos os alunos juntos, tanto do TXT quanto do JSON.
    return alunos


# Recebe uma lista de alunos e calcula a média das notas.
def calcular_media(alunos):
    soma = 0

    # Soma todas as notas encontradas na lista.
    for aluno in alunos:
        soma += aluno["nota"]

    # Divide a soma pela quantidade de alunos.
    return soma / len(alunos)


# Recebe uma lista de alunos e separa quem passou de quem não passou.
def separar_aprovados_reprovados(alunos):
    aprovados = []
    reprovados = []

    # Nota maior ou igual a 6 entra em aprovados.
    for aluno in alunos:
        if aluno["nota"] >= 6:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)

    # Retorna duas listas ao mesmo tempo.
    return aprovados, reprovados


# Procura o aluno de maior nota e o aluno de menor nota.
def encontrar_maior_menor_nota(alunos):
    # Começa usando o primeiro aluno como referência inicial.
    maior = alunos[0]
    menor = alunos[0]

    # Compara cada aluno com os valores guardados até o momento.
    for aluno in alunos:
        if aluno["nota"] > maior["nota"]:
            maior = aluno

        if aluno["nota"] < menor["nota"]:
            menor = aluno

    return maior, menor


# Mostra somente os nomes dos aprovados e reprovados.
def exibir_aprovados_reprovados():
    alunos = ler_txt_json()
    aprovados, reprovados = separar_aprovados_reprovados(alunos)

    nomes_aprovados = []
    nomes_reprovados = []

    # Guarda apenas o nome, para a saída ficar mais limpa.
    for aluno in aprovados:
        nomes_aprovados.append(aluno["nome"])

    for aluno in reprovados:
        nomes_reprovados.append(aluno["nome"])

    print("Lista de alunos aprovados: ", nomes_aprovados)
    print("Lista de alunos reprovados: ", nomes_reprovados)


# Exibe a maior e a menor nota encontradas entre todos os alunos.
def exibir_maior_menor_nota():
    alunos = ler_txt_json()
    maior, menor = encontrar_maior_menor_nota(alunos)

    print("A maior nota é: ", maior["nota"], "\nA menor nota é: ", menor["nota"])


# Exibe a média geral dos alunos.
def exibir_media():
    alunos = ler_txt_json()
    media = calcular_media(alunos)

    print("A média geral desses alunos é igual a: ", media)


# Exibe todos os alunos usando o mesmo formato visual.
def exibir_alunos():
    alunos = ler_txt_json()

    # Como os dados já foram padronizados, o print serve para TXT e JSON.
    for aluno in alunos:
        print(f"{aluno['id']} - {aluno['nome']} - {aluno['curso']} - Nota: {aluno['nota']}")


# Busca alunos que tenham exatamente a nota digitada pelo usuário.
def buscar_nota():
    alunos = ler_txt_json()
    encontrados = []

    # strip() remove espaços extras antes de converter para float.
    busca_nota = float(input("Qual nota deseja buscar? ").strip())

    # Se a nota for inválida, a função para aqui com return.
    if busca_nota < 0 or busca_nota > 10:
        print("Valor inválido! As notas só vão de 0 a 10")
        return

    # Guarda os alunos que têm a mesma nota informada.
    for aluno in alunos:
        if aluno["nota"] == busca_nota:
            encontrados.append(f"{aluno['id']} - {aluno['nome']}")

    # Lista vazia é considerada False em Python.
    if encontrados:
        print("Foram encontrados", len(encontrados), "aluno(s) com essa nota.")
        print("São eles:")

        for aluno in encontrados:
            print(aluno)
    else:
        print("Nenhum aluno foi encontrado com essa nota")


# Busca alunos pelo curso informado pelo usuário.
def buscar_curso():
    alunos = ler_txt_json()
    encontrados = []

    # Converte a busca para maiúsculo para aceitar "ads", "ADS" ou " Ads ".
    busca_curso = input("Qual curso deseja buscar? ").strip().upper()

    for aluno in alunos:
        # O curso do aluno também vira maiúsculo antes da comparação.
        curso = aluno["curso"].strip().upper()

        if curso == busca_curso:
            encontrados.append(f"{aluno['id']} - {aluno['nome']} - {curso}")

    # not encontrados significa que a lista está vazia.
    if not encontrados:
        print("Não há nenhum aluno desse curso")
    else:
        print(f"Alunos de {busca_curso} encontrados: ")

        for aluno in encontrados:
            print(aluno)


# Gera um relatório JSON com média, total, aprovados e reprovados.
def gerar_relatorio_json():
    alunos = ler_txt_json()
    aprovados, reprovados = separar_aprovados_reprovados(alunos)
    media = calcular_media(alunos)

    # Este dicionário segue o formato pedido para o relatório.
    relatorio = {
        "media": media,
        "total": len(alunos),
        "aprovados": aprovados,
        "reprovados": reprovados
    }

    # indent=4 deixa o JSON organizado.
    # ensure_ascii=False mantém acentos no arquivo.
    with open("relatorio.json", "w", encoding="utf-8") as arquivo_relatorio:
        json.dump(relatorio, arquivo_relatorio, indent=4, ensure_ascii=False)

    print("Relatório JSON gerado com sucesso!")


# Gera um relatório TXT resumido.
def exportar_txt():
    alunos = ler_txt_json()
    media = calcular_media(alunos)
    maior, menor = encontrar_maior_menor_nota(alunos)

    # O arquivo é aberto em modo "w", então ele é criado ou sobrescrito.
    with open("relatorio.txt", "w", encoding="utf-8") as arquivo_relatorio:
        arquivo_relatorio.write("===== RELATÓRIO =====\n\n")
        arquivo_relatorio.write(f"Total de alunos: {len(alunos)}\n")
        arquivo_relatorio.write(f"Média geral: {media:.2f}\n\n")
        arquivo_relatorio.write("Maior nota:\n")
        arquivo_relatorio.write(f"{maior['nome']} - {maior['nota']}\n\n")
        arquivo_relatorio.write("Menor nota:\n")
        arquivo_relatorio.write(f"{menor['nome']} - {menor['nota']}\n")

    print("Relatório TXT gerado com sucesso!")


# Mantém o menu rodando até o usuário escolher a opção 0.
while True:
    print("1 - Exibir todos os alunos \n2 - Calcular média geral \n3 - Exibir maior e menor nota \n4 - Exibir aprovados e reprovados \n5 - Buscar aluno por nota \n6 - Buscar aluno por curso \n7 - Gerar relatório JSON \n8 - Exportar relatório TXT \n0 - Encerrar sistema")
    op = int(input("Escolha uma opção: "))

    # Cada case representa uma opção do menu.
    match op:
        case 1:
            print("\n=========================================================")
            exibir_alunos()
            print("=========================================================\n")

        case 2:
            print("\n=========================================================")
            exibir_media()
            print("=========================================================\n")

        case 3:
            print("\n=========================================================")
            exibir_maior_menor_nota()
            print("=========================================================\n")

        case 4:
            print("\n=======================================================================================================================================================")
            exibir_aprovados_reprovados()
            print("=======================================================================================================================================================\n")

        case 5:
            print("\n=========================================================")
            buscar_nota()
            print("=========================================================\n")

        case 6:
            print("\n=========================================================")
            buscar_curso()
            print("=========================================================\n")

        case 7:
            print("\n=========================================================")
            gerar_relatorio_json()
            print("=========================================================\n")

        case 8:
            print("\n=========================================================")
            exportar_txt()
            print("=========================================================\n")

        case 0:
            print("Encerrando...")
            break

        # Qualquer número fora das opções cai aqui.
        case _:
            print("opção inválida\n")
