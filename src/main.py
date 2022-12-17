import tkinter
from vector_race import VectorRace


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


def main_ant():
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
        while option_players < 1 or option_players > 4:
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




race = VectorRace()
num_players = int()
exception = ""
choices = []

def config_map(window,map_file,num):
    try:
        global race
        global num_players
        global exception
        if num < 1 or num > 4:
            raise ValueError("Número de jogadores inválido.")
        num_players = num
        race = VectorRace.parser(map_file) # threads aqui
        race.show_parser(map_file)
    except FileNotFoundError:
        exception = "O ficheiro não existe."
    except ValueError:
        exception = "Número de jogadores inválido."
    finally:
        window.destroy()

def show_results(path, cost):
    out = "Caminho:\n"
    i = 0
    for node in path:
        out = out + str(node) + ", "
        if i == 1:
            out = out + "\n"
            i = 0
        else:
            i += 1
    out = out + "\nCusto: " + str(cost)

    window = tkinter.Tk()
    window.geometry("480x680")
    window.title("VECTOR RACE")
    window.configure(bg='#C2C2C2')
    frame_1 = tkinter.Frame(master=window, bg='#C2C2C2')
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)
    label_1 = tkinter.Label(master=frame_1, justify=tkinter.LEFT,
                            text=out, font=('Roboto', 10, 'normal'),
                            bg='#C2C2C2')
    label_1.pack(pady=12, padx=10)
    window.mainloop()

def search_dfs():
    path, cost = race.search_dfs_race()
    race.draw_circuit_path(path) # mudar para mostrar no matplotlib
    show_results(path, cost)

def search_bfs():
    path, cost = race.search_bfs_race()
    race.draw_circuit_path(path)
    show_results(path, cost)

def uniform_cost():
    path, cost = race.search_uniform_cost()
    race.draw_circuit_path(path)
    show_results(path, cost)

def greedy_fst():
    race.graph_heuristic()
    path, cost = race.search_greedy()
    race.draw_circuit_path(path)
    show_results(path, cost)

def greedy_snd():
    race.graph_heuristic_wall()
    path, cost = race.search_greedy()
    race.draw_circuit_path(path)
    show_results(path, cost)

def a_star_fst():
    race.graph_heuristic()
    path, cost = race.search_star_a()
    race.draw_circuit_path(path)
    show_results(path, cost)

def a_star_snd():
    race.graph_heuristic_wall()
    path, cost = race.search_star_a()
    race.draw_circuit_path(path)
    show_results(path, cost)

def fill_choices(window,entrys):
    global choices
    for i in range(num_players):
        choices.append(int(entrys[i].get()))
    window.destroy()

def main():
    window = tkinter.Tk()
    window.geometry("480x380")
    window.title("VECTOR RACE")
    window.configure(bg='#C2C2C2')
    frame_1 = tkinter.Frame(master=window, bg='#C2C2C2')
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)
    label_1 = tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="Vector Race", font=('Roboto', 24, 'bold'), bg='#C2C2C2')
    label_1.pack(pady=12, padx=10)
    label_1 = tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="Ficheiro com o mapa do jogo:", font=('Roboto', 10, 'normal'), bg='#C2C2C2')
    label_1.pack(pady=12, padx=10)
    entry_1 = tkinter.Entry(master=frame_1, bg='white')
    entry_1.pack(pady=12, padx=10)
    label_2 = tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="Número de jogadores (1 a 4):", font=('Roboto', 10, 'normal'), bg='#C2C2C2')
    label_2.pack(pady=12, padx=10)
    entry_2 = tkinter.Entry(master=frame_1, bg='white')
    entry_2.pack(pady=12, padx=10)
    button_1 = tkinter.Button(master=frame_1, text="Configurar", command=lambda: config_map(window,entry_1.get(),int(entry_2.get())), bg='black', fg='white')
    button_1.pack(pady=12, padx=10)
    window.mainloop()

    if (race is not None) and (num_players == 1):
        race.create_graph()
        window = tkinter.Tk()
        window.geometry("480x680")
        window.title("VECTOR RACE")
        window.configure(bg='#C2C2C2')
        frame_1 = tkinter.Frame(master=window, bg='#C2C2C2')
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Desenhar Circuito", command=lambda:race.draw_circuit(race.start), bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Desenhar Grafo", command=race.graph.graph_draw, bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Algoritmo DFS", command=lambda:search_dfs(), bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Algoritmo BFS", command=lambda:search_bfs(), bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Algoritmo Custo Uniforme", command=lambda:uniform_cost(), bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Algoritmo Greedy - Distância à meta", command=lambda:greedy_fst(), bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Algoritmo Greedy - Posição na pista", command=lambda:greedy_snd(), bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Algoritmo A* - Distância à meta", command=lambda:a_star_fst(), bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Algoritmo A* - Posição na pista", command=lambda:a_star_snd(), bg='black', fg='white').pack(pady=12, padx=10)
        tkinter.Button(master=frame_1, justify=tkinter.LEFT, text="Fechar", command=window.destroy, bg='black', fg='white').pack(pady=12, padx=10)
        window.mainloop()
    elif race is not None:
        # selecionar heuristica para cada player e simular
        window = tkinter.Tk()
        window.geometry("480x680")
        window.title("VECTOR RACE")
        window.configure(bg='#C2C2C2')
        frame_1 = tkinter.Frame(master=window, bg='#C2C2C2')
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)
        tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="Algoritmos", font=('Roboto', 24, 'bold'), bg='#C2C2C2').pack(pady=12, padx=10)
        tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="1 - DFS", font=('Roboto', 10, 'normal'), bg='#C2C2C2').pack(pady=12, padx=10)
        tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="2 - BFS", font=('Roboto', 10, 'normal'), bg='#C2C2C2').pack(pady=12, padx=10)
        tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="3 - Greedy", font=('Roboto', 10, 'normal'), bg='#C2C2C2').pack(pady=12, padx=10)
        tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="4 - A*", font=('Roboto', 10, 'normal'), bg='#C2C2C2').pack(pady=12, padx=10)

        entrys = []
        for i in range(num_players):
            label_1 = tkinter.Label(master=frame_1, justify=tkinter.LEFT, text="Selecione o algoritmo a utilizar pelo jogador " + str(i+1) + ":",
                                    font=('Roboto', 10, 'normal'), bg='#C2C2C2')
            label_1.pack(pady=12, padx=10)
            entrys.append(tkinter.Entry(master=frame_1, bg='white'))
            entrys[i].pack(pady=12, padx=10)

        button_1 = tkinter.Button(master=frame_1, text="Selecionar", command=lambda:fill_choices(window,entrys), bg='black', fg='white')
        button_1.pack(pady=12, padx=10)
        window.mainloop()

        race.multiplayer(choices)
    else:
        global exception
        window = tkinter.Tk() # error parsing the file or file not exist
        window.geometry("480x180")
        window.title("VECTOR RACE")
        window.configure(bg='#C2C2C2')
        frame_1 = tkinter.Frame(master=window, bg='#C2C2C2')
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)
        label_1 = tkinter.Label(master=frame_1, justify=tkinter.LEFT, text=exception, font=('Roboto', 10, 'normal'), bg='#C2C2C2')
        label_1.pack(pady=12, padx=10)
        button_1 = tkinter.Button(master=frame_1, text="Fechar", command=window.destroy, bg='black', fg='white')
        button_1.pack(pady=12, padx=10)
        window.mainloop()

if __name__ == "__main__":
    main()

