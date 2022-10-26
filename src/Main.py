from Parser import parser
from Grafo import Graph
def main():

    p=parser()
    gh=Graph()
    dict=p.parser("mapa1.txt")
    g=p.create_Grafo(dict)
    lista=g.imprime_aresta()
    print(lista)

if __name__ == "__main__":
    main()