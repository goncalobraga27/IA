from Parser import parser
from Grafo import Graph
import networkx as nx

import matplotlib.pyplot as plt
def main():

    p=parser()
    gh=Graph()
    dict=p.parser("mapa1.txt")
    g=p.create_Grafo(dict)
    # lista=g.imprime_aresta()
    g.desenha()

if __name__ == "__main__":
    main()