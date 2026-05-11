#Importando a biblioteca json
import json
def ler_txt():
    with open ("entrada_alunos.txt", "r", encoding="utf-8") as arquivo_txt:
        conteudo_txt = arquivo_txt.read()
        print (conteudo_txt)
#Estrutura de repetição para manter exibindo o menu até q se digite 0, que encerra o sistema
while True:
    #Criando o menu interativo
    print("1 - Exibir todos os alunos \n2 - Calcular média geral \n3 - Exibir maior e menor nota \n4 - Exibir aprovados e reprovados \n5 - Buscar aluno por nota \n6 - Buscar aluno por curso \n7 - Gerar relatório JSON \n8 - Exportar relatório TXT \n0 - Encerrar sistema")
    #Pedindo ao usuário a escolha de uma opção e guardando na variável op
    op = int(input("Escolha uma opção: "))
    #Lendo a variável op e fazendo com que a escolha do usuário execute o que foi solicitado
    match op:
        case 1:
            ler_txt()
        case 0:
            print("Encerrando...")
            break