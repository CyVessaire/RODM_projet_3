import numpy as np
import matplotlib.pyplot as plt
from random import *
from time import *
import Random_strategy as rs

def read_file(string):
  graph = []
  node_max = 0
  with open(string, "r") as f:
    list_edges = []
    for line in f:
      edge = line.split(" ")
      edge = [int(a) for a in edge]
      list_edges.append((edge[0], edge[1]))
      node_max = max(node_max,edge[0],edge[1])
    for i in range(node_max+1):
      graph.append([])
    for u,v in list_edges:
      graph[u].append(v)
      graph[v].append(u)
  return graph


def density(graph):
  n = len(graph)
  nb_arete = sum([len(a) for a in graph])/2
  nb_max = (n**2-n)*1.0/2
  return nb_arete*1.0/nb_max


def average_degree(graph):
  return sum([len(a) for a in graph])*1.0/len(graph)

def clustering_coeff(graph):
  proba = 0
  for i in range(len(graph)):
    nb_found = 0
    nb_tot = 0
    for j in range(len(graph[i])):
      for k in range(j):
        nb_tot +=1
        nb_found += (k in graph[j])
    if nb_tot > 0:
      proba+= nb_found*1.0/nb_tot
  return proba*1.0/len(graph)


def efficiency_worst_best_ran(n,m,t):
  x = t*m*2.0/(n*(n-1))
  if t<m:
    return (t*(t+1)*1.0/2 , t*(t+1)*1.0/2 , x*(x+1)/2.0 * t*1.0/x)
  elif t<(n**2-n)/2-m:
    return (0 , m*(m+1)*1.0/2 + m*(t-m) , x*(x+1)/2.0 * t*1.0/x)
  y = t-(n**2-n)/2+m
  return (y*(y+1)*1.0/2 , m*(m+1)*1.0/2 + m*(t-m) , x*(x+1)/2.0 * t*1.0/x)

def efficiency_strat(file_res, n, m):
  nb_found = 0
  integral = 0
  old_t = 0
  for t,n1,n2 in file_res:
    integral += nb_found * (t - old_t)
    nb_found += 1
    old_t = t
  integral += nb_found
  ew,eb,er = efficiency_worst_best_ran(n,m,old_t)
  return ((integral - ew)*1.0/(eb - ew), integral)

def order_nodes(list_nodes, gaph):
  list_nodes.sort(key = lambda x : len(graph[x]))
  list_nodes.reverse()

def strat_complete(graph,k,nb_max_test):
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
  list_nodes = [i for i in range(n)]
  done_node = [0]*n
  while nb_test<nb_max_test:
    order_nodes(list_nodes,found_graph)
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

def plot_efficiency_curve(file_res):
  times = [a[0] for a in file_res]
  plt.plot(times, [i for i in range(len(times))])
  #plt.show()


def compare_strat(graph,t):
  n = len(graph)
  m = sum([len(a) for a in graph])/2
  fr_random = rs.evolution(graph,t)
  fr_complete = strat_complete(graph,1000,t)
  print(efficiency_strat(fr_random, n, m))
  print(efficiency_strat(fr_complete, n, m))
  plot_efficiency_curve(fr_random)
  plot_efficiency_curve(fr_complete)
  plt.show()
        
        

if __name__ == "__main__":

  graph = read_file("../dataset/Flickr-test")
  #print(density(graph))
  #print(average_degree(graph))
  #print(clustering_coeff(graph))
  #list_nodes = [i for i in range(len(graph))]
  #order_nodes(list_nodes, graph)
  #print(list_nodes)
  #print([len(graph[x]) for x in list_nodes])

  #file_res = strat_complete(graph,1000,5000)
  #plot_efficiency_curve(file_res)
  compare_strat(graph,5000)











    
  

