from __future__ import division
import matplotlib.pyplot as plt
from random import *
import networkx as nx
import random
#import sys
#List a

G = nx.barabasi_albert_graph(1500 , 6)
nonInfected=[]
Infected=[]
cured=[]
childCured=[]
adjDict=nx.to_dict_of_lists(G)
prob=.005  #40%
prob1 = 0.006
# for i in range(1,len(set(G.nodes))+1):
#     nonInfected.append(i)
nonInfected = list(G.nodes())


startNode= nonInfected[0]
centeralnode = nx.center(G)
nonInfected.remove(startNode)
childInfected=[]
Infected.append(startNode)
step = 0
stepcount=[]
lenHealthy=[]
lenCured=[]
lenInfected=[]
cured.append(startNode)


def propagation():
    for i in Infected:
        if i not in childInfected:
            childInfected.append(i)
    for k in childInfected:
        child=(list(G.neighbors(k)))
        for i in child:
            if (random.uniform(0, 1)< prob) and (i in nonInfected):
                Infected.append(i)
                nonInfected.remove(i)
    # stepcount.append(step)
    lenInfected.append(len(Infected))
    lenHealthy.append(len(nonInfected))

def cure():
    for i in cured:
        if i not in childCured:
            childCured.append(i)
    for k in childCured:
        child=(list(G.neighbors(k)))
        for i in child:
            if (random.uniform(0, 1)< prob1) and (i in Infected):
                cured.append(i)
                Infected.remove(i)
    stepcount.append(step)
    lenCured.append(len(cured))

while(len(nonInfected)!=0):
    step += 1
    print("Initial state:{}".format(nonInfected))
    propagation()
    print("Noninfected -1 :{}".format(nonInfected))
    print("Infected:- 1{}".format(Infected))
    cure()
    print("Cured -2 :{}".format(cured))
    print("Infected - 2:{}".format(Infected))

print("Steps: {}".format(step))
print(stepcount,lenHealthy)
plt.subplot(311)
plt.plot(stepcount,lenCured)
plt.ylabel('Number of cured nodes')
plt.title('Cure of barabasi_albert_ with 1500 nodes / 9000 edges')
plt.subplot(312)
plt.plot(stepcount,lenHealthy)
plt.ylabel('Number of healthy nodes')
plt.subplot(313)
plt.plot(stepcount,lenInfected)
plt.xlabel('Number of Steps')
plt.ylabel('Number of Infected')
# plt.title('Cure of Watts Strogatz with 500 nodes / 1000 edges')
plt.grid(True)
print(nx.info(G))


plt.show()
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
