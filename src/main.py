from vector_race import VectorRace


def main():
    p = VectorRace("mapa.txt")
    p.parser()
    p.create_graph()
    print(p.graph)
    print(p.search_dfs_race())
    print(p.search_bfs_race())


if __name__ == "__main__":
    main()
