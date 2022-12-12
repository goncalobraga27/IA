from vector_race import VectorRace


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


if __name__ == "__main__":
    main()
