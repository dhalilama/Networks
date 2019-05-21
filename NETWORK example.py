#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 23:15:42 2019

@author: ajay
"""

N=[[0,1,0],[1,0,1],[0,1,0]]
# here is a network with nodes 0, 1, 2, such that node 1 is connected to node 0 and 2:
import numpy as np
import matplotlib.pyplot as plt 
def network_plot_circle(N):
    n=len(N)
    x=[np.cos(2*np.pi*i/n) for i in range(n)]
    y=[np.sin(2*np.pi*i/n) for i in range(n)]
    for i in range(n):
        for j in range(i):
               if N[i][j]==1:
                    plt.plot([x[i],x[j]],[y[i],y[j]],'b')
    plt.plot(x,y,'ro')
    plt.show()
    
network_plot_circle(N)

karate = open("karate_edgeList.txt").read()
pairs = [s.split('\t') for s in karate.splitlines()]
pairs = [[int(i) for i in j]for j in pairs]
n = max(max(j for j in pairs))
adjMatrix = [[0]*n for _ in range(n)]
for p in pairs:
    adjMatrix[p[0]-1][p[1]-1]=1
    adjMatrix[p[1]-1][p[0]-1]=1

network_plot_circle(adjMatrix)