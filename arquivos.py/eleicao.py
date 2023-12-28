import csv
from abc import ABC, abstractmethod

import pandas as pd
from gerenciador import GerenciadorEleitoral
from moviepy.editor import VideoFileClip

#Class responsável por designar os partidos
class Partido:
    partidos = []

    def _init_(self, nome):
        self.nome = nome
        self.membros = []
        Partido.partidos.append(self)

    #Metódo responsável
    def adicionar_membros(self, membro):
        if isinstance(membro, Candidato):
            self.membros.append(membro)

    @classmethod
    def exibir_partidos(cls):
        for partido in cls.partidos:
            print(partido)

    def _str_(self):
        return f"{self.nome}"
        
class Eleitor:
    def _init_(self, nome, titulo, local, votou=False):
        self.__nome = nome
        self.__titulo = titulo
        self.local= local
        self.votou= votou

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def get_local(self):
        self.local

    def _str_(self):
        return f"Nome: {self.__nome}\n"\
        f"titulo: {self.__titulo}\n"\
        f"Cidade: {self.local.cidade.nome}\n"\
        f"Estado: {self.local.cidade.estado}\n"\
        f"CEP: {self.local.cidade.cep}\n"\
        f"Escola: {self.local.escola}\n"\
        f"Zona: {self.local.zona}\n"\
        f"Sessão {self.local.sessao}"
    
        f"---------------------------------"

class Comicio(ABC):
    @abstractmethod
    def realizar_comicio():
        pass

class Candidato(Eleitor, Partido):
    def _init_(self, nome, titulo, local, partido,numeroEleitoral,votou=False):
        super()._init_(nome, titulo, local)
        self.partido = partido
        self.numeroEleitoral=numeroEleitoral
        self.votou=votou

    def _str_(self):
        return f"-----------------------------------\n"\
        f"Nome: {self.get_nome()}\n"\
        f"titulo: {self.get_titulo()}\n"\
        f"sessao: {self.get_sessao()}\n"\
        f"idade: {self.get_idade()}\n"\
        f"Partido: {self.partido}\n"\
        f"Cidade: {self.cidade.nome}\n"\
        f"Estado: {self.cidade.estado}\n"\
        f"CEP: {self.cidade.cep}\n"\
        f"Numero Eleitoral: {self.numeroEleitoral}\n"\
        f"-----------------------------------"


class Prefeito(Candidato,Comicio):
    def _init_(self, nome, titulo, local, partido, numeroEleitoral, votou=False):
        super()._init_(nome, titulo, local, partido, numeroEleitoral,votou=False)
        self.votou=votou
        self.votos=0

    def propostas(self,candidato):
        if candidato=="Frederico":
            caminho= "videos/candidato_Frederico.mp4"
            clip= VideoFileClip(caminho)
            clip.preview()
        elif candidato=="Joelma":
            caminho= "videos/candidata_Joelma.mp4"
            clip= VideoFileClip(caminho)
            clip.preview()
        else:
            return f"Não há proposta desse candidato"

    def realizar_comicio(self):
        print(f"Prefeito {self.get_nome()} realizando Comicio.")

class Vereador(Candidato):
    def _init_(self, nome, titulo, local, partido, numeroEleitoral, votou=False):
        super()._init_(nome, titulo, local, partido, numeroEleitoral, votou=False)
        self.votos=0
        self.votou=votou
    
    def realizar_comicio(self):
        print(f"Vereador {self.get_nome()} realizando Comicio.")

class Cidade:
    def _init_(self,nome,estado,cep):
        self.nome=nome
        self.estado=estado
        self.cep=cep

class Debate:
    @classmethod
    def debater(self):
        video_debate= "videos/debate.mp4"
        clip= VideoFileClip(video_debate)
        clip.preview()

class UrnaEletronica(GerenciadorEleitoral):

    def _init_(self, local, status=False):
        self.local = local
        self.status = status
        self.resultadoPrefeito = {}
        self.resultadoVereador = {}
        self.votosEmNuloPrefeito = 0
        self.votosEmNuloVereador = 0
    
    def iniciar_votacao(self):
        if self.status==True:
            print("Votação já havia sido foi iniciada.")
        else:
            self.status=True
            print("Urna ativada para votação.")

    def adicionar_voto(self,eleitor):
        if eleitor.votou == True:
            return f"Eleitor já votou"
        else:
            print("Candidados a Prefeitos:")
            for prefeito in GerenciadorEleitoral.prefeitos:
                print(f"{prefeito.get_nome()} - {prefeito.numeroEleitoral}")
            print("Voto Nulo - 01")
            numero= input("Informe seu voto: ")
            for prefeito in GerenciadorEleitoral.prefeitos:
                if numero==prefeito.numeroEleitoral:
                    self.resultadoPrefeito[prefeito.get_nome()] = self.resultadoPrefeito.get(prefeito.get_nome(), 0) + 1
                    print("Voto adicionado com sucesso!")
                    print("-"*30)
                    print("Candidatos a Vereadores")
                elif(numero=="01"):
                    self.votosEmNuloPrefeito+=1
                    print("Voto adicionado com sucesso!")
                    print("-"*30)
                    print("Candidatos a Vereadores")
            for vereador in GerenciadorEleitoral.vereadores:
                print(f"{vereador.get_nome()} - {vereador.numeroEleitoral}")
            numero= input("Informe seu voto: ")
            for vereador in GerenciadorEleitoral.vereadores:
                if numero==vereador.numeroEleitoral:
                    self.resultadoVereador[vereador.get_nome()] = self.resultadoVereador.get(vereador.get_nome(), 0) + 1
                    eleitor.votou=True
                    return f"Voto conclído"
                elif(numero=="01"):
                    self.votosEmNuloVereador+=1
                    eleitor.votou=True
                    return f"Voto concluido completamente."
    
    def encerrar_votacao(self):
        if self.status==True:
            print(f"Encerrando votacao na urna da sessao {self.local.sessao}")
            self.status=False

    def emitirBoletim(self): #Função exibir resultado de cada Urna
        if self.status == False:
            print("-"*55)
            print(f"Boletim para a urna:\n")
            print(self)
            print("Candidatos a Prefeito:")
            for prefeito in GerenciadorEleitoral.prefeitos:
                votos = self.resultadoPrefeito.get(prefeito.get_nome(), 0)
                print(f"{prefeito.get_nome()}, total de votos: {votos}") #Exibi os votos que cada Prefeito recebeu
            print("Votos em nulo: ",self.votosEmNuloPrefeito)  #Exibi os votos que foram nulos na votação a prefeito.
            print("-"*55)
            #Seguir a mesma lógica do codigo acima.
            print("Candidatos a Vereador:")
            for vereador in GerenciadorEleitoral.vereadores:
                votos = self.resultadoVereador.get(vereador.get_nome(), 0)
                print(f"{vereador.get_nome()}, total de votos: {votos}")
            print("Votos em nulo: ",self.votosEmNuloVereador)
            input("\nAperte enter para voltar pro menu")

    def _str_(self):
        return f"Urna Eletrônica:\n" \
               f"Cidade: {self.local.cidade.nome}\n"\
               f"Estado: {self.local.cidade.estado}\n"\
               f"CEP: {self.local.cidade.cep}\n"\
               f"Escola: {self.local.escola}\n"\
               f"Zona: {self.local.zona}\n"\
               f"Sessão: {self.local.sessao}\n" \
               f"Status: {'Ativa' if self.status else 'Inativa'}\n" \
               f"-------------------------------------------------------"
    
class Local:
    def _init_(self, cidade, escola, zona, sessao):
        self.cidade=cidade
        self.escola = escola
        self.zona = zona
        self.sessao = sessao

class Boletim:
    @classmethod
    def exibirResultado(self, urnas):
        print("-" * 50)
        print("Boletim Geral - Votos Totais de Todas as Urnas")

        #Dicionarios abaixo vão servir para adicionar os votos totais dos candidatos.
        resultadoPrefeitos = {}
        resultadoVereadores = {}

        #Percorre todas as urnas
        for urna in urnas:
            #Atualiza resultados totais para prefeitos.
            for prefeito, votos in urna.resultadoPrefeito.items():
                resultadoPrefeitos[prefeito] = resultadoPrefeitos.get(prefeito, 0) + votos

            #Atualiza resultados totais para vereadores.
            for vereador, votos in urna.resultadoVereador.items():
                resultadoVereadores[vereador] = resultadoVereadores.get(vereador, 0) + votos

        #Imprimir o boletim final com o resultado dos votos para prefeitos.
        print("Candidatos a Prefeito:")
        for prefeito, votos in resultadoPrefeitos.items():
            print(f"{prefeito}, total de votos: {votos}")

        
        #Imprimir o boletim final com o resultado dos votos para vereadores.
        print("-" * 50)
        print("Candidatos a Vereador:")
        for vereador, votos in resultadoVereadores.items():
            print(f"{vereador}, total de votos: {votos}")