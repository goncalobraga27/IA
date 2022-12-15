from tkinter import *
from tkinter import messagebox
from vector_race import VectorRace
class ui:
    def __init__(self):
        self.titule = "Interface gráfica para o programa"
    def interface(self):
        janelaInitial = Tk()
        janelaInitial.geometry("600x600")
        janelaInitial.title("VECTOR RACE")
        Label(janelaInitial, text="VECTOR RACE", font=('calibre', 15, 'bold'), anchor=W).place(x=190, y=200, width=500)
        Label(janelaInitial, text="Insira ficheiro com o circuito do jogo: ", background="#dde",
              foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=150, y=300, width=250)
        vMapa = Entry(janelaInitial)
        vMapa.place(x=150, y=320, width=250, height=20)
        Button(janelaInitial, text="Procurar", command=lambda: ui.dealWithMap(self, vMapa)).place(x=220, y=370)
        janelaInitial.mainloop()

    def dealWithMap(self, vMapa):
        nomeFile = vMapa.get()
        try:
            vector_race = VectorRace.parser(nomeFile)
            vector_race.show_parser(nomeFile)

            messagebox.showinfo("Resultado", "Circuito configurado")
            janelaNumberPlayers = Tk()
            janelaNumberPlayers.geometry("600x600")
            janelaNumberPlayers.title("VECTOR RACE")
            Label(janelaNumberPlayers, text="Introduza o número de jogadores (max 4): ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=150, y=300, width=300)
            eNumberPlayers = Entry(janelaNumberPlayers)
            eNumberPlayers.place(x=150, y=320, width=250, height=20)
            Button(janelaNumberPlayers, text="Confirmar",
                   command=lambda: ui.dealWithNumberPlayers(self,eNumberPlayers, vector_race)).place(x=220, y=370)
            janelaNumberPlayers.mainloop()
        except:
            messagebox.showinfo("Resultado", "Circuito inválido")

    def dealWithNumberPlayers(self, eNumberPlayers, vector_race):
        option_players = eNumberPlayers.get()
        if option_players == "1":
            numberPlayers = 1
        elif option_players == "2":
            numberPlayers = 2
        elif option_players == "3":
            numberPlayers = 3
        elif option_players == "4":
            numberPlayers = 4
        else:
            numberPlayers = 20  # É de propósito para dar erro
        if 1 < numberPlayers and numberPlayers > 4:
            messagebox.showinfo("Erro", "Valor Inválido")

        if numberPlayers == 1:
            vector_race.create_graph()
            janelaOnePlayer = Tk()
            janelaOnePlayer.geometry("600x600")
            janelaOnePlayer.title("VECTOR RACE")
            Label(janelaOnePlayer, text="1-Imprimir Circuito ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=50, width=300)
            Label(janelaOnePlayer, text="2-Desenhar Circuito ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=100, width=300)
            Label(janelaOnePlayer, text="3-Imprimir Grafo ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=150, width=300)
            Label(janelaOnePlayer, text="4-Desenhar Grafo ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=200, width=300)
            Label(janelaOnePlayer, text="5-Imprimir Nodos do Grafo ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=250, width=300)
            Label(janelaOnePlayer, text="6-Imprimir Arestas do Grafo ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=300, width=300)
            Label(janelaOnePlayer, text="7-BFS ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=350, width=300)
            Label(janelaOnePlayer, text="8-DFS ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=400, width=300)
            Label(janelaOnePlayer, text="9-Pesquisa Gulosa ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=450, width=300)
            Label(janelaOnePlayer, text="10-Pesquisa A* ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=500, width=300)
            Label(janelaOnePlayer, text="0-Sair ", background="#dde",
                  foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=100, y=550, width=300)
            optionGame = Entry(janelaOnePlayer)
            optionGame.place(x=450, y=300, width=100, height=20)
            Button(janelaOnePlayer, text="Confirmar",
                   command=lambda: ui.dealWithOptionChoose(self, optionGame, vector_race)).place(x=450, y=350)
            janelaOnePlayer.mainloop()

    def dealWithOptionChoose(self, optionGame, vector_race):
        option_players = optionGame.get()
        match option_players:
            case "1":
                janelaFstOpt = Tk()
                janelaFstOpt.title("VECTOR RACE")
                janelaFstOpt.geometry("600x600")
                Label(janelaFstOpt, text=vector_race.print_map(), background="#dde",
                      foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=200, y=100, width=250)
                janelaFstOpt.mainloop()
            case "2":
                janelaSndOpt = Tk()
                janelaSndOpt.title("VECTOR RACE")
                janelaSndOpt.geometry("600x600")
                Label(janelaSndOpt, text=vector_race.draw_circuit(vector_race.start), background="#dde",
                      foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=200, y=100, width=250)
                janelaSndOpt.mainloop()

            case "3":
                janelaTrdOpt = Tk()
                janelaTrdOpt.title("VECTOR RACE")
                janelaTrdOpt.geometry("600x600")
                Label(janelaTrdOpt, text=vector_race.graph, background="#dde",
                      foreground="#009", anchor=W, font=('calibre', 10, 'normal')).place(x=200, y=100, width=250)
                janelaTrdOpt.mainloop()
            case "4":
                vector_race.graph.graph_draw()
            case "5":
                print(vector_race.graph.show_nodes())
            case "6":
                print(vector_race.graph.show_edges())
            case "7":
                path, cost = vector_race.search_bfs_race()
                print(path, end=", Cost=")
                print(cost, end="\n\n")
                print(vector_race.print_map(path))
                vector_race.draw_circuit_path(path)
            case "8":

                path, cost = vector_race.search_dfs_race()
                print(path, end=", Cost=")
                print(cost, end="\n\n")
                print(vector_race.print_map(path))
                vector_race.draw_circuit_path(path)
            case "9":
                #chose_heuristic(vector_race)

                path, cost = vector_race.search_greedy()
                print(path, end=", Cost=")
                print(cost, end="\n\n")
                print(vector_race.print_map(path))
                vector_race.draw_circuit_path(path)
            case "10":
                #chose_heuristic(vector_race)
                path, cost = vector_race.search_star_a()
                print(path, end=", Cost=")
                print(cost, end="\n\n")
                print(vector_race.print_map(path))
                vector_race.draw_circuit_path(path)
            case "0":
                option = 0
