from Grafo import Graph
import numpy as np
class parser:

    def parser(self,mapa):
        file = open(mapa, "r")   # Abertura do file
        lines = file.readlines()        # Leitura das linhas do file
        file.close()                    # Fecho do file
        nLines = 0                      # Contador para saber quantas linhas tem o file
        dict_Mapa = {}                  # Dicionário para guardar todos os caracteres das linhas lidas
        # TIPO DO DICT: (Nº da linha no ficheiro,Nº da coluna no ficheiro): Caractere que se encontra nessa posição do ficheiro
        # Neste caso, como cada caractere ocupa 2 posições então vamos ter as colunas com números par, isto é,
        # quando supostamente iria ser a coluna número 1 é a coluna número 2
        # Onde deveria ser coluna : 0 - 1 - 2 -3
        # É coluna: 0 - 2 - 4 - 6

        for line in lines:             # Percorrer todas as linhas do file
            tamanhoLinha=(len(line))   # Como a matriz, começa na coluna 0 e linha 0 tira-se uma unidade (Exemplo: 6 colunas- 0..2..4..6..8..10)
            for i in range(int(tamanhoLinha)): # Percorrer a linha toda, caractere a caractere
                if (line[i]=='#'):       # Verificação do caractere- Neste caso # é uma parede
                        dict_Mapa[(nLines,i)]=1 # Coloca-se no dict, a coordenada da parede (A parede na matriz do mapa é representado por um 1)
                if (line[i]=='-'):       # Verificação do caractere- Neste caso - é por onde passa a pista
                        dict_Mapa[(nLines,i)]=0 # Coloca-se no dict, a coordenada da pista (A pista na matriz do mapa é representado por um 0)
                if (line[i]=='F'):       # Verificação do caractere- Neste caso F é a meta
                        dict_Mapa[(nLines,i)] = 2    # Coloca-se no dict, a coordenada da meta (A meta na matriz do mapa é representado por um 2)
                if (line[i]=='P'):        # Verificação do caractere- Neste caso P é a partida
                        dict_Mapa[(nLines,i)] = -1  # Coloca-se no dict, a coordenada da partida (A partida na matriz do mapa é representado por um -1)

            nLines=nLines+1           # Aumenta-se o contador do número de linhas do ficheiro que já foram analisadas

        return (dict_Mapa)            # Retorna-se o dicionário(matriz) com o mapa em números da pista
    def calcula_listaAdj(self,key,dic):  # Calculo da lista de adjacência de um nodo do grafo
        #print("Calculo da matriz de adjacencias do nodo",key)
        listaR=[]      # Lista de adjacência do resultado
        for keyD in dic:   # Percorre todas as chaves do dicionário- A chave indica a posição do caracter na pista
            #print(keyD)
            if (dic[keyD]==0 or dic[keyD]==2 or dic[keyD]==-1):   # Verifica se o elemento a analisar pode ser nodo adjacente do dado como input
                if (keyD[0]==(key[0]+1) and keyD[1]==(key[1])):   # Condição que verifica se o nodo é adjacente ao dado
                    listaR.append(keyD)                           # Coloca o nodo na lista de adjacência
                if (keyD[0]==(key[0]-1) and keyD[1]==(key[1])):   # Condição que verifica se o nodo é adjacente ao dado
                    listaR.append(keyD)                           # Coloca o nodo na lista de adjacência
                if (key[0]==(keyD[0]) and keyD[1]==(key[1])+2):   # Condição que verifica se o nodo é adjacente ao dado
                    listaR.append(keyD)                           # Coloca o nodo na lista de adjacência
                if (key[0]==(keyD[0]) and keyD[1]==(key[1])-2):   # Condição que verifica se o nodo é adjacente ao dado
                    listaR.append(keyD)                             # Coloca o nodo na lista de adjacência
                if  (keyD[0]==(key[0]+1) and keyD[1]==(key[1])+2):   # Condição que verifica se o nodo é adjacente ao dado
                    listaR.append(keyD)                               # Coloca o nodo na lista de adjacência
                if  (keyD[0]==(key[0]+1) and keyD[1]==(key[1])-2):   # Condição que verifica se o nodo é adjacente ao dado
                    listaR.append(keyD)                               # Coloca o nodo na lista de adjacência
                if  (keyD[0]==(key[0]-1) and keyD[1]==(key[1])-2):   # Condição que verifica se o nodo é adjacente ao dado
                    listaR.append(keyD)                               # Coloca o nodo na lista de adjacência
                if  (keyD[0]==(key[0]-1) and keyD[1]==(key[1])+2):   # Condição que verifica se o nodo é adjacente ao dado
                    listaR.append(keyD)

        return listaR      # Dá se o return da lista de adjacência

    def create_Grafo(self,dict):       # Calcula o grafo que mais se adequa ao mapa fornecido, por isso o parametro
        g=Graph()                      # Criação inicial do grafo
        for key in dict:               # Todo o dicionário é percorrido
            if dict[key]==0:           # Se o nodo pertence á pista, então calculamos os nodos adjacentes ao mesmo
                #print("Este é o ponto onde vai ser calculado a matriz de adj",key)
                nomeNodo=str(key[0])+str(key[1])   # Criação de um nome para o nodo (Neste caso, é xy)
                lista1= self.calcula_listaAdj(key, dict)   # Calculo da lista de nodos adjacentes
                for it1 in lista1:                         # Percorrer a lista de adjacencia daquele nodo
                    nomeNodoAdj=str(it1[0])+str(it1[1])    # Criação de um nome para o nodo (Neste caso, é xy)
                    g.add_edge(nomeNodo,nomeNodoAdj,1)     # Criação de uma aresta no grafo que representa o mapa
            if dict[key]==2:           # Se o nodo pertence á meta, então calculamos os nodos adjacentes ao mesmo
                #print("Este é o ponto onde vai ser calculado a matriz de adj", key)
                nomeNodo = str(key[0]) + str(key[1])  #Criação de um nome para o nodo (Neste caso, é xy)
                lista2 = self.calcula_listaAdj(key, dict) # Calculo da lista de nodos adjacentes
                for it2 in lista2:   # Percorrer a lista de adjacencia daquele nodo
                    nomeNodoAdj=str(it2[0])+str(it2[1])  # Criação de um nome para o nodo (Neste caso, é xy)
                    g.add_edge(nomeNodo,nomeNodoAdj,1)   # Criação de uma aresta no grafo que representa o mapa
            if dict[key]==-1:          # Se o nodo pertence á partida, então calculamos os nodos adjacentes ao mesmo
                #print("Este é o ponto onde vai ser calculado a matriz de adj", key)
                nomeNodo = str(key[0]) + str(key[1])  #Criação de um nome para o nodo (Neste caso, é xy)
                lista3 = self.calcula_listaAdj(key, dict)  # Calculo da lista de nodos adjacentes
                for it3 in lista3: # Percorrer a lista de adjacencia daquele nodo
                    nomeNodoAdj = str(it3[0]) + str(it3[1]) # Criação de um nome para o nodo (Neste caso, é xy)
                    g.add_edge(nomeNodo, nomeNodoAdj, 1) # Criação de uma aresta no grafo que representa o mapa
        return g # O grafo que representa o mapa é retornado








