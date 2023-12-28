import os  # Utilizar para limpar a tela do terminal

from eleicao import Boletim, Debate, UrnaEletronica
from gerenciador import GerenciadorEleitoral
from leitor_csv import lerArquivoCsv

if __name__=="__main__":

    eleitores=[]
    vereadores=[]
    prefeitos=[]
    urnas=[]

    eleitores,prefeitos,vereadores,urnas=lerArquivoCsv()

    GerenciadorEleitoral.eleitores=eleitores
    GerenciadorEleitoral.prefeitos=prefeitos
    GerenciadorEleitoral.vereadores=vereadores
    GerenciadorEleitoral.urnas=urnas

    opcao=0
    print("                        BEM-VINDO USUÁRIO A CAMPANHA ELEITORAL                     ")
    while opcao!=12:
        os.system('cls')
        print("Escolha uma opção abaixo que deseja acessar\n")
        print("1. Acessar os Candidatos a Prefeito.")
        print("2. Acessar os Candidatos a Vereador")
        print("3. Ver a lista com todos os eleitores cadastrados.")
        print("4. Ver urnas cadastradas no sistema.")
        print("5. Saber a proposta dos candidados a prefeito")
        print("6. Ver o debate dos candidados.")
        print("7. Verificar dados do eleitor especifico.")
        print("8. Iniciar votação.")
        print("9. Adicionar Voto.")
        print("10. Encerrar votação.")
        print("11. Boletim individual de cada urna")
        print("12. Resultado Final.")
        print("11. Sair do programa.")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            os.system('cls')
            gerenciador = GerenciadorEleitoral()
            Tabela_Prefeito= gerenciador.criarDataFramePrefeito()
            print(Tabela_Prefeito)
            input("\nAperte enter para voltar pro menu")

        if opcao == 2:
            os.system('cls')
            gerenciador = GerenciadorEleitoral()
            Tabela_Vereador= gerenciador.criarDataFrameVereador()
            print(Tabela_Vereador)
            input("\nAperte enter para voltar pro menu")

        elif opcao == 3:
            os.system('cls')
            gerenciador = GerenciadorEleitoral()
            tabelaEleitor=gerenciador.criarDataFrameEleitor()
            print(tabelaEleitor)
            input("\nAperte enter para voltar pro menu")

        elif opcao == 4:
            os.system('cls')
            gerenciador = GerenciadorEleitoral()
            tabelaUrna = gerenciador.criarDataFrameUrna()
            print(tabelaUrna)
            input("\nAperte enter para voltar pro menu")

        elif opcao == 5:
            candidatoEncontrado = False
            os.system('cls')
            candidato= input("Digite o nome do candidato que você deseja saber a proposta: ")
            for prefeito in GerenciadorEleitoral.prefeitos:
                if candidato==prefeito.get_nome():
                    print ("Candidato encontrado")
                    prefeito.propostas(candidato)
                    candidatoEncontrado = True
            if(candidatoEncontrado==False): print("Candidato não encontrado")
            input("\nAperte enter para voltar pro menu")
            
        elif opcao == 6:
            os.system('cls')
            print("Foi aberto uma nova janela no seu programa, por favor clique na nova janela aberta para assistir o video.")
            Debate.debater()
            input("\nAperte enter para voltar pro menu")

        elif opcao == 7:
            EleitorEncontrado = False
            os.system('cls')
            eleitor= input("Digite o nome do eleitor: ")
            titulo= input("Digite o titulo do eleitor: ")
            for eleitores in GerenciadorEleitoral.eleitores:
                if eleitores.get_nome()==eleitor:
                    if eleitores.get_titulo()==titulo:
                        print(eleitores)
                        EleitorEncontrado = True
            if(EleitorEncontrado==False): print("Eleitor não consta no sistema")                 
            input("\nAperte enter para voltar pro menu")

        elif opcao == 8:
            os.system('cls')
            for urna in UrnaEletronica.urnas:
                urna.iniciar_votacao()
            gerenciador=GerenciadorEleitoral()
            gerenciador.adicionarUrnaCsv()
            input("\nAperte enter para voltar pro menu")
            
        elif opcao == 9:
            os.system('cls')
            nome= input("Digite o nome do eleitor: ")
            titulo=input("Digite o titulo do eleitor: ")
            for eleitor in GerenciadorEleitoral.eleitores:
                    if eleitor.get_nome()==nome and eleitor.get_titulo()==titulo:
                        for urna in GerenciadorEleitoral.urnas:
                            if urna.local.sessao==eleitor.local.sessao:
                                print(urna.adicionar_voto(eleitor))
            gerenciador= GerenciadorEleitoral()
            gerenciador.adicionandoEleitorCsv()
            input("\nAperte enter para voltar pro menu")

        elif opcao == 10:
            os.system('cls')
            for urna in GerenciadorEleitoral.urnas:
                urna.encerrar_votacao()
            input("Aperte enter para voltar pro menu")
        elif opcao ==11:
            os.system('cls')
            for urna in GerenciadorEleitoral.urnas:
                urna.emitirBoletim()
                print("Aperte enter")
            input("Aperte enter para voltar pro menu")
        elif opcao == 12:
            os.system('cls')
            Boletim.exibirResultado(GerenciadorEleitoral.urnas)
            input("Aperte enter para voltar pro menu")
        elif opcao ==13:    
            os.system('cls')
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

