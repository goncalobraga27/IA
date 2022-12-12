from vector_race import VectorRace
from tkinter import *

def chose_heuristic(vector_race):
    print()
    print("-------------------------------------------------")
    print("Qual é a heurística que deseja utilizar?")
    print("1-Distância para a meta")
    print("2-Encontra-se bem posicionado na pista")
    print("Introduza a sua opção: ", end="")
    heuristic = int(input())
    while heuristic != 1 and heuristic != 2:
        print("Opção errada")
        print("Intoduza a sua opação: ", end="")
        heuristic = int(input())
    print("-------------------------------------------------")

    if heuristic == 1:
        vector_race.graph_heuristic()
    else:
        vector_race.graph_heuristic_wall()


def main():
    print("------------------VECTOR RACE--------------------")

    vector_race = None
    configured = False
    while not configured:
        print("Insira ficheiro com o circuito do jogo: ", end="")
        map_file = str(input())
        try:
            vector_race = VectorRace.parser(map_file)
            vector_race.show_parser(map_file)
            configured = True
        except:
            print("Circuito inválido")

    if configured:
        print("Circuito configurado")
        print("-------------------------------------------------")

        print()
        print("Introduza o número de jogadores (max 4): ", end="")
        option_players = int(input())
        while 1 > option_players > 4:
            print()
            print("Opção errada")
            print("Intoduza a sua opção: ", end="")
            option_players = int(input())

        vector_race.create_graph()

        if option_players == 1:

            option = -1
            while option != 0:
                print()
                print("1-Imprimir circuito")
                print("2-Imprimir Grafo")
                print("3-Desenhar Grafo")
                print("4-Imprimir nodos do Grafo")
                print("5-Imprimir arestas do Grafo")
                print("6-BFS")
                print("7-DFS")
                print("8-Pesquisa Gulosa")
                print("9-Pesquisa A*")
                print("0-Sair")

                print("Introduza a sua opção: ", end="")
                option = int(input())
                match option:
                    case 1:
                        print(vector_race.print_map())
                    case 2:
                        print(vector_race.graph)
                    case 3:
                        vector_race.graph.graph_draw()
                    case 4:
                        print(vector_race.graph.show_nodes())
                        print()
                    case 5:
                        print(vector_race.graph.show_edges())
                    case 6:
                        path, cost = vector_race.search_bfs_race()
                        print(path, cost)
                        print()
                        print(vector_race.print_map(path))
                    case 7:
                        path, cost = vector_race.search_dfs_race()
                        print(path, cost)
                        print()
                        print(vector_race.print_map(path))
                    case 8:
                        chose_heuristic(vector_race)
                        path, cost = vector_race.search_greedy()
                        print(path, cost)
                        print()
                        print(vector_race.print_map(path))
                    case 9:
                        chose_heuristic(vector_race)
                        path, cost = vector_race.search_star_a()
                        print(path, cost)
                        print()
                        print(vector_race.print_map(path))
                    case 0:
                        option = 0
                    case _:
                        print("Opção invalida.")
                        print()
        else:
            vector_race.two_players()
def dealWithMap(janelaInitial):
    vector_race = VectorRace()
    nomeFile = vMapa.get()
    try:
        vector_race.parser(nomeFile)
        vector_race.show_parser(nomeFile)
        Label(janelaInitial, text="Circuito configurado").place(x=220, y=450)
    except:
        Label(janelaInitial, text="Circuito inválido").place(x=220, y=450)

janelaInitial = Tk()
janelaInitial.geometry("600x600")
janelaInitial.title("VECTOR RACE")
Label(janelaInitial, text="VECTOR RACE", font=('calibre', 15, 'bold'), anchor=W).place(x=190, y=200, width=500)
Label(janelaInitial, text="Insira ficheiro com o circuito do jogo: ", background="#dde",
      foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=150, y=300, width=250)
vMapa = Entry(janelaInitial)
vMapa.place(x=150, y=320, width=250, height=20)
Button(janelaInitial, text="Procurar", command=lambda: dealWithMap(janelaInitial)).place(x=220, y=370)
janelaInitial.mainloop()


if __name__ == "__main__":
    main()
