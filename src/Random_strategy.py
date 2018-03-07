import numpy as np
import random
import matplotlib.pyplot as plt
import TP_strategie as TP

# n designe le nombre de noeud du graphe
# Random_strategy renvoie une liste d arete a tester
def Random_strategy(n):
    L = []
    for i in range(n-1):
        for j in range(i+1,n):
            L.append([i,j])

    random.shuffle(L)

    return L

# liste_node est la liste [i,j], on suppose qu elle est de taille 2
# graphe est une liste d adjacence
def test_edge(liste_node, graphe):
    return liste_node[1] in graphe[liste_node[0]]

def evolution(graphe, nb_max_test = None):
    n = len(graphe)
    L = Random_strategy(n)
    if nb_max_test == None:
      nb_max_test = len(L)+2
    PlotList = [[0,0]]
    efficiency_list = []
    test_count = 0
    count = 0
    while(len(L)>0 and test_count<nb_max_test):
        liste_node = L.pop()
        test_count += 1
        if (test_edge(liste_node, graphe)):
            PlotList.append([test_count, count])
            count += 1
            PlotList.append([test_count, count])
            efficiency_list.append([test_count, liste_node[0], liste_node[1]])

    #plt.scatter(*zip(*PlotList))
    #plt.show()
    m = sum([len(a) for a in graphe])/2
    #print(TP.efficiency_strat(efficiency_list,len(graphe), m))
    return efficiency_list

if __name__ == "__main__":
  graph = TP.read_file("/home/cyrille/Documents/RODM_projet/RODM_projet_3/dataset/Flickr-test")
  print(TP.density(graph))
  print(TP.average_degree(graph))
  print(TP.clustering_coeff(graph))

  evolution(graph)
