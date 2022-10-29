from parser import Parser
from graph import Graph


def main():

    p = Parser("mapa1.txt")
    p.parser()
    g = p.create_graph()
    g.graph_draw()


if __name__ == "__main__":
    main()
