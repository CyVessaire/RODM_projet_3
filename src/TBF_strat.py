import numpy as np
from random import *
import matplotlib.pyplot as plt
import TP_strategie as TP

def order_link(simul_graph):
    L = []
    n = len(simul_graph)
    for i in range(n-1):
        for j in simul_graph[i]:
            if j>i:
                count = 0
                count += len(simul_graph[i])
                count += len(simul_graph[j])
                L.append([[i,j], count])

    L.sort(key=lambda x: x[1])
    return L

def triangle_strat(graph,k,nb_max_test):
    list_discover = []
    n = len(graph)
    tested = np.zeros((n,n))
    found_graph = []
    for i in range(n):
        found_graph.append([])
    for i in range(k):
        u,v = randint(0,n-1),randint(0,n-1)
        while tested[u,v]:
            u,v = randint(0,n-1),randint(0,n-1)
        tested[u,v] = 1
        tested[v,u] = 1
        if u in graph[v]:
            list_discover.append((i,u,v))
            found_graph[u].append(v)
            found_graph[v].append(u)
    nb_test = k

    L = order_link(found_graph)
    print(len(L))

    while (len(L)>0 and nb_test < nb_max_test):
        edge = L.pop()[0]
        node_1 = edge[0]
        node_2 = edge[1]
        test = False

        for i in found_graph[node_1]:
            if not tested[node_2,i]:
                tested[node_2,i] = True
                nb_test += 1
                if i in graph[node_2]:
                    list_discover.append((nb_test,node_2,i))
                    found_graph[node_2].append(i)
                    found_graph[i].append(node_2)
                    test = True

                if nb_test >= nb_max_test:
                    break

        for i in found_graph[node_2]:
            if not tested[node_1,i]:
                tested[node_1,i] = True
                nb_test += 1
                if i in graph[node_1]:
                    list_discover.append((nb_test,node_1,i))
                    found_graph[node_1].append(i)
                    found_graph[i].append(node_1)
                    test = True

                if nb_test >= nb_max_test:
                    break

        if test:
            L = order_link(found_graph)

    return list_discover

def triangle_complete_strat(graph,k,nb_max_test):
    list_discover = []
    n = len(graph)
    tested = np.zeros((n,n))
    found_graph = []
    for i in range(n):
        found_graph.append([])
    for i in range(k):
        u,v = randint(0,n-1),randint(0,n-1)
        while tested[u,v]:
            u,v = randint(0,n-1),randint(0,n-1)
        tested[u,v] = 1
        tested[v,u] = 1
        if u in graph[v]:
            list_discover.append((i,u,v))
            found_graph[u].append(v)
            found_graph[v].append(u)
    nb_test = k

    L = order_link(found_graph)
    print(len(L))

    while (len(L)>0 and nb_test < nb_max_test):
        edge = L.pop()[0]
        node_1 = edge[0]
        node_2 = edge[1]
        test = False

        for i in found_graph[node_1]:
            if not tested[node_2,i]:
                tested[node_2,i] = True
                nb_test += 1
                if i in graph[node_2]:
                    list_discover.append((nb_test,node_2,i))
                    found_graph[node_2].append(i)
                    found_graph[i].append(node_2)
                    test = True

                if nb_test >= nb_max_test:
                    break

        for i in found_graph[node_2]:
            if not tested[node_1,i]:
                tested[node_1,i] = True
                nb_test += 1
                if i in graph[node_1]:
                    list_discover.append((nb_test,node_1,i))
                    found_graph[node_1].append(i)
                    found_graph[i].append(node_1)
                    test = True

                if nb_test >= nb_max_test:
                    break

        if test:
            L = order_link(found_graph)

    if nb_test < nb_max_test:
        list_nodes = [i for i in range(n)]
        done_node = [0]*n
        while nb_test < nb_max_test:
            TP.order_nodes(list_nodes, found_graph)
            i = 0
            while done_node[list_nodes[i]]:
                i+=1
            node = list_nodes[i]
            done_node[node] = 1
            order = [i for i in range(n)]
            shuffle(order)
            for i in order:
                if not tested[node,i]:
                    tested[node,i] = 1
                    tested[i,node] = 1
                    nb_test += 1
                    if i in graph[node]:
                        list_discover.append((nb_test,node,i))
                        found_graph[node].append(i)
                        found_graph[i].append(node)

    return list_discover

def order_pair(simul_graph, tested):
    L = []
    n = len(simul_graph)
    for i in range(n-1):
        counti = 0
        counti = len(simul_graph[i])
        if counti > 0:
            for j in range(n):
                if j>i and not(tested[i,j]):
                    countj = 0
                    countj = len(simul_graph[j])
                    if countj > 0:
                        L.append([[i,j], counti + countj])

    L.sort(key=lambda x: x[1])
    return L

def tbf_strat(graph,k,nb_max_test):
    list_discover = []
    n = len(graph)
    tested = np.zeros((n,n))
    found_graph = []
    for i in range(n):
        found_graph.append([])
    for i in range(k):
        u,v = randint(0,n-1),randint(0,n-1)
        while tested[u,v]:
            u,v = randint(0,n-1),randint(0,n-1)
        tested[u,v] = 1
        tested[v,u] = 1
        if u in graph[v]:
            list_discover.append((i,u,v))
            found_graph[u].append(v)
            found_graph[v].append(u)
    nb_test = k

    L = order_pair(found_graph, tested)

    while (len(L)>0 and nb_test < nb_max_test):
        edge = L.pop()[0]
        node_1 = edge[0]
        node_2 = edge[1]
        test = False
        nb_test += 1
        tested[node_1, node_2] = True
        tested[node_2, node_1] = True

        if node_2 in graph[node_1]:
            list_discover.append((nb_test,node_2,node_1))
            found_graph[node_2].append(node_1)
            found_graph[node_1].append(node_2)
            test = True

        if test:
            L = order_pair(found_graph, tested)

    return list_discover

def tbf_complete_strat(graph,k,nb_max_test):
    list_discover = []
    n = len(graph)
    tested = np.zeros((n,n))
    found_graph = []
    for i in range(n):
        found_graph.append([])
    for i in range(k):
        u,v = randint(0,n-1),randint(0,n-1)
        while tested[u,v]:
            u,v = randint(0,n-1),randint(0,n-1)
        tested[u,v] = 1
        tested[v,u] = 1
        if u in graph[v]:
            list_discover.append((i,u,v))
            found_graph[u].append(v)
            found_graph[v].append(u)
    nb_test = k

    L = order_pair(found_graph, tested)

    while (len(L)>0 and nb_test < nb_max_test):
        edge = L.pop()[0]
        node_1 = edge[0]
        node_2 = edge[1]
        test = False
        nb_test += 1
        tested[node_1, node_2] = True
        tested[node_2, node_1] = True

        if node_2 in graph[node_1]:
            list_discover.append((nb_test,node_2,node_1))
            found_graph[node_2].append(node_1)
            found_graph[node_1].append(node_2)
            test = True

        if test:
            L = order_pair(found_graph, tested)

    if nb_test < nb_max_test:
        list_nodes = [i for i in range(n)]
        done_node = [0]*n
        while nb_test < nb_max_test:
            TP.order_nodes(list_nodes, found_graph)
            i = 0
            while done_node[list_nodes[i]]:
                i+=1
            node = list_nodes[i]
            done_node[node] = 1
            order = [i for i in range(n)]
            shuffle(order)
            for i in order:
                if not tested[node,i]:
                    tested[node,i] = 1
                    tested[i,node] = 1
                    nb_test += 1
                    if i in graph[node]:
                        list_discover.append((nb_test,node,i))
                        found_graph[node].append(i)
                        found_graph[i].append(node)

    return list_discover
