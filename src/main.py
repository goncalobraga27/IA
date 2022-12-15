from vector_race import VectorRace
from interface import ui

def chose_heuristic(vector_race):
    print("\n-------------------------------------------------")
    print("Qual é a heurística que deseja utilizar?")
    print("1-Distância para a meta")
    print("2-Encontra-se bem posicionado na pista")
    print("-------------------------------------------------")
    print("Introduza a sua opção: ", end="")
    heuristic = int(input())
    while heuristic != 1 and heuristic != 2:
        print("Opção errada")
        print("Intoduza a sua opação: ", end="")
        heuristic = int(input())

    if heuristic == 1:
        vector_race.graph_heuristic()
    else:
        vector_race.graph_heuristic_wall()


# 1 - DFS, 2 - BFS, 3 - Greedy, 4 - A*
def chose_player_algorithm(num):
    print("\n-----------------------------------------------------------")
    print("Indique o algoritmo de procura a utilizar pelo jogador " + str(num))
    print("1 - DFS")
    print("2 - BFS")
    print("3 - Greedy")
    print("4 - A*")
    print("-----------------------------------------------------------")


def invalid_option():
    print()
    print("Opção errada")
    print("Intoduza a sua opção: ", end="")
    return int(input())


def single_player_menu():
    print("\n------------------------------------------------")
    print("1-Imprimir Circuito")
    print("2-Desenhar Circuito")
    print("3-Imprimir Grafo")
    print("4-Desenhar Grafo")
    print("5-Imprimir Nodos do Grafo")
    print("6-Imprimir Arestas do Grafo")
    print("7-BFS")
    print("8-DFS")
    print("9-Pesquisa Gulosa")
    print("10-Pesquisa A*")
    print("0-Sair")
    print("------------------------------------------------")


def option1(vector_race):
    option = -1
    while option != 0:
        single_player_menu()

        print("Introduza a sua opção: ", end="")
        option = int(input())
        match option:
            case 1:
                print()
                print(vector_race.print_map())
            case 2:
                vector_race.draw_circuit(vector_race.start)
            case 3:
                print()
                print(vector_race.graph, end="")
            case 4:
                vector_race.graph.graph_draw()
            case 5:
                print()
                print(vector_race.graph.show_nodes())
            case 6:
                print()
                print(vector_race.graph.show_edges())
            case 7:
                print()
                path, cost = vector_race.search_bfs_race()
                print(path, end=", Cost=")
                print(cost, end="\n\n")
                print(vector_race.print_map(path))
                vector_race.draw_circuit_path(path)
                print("Um gif com o caminho tomado pelo carro foi gerado")
            case 8:
                print()
                path, cost = vector_race.search_dfs_race()
                print(path, end=", Cost=")
                print(cost, end="\n\n")
                print(vector_race.print_map(path))
                vector_race.draw_circuit_path(path)
                print("Um gif com o caminho tomado pelo carro foi gerado")
            case 9:
                chose_heuristic(vector_race)
                print()
                path, cost = vector_race.search_greedy()
                print(path, end=", Cost=")
                print(cost, end="\n\n")
                print(vector_race.print_map(path))
                vector_race.draw_circuit_path(path)
                print("Um gif com o caminho tomado pelo caro foi gerado")
            case 10:
                chose_heuristic(vector_race)
                print()
                path, cost = vector_race.search_star_a()
                print(path, end=", Cost=")
                print(cost, end="\n\n")
                print(vector_race.print_map(path))
                vector_race.draw_circuit_path(path)
                print("Um gif com o caminho tomado pelo carro foi gerado")
            case 0:
                option = 0
            case _:
                print("Opção invalida.")


def other_options(vector_race, choices):
    winner = vector_race.multiplayer(choices)
    print("Jogador " + str(winner) + " venceu!")


def main():
    userInterface = ui()
    userInterface.interface()
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
        print("Introduza o número de jogadores (max 4): ", end="")
        option_players = int(input())
        while option_players < 1 or option_players  > 4:
            option_players = invalid_option()

        vector_race.create_graph()

        if option_players == 1:
            option1(vector_race)
        else:
            save_choices = []
            for i in range(option_players):
                chose_player_algorithm(i + 1)
                print("Introduza a sua opção: ", end="")
                inp = int(input())
                while inp < 1 or inp > 4:
                    inp = invalid_option()
                save_choices.append(inp)
            other_options(vector_race, save_choices)

if __name__ == "__main__":
    main()
