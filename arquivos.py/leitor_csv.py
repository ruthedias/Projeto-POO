from eleicao import Eleitor, Prefeito, Cidade, UrnaEletronica, Local,Vereador
import csv

def lerArquivoCsv():

    eleitores = []  # armazenar os eleitores
    candidatos = []  # armazenar os candidatos
    vereadores = []  # armazenar os vereadores
    urnas = []  # armazenar as urnas

    caminho="arquivos_csv/eleitores.csv"  #Uma variavel para armazenar o caminho que encontra o arquivo
    with open("arquivos_csv/eleitores.csv", mode='r') as file:  #Abrir o arquivo em modo de leitura ('r')
        reader = csv.reader(file) #ler o arquivo
        next(reader, None) #Pular a primeira linha

        for linha in reader:
            nome, titulo, nomeCidade, estado, cep, escola, zona, sessao, votou = linha # Criando variaveis e preenchendo com os conteudos da linha
            if votou=="False":
                votou=False
            else:
                votou=True
            cidade= Cidade(nomeCidade,estado,cep)
            local= Local(cidade,escola,zona,sessao)
            novoEleitor = Eleitor(nome, titulo, local,votou) #Cria um objeto de eleitor com os dados da linha
            eleitores.append(novoEleitor) #adiciona o eleitor criado na lista eleitores
    
    #codigo abaixo segue o mesmo raciocínio do codigo acima
    caminho="arquivos_csv/prefeitos.csv"
    with open(caminho, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for linha in reader:
            nome, titulo, nomeCidade, estado, cep, escola, zona, sessao, partido, numeroEleitoral = linha # Criando variaveis e preenchendo com os conteudos da linha
            cidade= Cidade(nomeCidade,estado,cep)
            local= Local(cidade,escola,zona,sessao)
            novoCandidato = Prefeito(nome, titulo, local, partido, numeroEleitoral)
            candidatos.append(novoCandidato)

    caminho_vereadores = "arquivos_csv/vereadores.csv"
    with open(caminho_vereadores, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for linha in reader:
            nome, titulo, nomeCidade, estado, cep, escola, zona, sessao, partido, numeroEleitoral = linha # Criando variaveis e preenchendo com os conteudos da linha
            cidade= Cidade(nomeCidade,estado,cep)
            local= Local(cidade,escola,zona,sessao)
            novoCandidato = Vereador(nome, titulo, local, partido, numeroEleitoral)
            vereadores.append(novoCandidato)

    caminho= "arquivos_csv/urnas.csv"
    with open (caminho,mode='r') as file:
        reader = csv.reader(file)
        next(reader,None)

        for linha in reader:
            cidade, estado, cep, escola, zona, sessao, status = linha
            if status=="False":
                status=False
            else:
                status=True
            cidade1= Cidade(cidade,estado,cep)
            local= Local(cidade1,escola,zona,sessao)
            novaUrna= UrnaEletronica(local,status)
            urnas.append(novaUrna)
    
    #retorna todas as listas preenchidas com dados de eleitores, candidatos e urna
    return eleitores, candidatos, vereadores, urnas

