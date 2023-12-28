import csv

import pandas as pd

contP = 0 
contV = 0

class GerenciadorEleitoral: #Classe responsavel por fazer a armazenação dos eleitores cadastrados´

    eleitores =[]
    prefeitos=[]
    vereadores=[]
    urnas=[]

    def adicionarEleitor(self,eleitor):
        self.eleitores.append(eleitor)
    
    def adicionarPrefeito(self,prefeito):
        self.prefeitos.append(prefeito)

    def adicionarVereador(self,vereador):
        self.vereadores.append(vereador)
    
    def adicionarUrnas(self, urna):
        self.urnas.append(urna)


    def adicionandoEleitorCsv (self): #adiciona os eleitores em um arquivo csv
        caminho= "arquivos_csv/eleitores.csv" #caminho em que o arquivo se encontra
        with open(caminho, mode='w', newline='') as file: 
            writer = csv.writer(file)

            writer.writerow(['Nome','Titulo', 'Cidade', 'Estado', 'CEP', 'Escola', 'Zona', 'Sessão', 'Votou'])

            for eleitor in self.eleitores:
                writer.writerow([eleitor.get_nome(),eleitor.get_titulo(),eleitor.local.cidade.nome,eleitor.local.cidade.estado, eleitor.local.cidade.cep, eleitor.local.escola,eleitor.local.zona, eleitor.local.sessao, eleitor.votou])


    def adicionandoPrefeitosCsv (self):
        caminho= "arquivos_csv/prefeitos.csv"
        with open(caminho, mode='w', newline='') as file:
            writer = csv.writer(file) #writer é um objeto criado do tipo csv.writer ele será responsavel por criar linhas no codigo
            writer.writerow(['Nome', 'Titulo', 'Cidade', 'Estado', 'CEP', 'Escola', 'Zona', 'Sessao', 'Partida', 'Numero Eleitoral']) #Criando um cabeçalho adicionando ele a primeira linha

            #preenchendo o csv com dados da lista prefeitos com writerow que permite escrever nas linhas.
            for prefeito in self.prefeitos:
                writer.writerow([prefeito.get_nome(), prefeito.get_titulo(), prefeito.local.cidade.nome, prefeito.local.cidade.estado, prefeito.local.cidade.cep, prefeito.local.escola, prefeito.local.zona, prefeito.local.sessao, prefeito.partido, prefeito.numeroEleitoral])

    def adicionandoVereadoresCsv (self):
        caminho = "arquivos_csv/vereadores.csv"
        with open(caminho, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Titulo', 'Cidade', 'Estado', 'CEP', 'Escola', 'Zona', 'Sessao', 'Partida', 'Numero Eleitoral'])

            for vereador in self.vereadores:
                writer.writerow([vereador.get_nome(), vereador.get_titulo(), vereador.local.cidade.nome, vereador.local.cidade.estado, vereador.local.cidade.cep, vereador.local.escola, vereador.local.zona, vereador.local.sessao, vereador.partido, vereador.numeroEleitoral])

    def adicionarUrnaCsv (self):
        caminho= "arquivos_csv/urnas.csv"
        with open(caminho,mode="w", newline='') as file:
            writer= csv.writer(file)
            writer.writerow(['Cidade', 'Estado', 'CEP', 'Escola','Zona', 'Sessão', 'Status'])

            for urna in self.urnas:
                writer.writerow([urna.local.cidade.nome, urna.local.cidade.estado, urna.local.cidade.cep, urna.local.escola, urna.local.zona, urna.local.sessao, urna.status])

    def criarDataFrameEleitor(self):
        #Utilizando o pandas aqui, para mostrar as listas com os dados presentes nela em formato de tabela.
        tabela_eleitores = {
            # Nome, titulo, sessão e idade são colunas que seram preenchidas pela lista GerenciadorEleitoral.eleitores
            'Nome': [eleitor.get_nome() for eleitor in GerenciadorEleitoral.eleitores], 
            'Titulo': [eleitor.get_titulo() for eleitor in GerenciadorEleitoral.eleitores],
            'Cidade': [eleitor.local.cidade.nome for eleitor in GerenciadorEleitoral.eleitores],
            'Estado': [eleitor.local.cidade.estado for eleitor in GerenciadorEleitoral.eleitores],
            'CEP': [eleitor.local.cidade.cep for eleitor in GerenciadorEleitoral.eleitores],
            'Escola': [eleitor.local.escola for eleitor in GerenciadorEleitoral.eleitores],
            'Zona': [eleitor.local.zona for eleitor in GerenciadorEleitoral.eleitores],
            'Sessao': [eleitor.local.sessao for eleitor in GerenciadorEleitoral.eleitores],
            'Votou': [eleitor.votou for eleitor in GerenciadorEleitoral.eleitores]
            
        }
        return pd.DataFrame(tabela_eleitores) #retorna um objeto do tipo dataframe do Pandas (retorna uma tabela) aparti do dicionario tabela_eleitores.

    #codigo abaixo segue a mesma lógica.
    def criarDataFramePrefeito (self):
        tabela_prefeitos = {
            'Nome': [prefeito.get_nome() for prefeito in GerenciadorEleitoral.prefeitos],
            'Titulo': [prefeito.get_titulo() for prefeito in GerenciadorEleitoral.prefeitos],
            'Cidade': [prefeito.local.cidade.nome for prefeito in GerenciadorEleitoral.prefeitos],
            'Estado': [prefeito.local.cidade.estado for prefeito in GerenciadorEleitoral.prefeitos],
            'CEP': [prefeito.local.cidade.cep for prefeito in GerenciadorEleitoral.prefeitos],
            'Escola': [prefeito.local.escola for prefeito in GerenciadorEleitoral.prefeitos],
            'Zona': [prefeito.local.zona for prefeito in GerenciadorEleitoral.prefeitos],
            'Sessão': [prefeito.local.sessao for prefeito in GerenciadorEleitoral.prefeitos],
            'Partido': [prefeito.partido for prefeito in GerenciadorEleitoral.prefeitos],
            'Numero': [prefeito.numeroEleitoral for prefeito in GerenciadorEleitoral.prefeitos]
        }
        return pd.DataFrame(tabela_prefeitos)

    def criarDataFrameVereador (self):
        tabela_vereadores = {
            'Nome': [vereador.get_nome() for vereador in GerenciadorEleitoral.vereadores],
            'Titulo': [vereador.get_titulo() for vereador in GerenciadorEleitoral.vereadores],
            'Cidade': [vereador.local.cidade.nome for vereador in GerenciadorEleitoral.vereadores],
            'Estado': [vereador.local.cidade.estado for vereador in GerenciadorEleitoral.vereadores],
            'CEP': [vereador.local.cidade.cep for vereador in GerenciadorEleitoral.vereadores],
            'Escola': [vereador.local.escola for vereador in GerenciadorEleitoral.vereadores],
            'Zona': [vereador.local.zona for vereador in GerenciadorEleitoral.vereadores],
            'Sessão': [vereador.local.sessao for vereador in GerenciadorEleitoral.vereadores],
            'Partido': [vereador.partido for vereador in GerenciadorEleitoral.vereadores],
            'Numero': [vereador.numeroEleitoral for vereador in GerenciadorEleitoral.vereadores]
        }
        return pd.DataFrame(tabela_vereadores)

    def criarDataFrameUrna (self):
        data = {
            'Cidade': [urna.local.cidade.nome for urna in GerenciadorEleitoral.urnas],
            'Estado': [urna.local.cidade.estado for urna in GerenciadorEleitoral.urnas],
            'CEP': [urna.local.cidade.cep for urna in GerenciadorEleitoral.urnas],
            'Escola': [urna.local.escola for urna in GerenciadorEleitoral.urnas],
            'Zona': [urna.local.zona for urna in GerenciadorEleitoral.urnas],
            'Sessão': [urna.local.sessao for urna in GerenciadorEleitoral.urnas],
            'Status': [urna.status for urna in GerenciadorEleitoral.urnas]
        }
        return pd.DataFrame(data)
