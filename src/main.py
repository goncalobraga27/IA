from vector_race import VectorRace


def main():
    print("------------------VECTOR RACE------------------")

    vector_race = None
    configured = False
    while not configured:
        print("Insira ficheiro com o mapa do jogo: ", end="")
        map_file = str(input())
        try:
            vector_race = VectorRace(map_file)
            vector_race.parser()
            configured = True
        except:
            print("Mapa inválido")

    if configured:
        print("Mapa configurado")
        vector_race.create_graph()
        nf = vector_race.goal.pop()
        vector_race.goal.add(nf)
        vector_race.graph_heuristic(nf)

        option = -1
        while option != 0:
            print("1-Imprimir Grafo")
            print("2-Desenhar Grafo")
            print("3-Imprimir  nodos do Grafo")
            print("4-Imprimir arestas do Grafo")
            print("5-BDS")
            print("6-DFS")
            print("7-Pesquisa Gulosa")
            print("8-Pesquisa A*")
            print("0-Sair")

            print("Intruza a sua opção: ", end="")
            option = int(input())
            match option:
                case 1:
                    print(vector_race.graph)
                case 2:
                    print(vector_race.graph.graph_draw())
                case 3:
                    print(vector_race.graph.show_nodes())
                    print()
                case 4:
                    print(vector_race.graph.show_edges())
                case 5:
                    print(vector_race.search_bfs_race())
                    print()
                case 6:
                    print(vector_race.search_dfs_race())
                    print()
                case 7:
                    print(vector_race.search_greedy())
                    print()
                case 8:
                    print(vector_race.search_star_a())
                    print()
                case 0:
                    option = 0
                case _:
                    print("Opção invalida.")
                    print()


if __name__ == "__main__":
    main()
