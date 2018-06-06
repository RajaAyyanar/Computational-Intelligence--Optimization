# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 12:46:23 2017

@author: Raja Ayyanar
"""
def Sphere(Colony):
    S=Colony*Colony;
    ObjVal=sum(S);
    return ObjVal
    
def calculateFitness(fObjV):
    import numpy as np
    fFitness=np.zeros(np.max(np.shape(fObjV)));
    ind=np.nonzero(fObjV>=0);
    fFitness[ind]=1/(fObjV[ind]+1);
    ind=np.nonzero(fObjV<0);
    fFitness[ind]=1+abs(fObjV[ind]);
    return fFitness
    

    



import numpy as np
import time
import random as random


# Control Parameters of ABC algorithm
population=30; #The number of colony size (employed bees+onlooker bees)
FoodNumber=population/2; #The number of food sources equals the half of the colony size
limit=100; # A food source which could not be improved through "limit" trials is abandoned by its employed bee
max_iterations=200; #The number of cycles for foraging


d=2; #The number of parameters of the problem to be optimized
ub=np.ones((1,d))*5.12; #lower bounds of the parameters. 
lb=np.ones((1,d))*(-5.12);#upper bound of the parameters.

runtime=10;#No of runs in order to see its robustness 
Global_gbest=np.zeros((1,runtime));

for r in range(0,runtime):
    
# All food sources are initialized 
# Variables are initialized in the range [lb,ub]
    
    Range=np.tile((ub-lb), (round(FoodNumber), 1))
    Lower=np.tile(lb, (round(FoodNumber), 1))
    Foods=np.random.uniform(0,1,(round(FoodNumber),d))*Range + Lower;
# Foods is the population of food sources. 
# Each row of Foods matrix is a vector holding d parameters to be optimized.
# The number of rows of Foods matrix equals to the FoodNumber

    Fun_Cost = Sphere(Foods); # Result from the function
    Fitness=calculateFitness(Fun_Cost); # Fitness of cost 
    
    # reset trial counters
    # trial vector holds trial numbers through which solutions can not be improved
    trial=np.zeros((1,FoodNumber));
    
    #The best food source is memorized
    BestInd=np.nonzero(Fun_Cost==Fun_Cost.min());
    BestInd=BestInd[-1];
    gbest=Fun_Cost[BestInd]; # Optimal solution
    gbest_Params=Foods[BestInd,:]; # Parameters of Optimal Solution
    iter=1;

    start=time.time()
    while iter<=max_iterations:
######### EMPLOYED BEE PHASE ########################        
        for i in range(0,FoodNumber):
            #The parameter to be changed is determined randomly
            k=np.floor(random.random()*d);
            
            # A randomly chosen solution is used in producing a mutant solution of the solution i
            j=np.floor(random.random()*(FoodNumber));
           
            #Randomly selected solution must be different from the solution i       
            while(j==i):
                j=np.floor(random.random()*(FoodNumber));
                
            # Generate a new solution
            new_sol=Foods[i,:]; 
           #  v_{ij}=x_{ij}+\phi_{ij}*(x_{kj}-x_{ij}) 
            new_sol[k]=Foods[i,k]+(Foods[i,k]-Foods[j,k])*(random.random()-0.5)*2;
            
           #  if generated parameter value is out of boundaries, it is shifted onto the boundaries
            ind=np.nonzero(new_sol<lb);
            new_sol[ind]=lb[ind];
            ind=np.nonzero(new_sol>ub);
            new_sol[ind]=ub[ind];
            
            #evaluate new solution
            Sol_cost = Sphere(new_sol);
            # Fitness value of new solution
            FitnessSol=calculateFitness(Sol_cost);
            







