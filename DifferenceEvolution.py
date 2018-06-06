# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 18:09:40 2017

@author: Raja Ayyanar
"""
import numpy as np
from random import randint
from random import random

dimension=2;
gen=0;
mini=-6;
maxi=6;
totalparent=20;
totalgen=100;
scale=0.5;
pr=0.5;
bestfit=1000;
parent=np.zeros((totalparent,dimension))
for p in range(0,totalparent):
    for q in range(0,dimension):
        parent[p,q]=mini+ randint(mini,maxi)
#print(parent)
for gen in range(0,totalgen):
    newparent=parent;
    for i in range(0,totalparent):
        x1=randint(0,totalparent);
        while(x1==i):
            x1=randint(0,totalparent);
        
        x2=randint(0,totalparent);
        while(x2==i or x2==x1):
            x2=randint(0,totalparent);

        x3=randint(0,totalparent);
        while(x2==i or x3==x2 or x3==x1):
            x3=randint(0,totalparent);

        trial= parent[(x1-1),:] + scale*(parent[(x3-1),:]-parent[(x2-1),:])
        
        child=np.zeros(dimension);
        for k in range(0,dimension):
            rand=random();
            if  (rand>pr):
                child[k]=parent[i,k];
            else:
                child[k]=trial[k];

        singleparent= parent[i,:]
        childfit= sum(child*child)
        parentfit= sum(singleparent*singleparent);
        if (childfit<parentfit):
            parent[i,:]=child;
            
            if(childfit<bestfit):
                bestfit=childfit;
        if(parentfit<bestfit):
            bestfit=parentfit;
    print('\n generation- ', gen ,' bestfit- ',bestfit)

print(bestfit)
            
    
                






















