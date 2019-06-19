from __future__ import division
import matplotlib.pyplot as plt
from random import *
import networkx as nx
import random
#import sys
#List a

G = nx.erdos_renyi_graph(500 ,0.1)
nonInfected=[]
Infected=[]
adjDict=nx.to_dict_of_lists(G)
prob=.005  #40%
# for i in range(1,len(set(G.nodes))+1):
#     nonInfected.append(i)
nonInfected = list(G.nodes())


startNode= nonInfected[0]
nonInfected.remove(startNode)
childInfected=[]
Infected.append(startNode)
step = 0
stepcount=[]
lenHealthy=[]
while(len(nonInfected)!=0):
    step += 1
    #  pdb.set_trace()
    print("Initial state:{}".format(nonInfected))
    for i in Infected:
      if i not in childInfected:
        childInfected.append(i)
    for k in childInfected:
        child=(list(G.neighbors(k)))
        for i in child:
           if (random.uniform(0, 1)< prob) and (i in nonInfected):
                Infected.append(i)
                nonInfected.remove(i)
    stepcount.append(step)
    lenHealthy.append(len(nonInfected))
            # nonInfected = [x for x in nonInfected if x not in Infected]

    print("Noninfected:{}".format(nonInfected))
    print("Infected:{}".format(Infected))
print("Steps: {}".format(step))
print(stepcount,lenHealthy)

plt.plot(stepcount,lenHealthy)
# plt.show()
plt.savefig("test.png")
#print("Noninfected:{}".format(len(nonInfected)))
#print("Infected:{}".format(len(Infected)))
#k = (G['1'])
#for node in k
#if nodea
#k.nodes[1]['color'] = 'red'

#n = {G['k.nodes[1]']}

#for s,k in n.items():
#if n.nodes['s'].data() == 'blue':
# k.nodes['s']['color'] = 'red'

# if n.nodes('s') == 'N':
# nx.relable_nodes(k['s'],"R")
#print (nx.info(G))
#noOfChildren=len(child)
#getInfected=int(prob*noOfChildren)
#random.shuffle(child)
#y=child[0:getInfected-1]
