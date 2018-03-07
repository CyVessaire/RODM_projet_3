import numpy as np
import matplotlib.pyplot as plt
from random import *
from time import *

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
  return (m*(m+1)*1.0/2 , m*(m+1)*1.0/2 + m*(t-m) , x*(x+1)/2.0 * t*1.0/x)

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
  print(ew,eb,er)
  return ((integral - ew)*1.0/(eb - ew), integral)

#
# graph = read_file("/home/l/lamothe/3 A/RODM/RODM_projet_3/dataset/Flickr-test")
# print(density(graph))
# print(average_degree(graph))
# print(clustering_coeff(graph))
