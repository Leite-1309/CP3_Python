#Importando a biblioteca json
import json


def gerar_relatorio_txt():
    soma = 0
    total = 0
    maior_nota = -1
    menor_nota = 11
    aluno_maior_nota = ""
    aluno_menor_nota = ""

    with open("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        for linha in arquivo_txt:
            linha = linha.strip()

            partes = linha.split("-")
            nome = partes[1].strip()

            pos_nota = linha.split(":")
            nota = float(pos_nota[1])

            soma += nota
            total += 1

            if nota > maior_nota:
                maior_nota = nota
                aluno_maior_nota = nome

            if nota < menor_nota:
                menor_nota = nota
                aluno_menor_nota = nome

    with open("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        alunos = json.load(arquivo_json)

        for aluno in alunos:
            nome = aluno["nome"]
            nota = aluno["nota"]

            soma += nota
            total += 1

            if nota > maior_nota:
                maior_nota = nota
                aluno_maior_nota = nome

            if nota < menor_nota:
                menor_nota = nota
                aluno_menor_nota = nome

    media = soma / total

    with open("relatorio.txt", "w", encoding="utf-8") as arquivo_relatorio:
        arquivo_relatorio.write("===== RELATÓRIO =====\n\n")
        arquivo_relatorio.write(f"Total de alunos: {total}\n")
        arquivo_relatorio.write(f"Média geral: {media:.2f}\n\n")
        arquivo_relatorio.write("Maior nota:\n")
        arquivo_relatorio.write(f"{aluno_maior_nota} - {maior_nota}\n\n")
        arquivo_relatorio.write("Menor nota:\n")
        arquivo_relatorio.write(f"{aluno_menor_nota} - {menor_nota}\n")

    print("Relatório TXT gerado com sucesso!")


def gerar_relatorio_json():
    soma = 0
    total = 0
    aprovados = []
    reprovados = []

    with open("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        for linha in arquivo_txt:
            linha = linha.strip()

            partes = linha.split("-")
            id = partes[0].strip()
            nome = partes[1].strip()
            curso = partes[2].strip()

            pos_nota = linha.split(":")
            nota = float(pos_nota[1])

            aluno = {
                "id": id,
                "nome": nome,
                "curso": curso,
                "nota": nota
            }

            soma += nota
            total += 1

            if nota >= 6:
                aprovados.append(aluno)
            else:
                reprovados.append(aluno)

    with open("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        alunos = json.load(arquivo_json)

        for aluno in alunos:
            nota = aluno["nota"]

            aluno_formatado = {
                "id": f"{aluno['id']:03d}",
                "nome": aluno["nome"],
                "curso": aluno["curso"],
                "nota": nota
            }

            soma += nota
            total += 1

            if nota >= 6:
                aprovados.append(aluno_formatado)
            else:
                reprovados.append(aluno_formatado)

    media = soma / total

    relatorio = {
        "media": media,
        "total": total,
        "aprovados": aprovados,
        "reprovados": reprovados
    }

    with open("relatorio.json", "w", encoding="utf-8") as arquivo_relatorio:
        json.dump(relatorio, arquivo_relatorio, indent=4, ensure_ascii=False)

    print("Relatório JSON gerado com sucesso!")







def buscar_curso():
    encontrados = []

    busca_curso = input("Qual curso deseja buscar? ").strip().upper()

    #Abrindo o arquivo .txt em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        #Percorrendo o arquivo .txt linha por linha
        for linha in arquivo_txt:
            linha = linha.strip()
            partes = linha.split("-")
            curso = partes[2].strip().upper()
            id = partes[0].strip()
            nome = partes[1].strip()
            if (curso == busca_curso):
                encontrados.append(f"{id} - {nome} - {curso}")

    #Abrindo o arquivo .json em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        #Lendo o conteudo do json e transformando em uma lista de dicionarios do Python
        alunos = json.load(arquivo_json)
        #Percorrendo cada aluno dentro da lista alunos
        for aluno in alunos:
            if (aluno["curso"].upper() == busca_curso):
                encontrados.append(f"{aluno['id']:03d} - {aluno['nome']} - {aluno['curso'].upper()}")

    if not encontrados:
        print("Não há nenhum aluno desse curso")
    else:
        print(f"Alunos de {busca_curso} encontrados: ")
        for aluno in encontrados:
            print(aluno)
    





def buscar_nota():
    encontrados = [] 

    busca_nota = float(input("Qual nota deseja buscar? ").strip())

    if (busca_nota < 0 or busca_nota > 10):
        print("Valor inválido! As notas só vão de 0 a 10")
        return
    
    #Abrindo o arquivo .txt em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        #Percorrendo o arquivo .txt linha por linha
        for linha in arquivo_txt:
            linha = linha.strip()
            pos_nota = linha.split(":")
            nota = float(pos_nota[1])
            if (nota == busca_nota):
                partes = linha.split("-")
                id = partes[0].strip()
                nome = partes[1].strip()
                encontrados.append(f"{id} - {nome}")

    #Abrindo o arquivo .json em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        #Lendo o conteudo do json e transformando em uma lista de dicionarios do Python
        alunos = json.load(arquivo_json)
        #Percorrendo cada aluno dentro da lista alunos
        for aluno in alunos:
            if (aluno["nota"] == busca_nota):
                encontrados.append(f"{aluno['id']:03d} - {aluno['nome']}")

    if (len(encontrados) != 0):            
        print("Foram encontrados", len(encontrados), "aluno(s) com essa nota.")
        print("São eles:")
        for aluno in encontrados:
            print(aluno)
    else:
        print("Nenhum aluno foi encontrado com essa nota")



#Criando listas vazias para armazenar o nome dos alunos aprovados e reprovados
aprovados = []
reprovados = []
#Criando a funcao que separa os alunos aprovados e reprovados dos arquivos .txt e .json
def exibir_aprovados_reprovados():
    #Abrindo o arquivo .txt em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        #Percorrendo o arquivo .txt linha por linha
        for linha in arquivo_txt:
            #Removendo espacos extras e quebras de linha do inicio e do fim da linha
            linha = linha.strip()
            #Separando a linha nos dois pontos, pois no .txt a nota aparece depois de "Nota:"
            pos_nota = linha.split(":")
            #Convertendo a nota de texto para numero decimal e designando a variavel nota
            nota = float(pos_nota[1])
            #Verificando se a nota do aluno é suficiente para aprovação
            if (nota >= 6):
                #Separando a linha pelos hifens para pegar o nome do aluno
                pos_nome = linha.split("-")
                nome = pos_nome[1]
                #Adicionando o nome do aluno na lista de aprovados
                aprovados.append(nome)
            else:
                #Separando a linha pelos hifens para pegar o nome do aluno
                pos_nome = linha.split("-")
                nome = pos_nome[1]
                #Adicionando o nome do aluno na lista de reprovados
                reprovados.append(nome)
    #Abrindo o arquivo .json em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        #Lendo o conteudo do json e transformando em uma lista de dicionarios do Python
        alunos = json.load(arquivo_json)
        #Percorrendo cada aluno dentro da lista alunos
        for aluno in alunos:
            #Pegando a nota do aluno no json para verificar sua situacao
            nota = aluno["nota"]
            #Se a nota for maior ou igual a 6, o aluno entra na lista de aprovados
            if(nota >= 6):
                aprovados.append(aluno["nome"])
            else:
                #Se a nota for menor que 6, o aluno entra na lista de reprovados
                reprovados.append(aluno["nome"])
    #Mostrando as listas de alunos aprovados e reprovados no terminal
    print("Lista de alunos aprovados: ", aprovados)
    print("Lista de alunos reprovados: ", reprovados)



#Criando a funcao que encontra a maior e a menor nota dos arquivos .txt e .json
def exibir_maior_menor_nota():
    #Criando as variaveis que vao guardar a maior e a menor nota encontradas
    maior_nota = 0
    menor_nota = 100
    #Abrindo o arquivo .txt em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        #Percorrendo o arquivo .txt linha por linha
        for linha in arquivo_txt:
            #Removendo espacos extras e quebras de linha do inicio e do fim da linha
            linha = linha.strip()
            #Separando a linha nos dois pontos, pois no .txt a nota aparece depois de "Nota:"
            pos_nota = linha.split(":")
            #Convertendo a nota de texto para numero decimal e designando a variavel nota
            nota = float(pos_nota[1])
            #Comparando a nota atual com a maior nota encontrada ate agora
            if (nota > maior_nota):
                maior_nota = nota
            elif (nota < menor_nota):
                #Comparando a nota atual com a menor nota encontrada ate agora
                menor_nota = nota
    #Abrindo o arquivo .json em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        #Lendo o conteudo do json e transformando em uma lista de dicionarios do Python
        alunos = json.load(arquivo_json)
        #Percorrendo cada aluno dentro da lista alunos
        for aluno in alunos:
            #Pegando a nota do aluno no json para comparar com a maior e a menor nota
            nota = aluno["nota"]
            #Atualizando a maior nota, caso a nota atual seja maior
            if (nota > maior_nota):
                maior_nota = nota
            elif (nota < menor_nota):
                #Atualizando a menor nota, caso a nota atual seja menor
                menor_nota = nota
    #Mostrando a maior e a menor nota encontradas no terminal
    print("A maior nota é: ", maior_nota, "\nA menor nota é: ", menor_nota)



#Criando a funcao que calcula a media geral das notas dos alunos do arquivo .txt e do arquivo .json
def calcular_media():
    #Criando a variavel soma para guardar a soma de todas as notas encontradas
    soma = 0
    #Criando a variavel n_alunos para contar quantos alunos existem no total
    n_alunos = 0
    #Abrindo o arquivo .txt em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        #Percorrendo o arquivo .txt linha por linha
        for linha in arquivo_txt:
            #Removendo espacos extras e quebras de linha do inicio e do fim da linha
            linha = linha.strip()
            #Separando a linha nos dois pontos, pois no .txt a nota aparece depois de "Nota:"
            pos_nota = linha.split(":")
            #Convertendo a nota de texto para numero decimal e somando na variavel soma
            soma += float(pos_nota[1])
            #Somando mais 1 na quantidade de alunos
            n_alunos += 1
    #Abrindo o arquivo .json em modo leitura, usando encoding utf-8 para aceitar acentos
    with open ("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        #Lendo o conteudo do json e transformando em uma lista de dicionarios do Python
        alunos = json.load(arquivo_json)
        #Percorrendo cada aluno dentro da lista alunos
        for aluno in alunos:
            #Pegando a nota do aluno no json e somando na variavel soma
            soma += aluno["nota"]
            #Somando mais 1 na quantidade de alunos
            n_alunos += 1
    #Calculando a media dividindo a soma das notas pela quantidade total de alunos
    media = soma / n_alunos
    #Mostrando o resultado da media no terminal
    print("A média geral desses alunos é igual a: ", media)



#Criando a função que abre o arquivo .txt e o lê, coloquei um print vazio no final para a ultima linha do arquivo .txt não ficar grudada no .json na hora de exibir
def ler_txt():
    #Abrindo o arquivo entrada_alunos.txt em modo leitura
    with open ("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        #Percorrendo o arquivo de texto uma linha por vez
        for linha in arquivo_txt:
            #Mostrando a linha no terminal sem adicionar outra quebra de linha alem da que ja existe no arquivo
            print (linha, end="")
    #Print vazio para garantir que o proximo conteudo comece em uma nova linha
    print()



#Criando a função que abre o arquivo .json e o lê, também coloquei o print para sair no msm formato que os nomes saem no arquivo .txt
def ler_json():
    #Abrindo o arquivo entrada_alunos.json em modo leitura
    with open ("entrada_alunos.json", "r", encoding="utf-8") as arquivo_json:
        #Lendo o json e guardando os dados na variavel alunos
        alunos = json.load(arquivo_json)
        #Percorrendo cada aluno dentro da lista alunos
        for aluno in alunos:
            #Mostrando os dados do aluno no mesmo formato usado no arquivo .txt
            #O :03d faz o id aparecer com 3 digitos, por exemplo: 006, 007, 008
            print(f"{aluno['id']:03d} - {aluno['nome']} - {aluno['curso']} - Nota: {aluno['nota']}")



#Estrutura de repetição para manter exibindo o menu até q se digite 0, que encerra o sistema
while True:
    #Criando o menu interativo
    print("1 - Exibir todos os alunos \n2 - Calcular média geral \n3 - Exibir maior e menor nota \n4 - Exibir aprovados e reprovados \n5 - Buscar aluno por nota \n6 - Buscar aluno por curso \n7 - Gerar relatório JSON \n8 - Exportar relatório TXT \n0 - Encerrar sistema")
    #Pedindo ao usuário a escolha de uma opção e guardando na variável op
    op = int(input("Escolha uma opção: "))
    #Lendo a variável op e fazendo com que a escolha do usuário execute o que foi solicitado
    match op:
        #Caso o usuario escolha a opcao 1, o programa exibe todos os alunos do .txt e do .json
        case 1:
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=========================================================")
            #Chamando a funcao que le e mostra os alunos do arquivo .txt
            ler_txt()
            #Chamando a funcao que le e mostra os alunos do arquivo .json
            ler_json()
            #Mostrando outra linha para fechar a exibicao dos alunos
            print("=========================================================\n")

        #Caso o usuario escolha a opcao 2, o programa calcula a media geral
        case 2:
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=========================================================")
            #Chamando a funcao responsavel pelo calculo da media
            calcular_media()
            #Mostrando outra linha para fechar a exibicao da media
            print("=========================================================\n")

        #Caso o usuario escolha a opcao 3, o programa exibe a maior e a menor nota
        case 3: 
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=========================================================")
            #Chamando a funcao responsavel por encontrar a maior e a menor nota
            exibir_maior_menor_nota()
            #Mostrando outra linha para fechar a exibicao da maior e menor nota
            print("=========================================================\n")

        #Caso o usuario escolha a opcao 4, o programa exibe os alunos aprovados e reprovados
        case 4:
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=======================================================================================================================================================")
            #Chamando a funcao responsavel por separar aprovados e reprovados
            exibir_aprovados_reprovados()
            #Mostrando outra linha para fechar a exibicao das listas
            print("=======================================================================================================================================================\n")

        case 5:
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=========================================================")
            #Chamando a funcao responsavel por buscar os alunos pela nota
            buscar_nota()
            #Mostrando outra linha para fechar a exibicao da maior e menor nota
            print("=========================================================\n")

        case 6:
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=========================================================")
            #Chamando a funcao responsavel por buscar os alunos pelo curso
            buscar_curso()
            #Mostrando outra linha para fechar a exibicao da maior e menor nota
            print("=========================================================\n")   

        case 7:
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=========================================================")
            #Chamando a funcao responsavel por buscar os alunos pelo curso
            gerar_relatorio_json()
            #Mostrando outra linha para fechar a exibicao da maior e menor nota
            print("=========================================================\n")

        case 8:
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=========================================================")
            #Chamando a funcao responsavel por buscar os alunos pelo curso
            gerar_relatorio_txt()
            #Mostrando outra linha para fechar a exibicao da maior e menor nota
            print("=========================================================\n")

        #Caso o usuario escolha a opcao 0, o programa encerra o sistema
        case 0:
            #Mensagem avisando que o sistema esta sendo encerrado
            print("Encerrando...")
            #Interrompendo o while True e finalizando o programa
            break

        case _:
            #Mostrando uma linha para separar visualmente o resultado do menu
            print("\n=========================================================")
            print("Opção inválida!")
            #Mostrando outra linha para fechar a exibicao da maior e menor nota
            print("=========================================================\n")

