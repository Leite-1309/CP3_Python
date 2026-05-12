#Importando a biblioteca json
import json


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
        #Caso o usuario escolha a opcao 0, o programa encerra o sistema
        case 0:
            #Mensagem avisando que o sistema esta sendo encerrado
            print("Encerrando...")
            #Interrompendo o while True e finalizando o programa
            break
