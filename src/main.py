from vector_race import VectorRace
from graph import Graph


def main():

    p = VectorRace("mapa1.txt")
    p.parser()
    p.create_graph()
    #print(p.graph)
    #print(p.search_dfs_race())
    print(p.search_greedy())


if __name__ == "__main__":
    main()


"""
Estado 
l = (l,c)

Acel = {-1,0,1}
a = (al, ac)  -> (-1,-1) ; (-1,0) ; (-1,1) ;
                 (0,-1) ; (0,0) ; (0,1) ;
                 (1,-1) ; (1,0) ; (1,1)  

pj = (pl, pc)

pj+1 = pj + vj + aj

vj+1 = vj + aj
 
 pi       a        pf
(0,0) ->  (0,1) -> (0,2)
vj = (0,0)
vj+1 = (0,1)




"""