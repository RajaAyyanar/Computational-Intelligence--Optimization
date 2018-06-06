# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 00:47:06 2017

@author: Raja Ayyanar
"""
import numpy as np
from random import random
from random import randint


no_of_chromosomes = 40;
dimensions = 2;

bits = 16;
max_weight = +8;
min_weight = -8;

max_generations = 150;

cr_probability = 0.9;
mut_probability = 0.2;

chromosome=np.zeros((no_of_chromosomes,dimensions,bits))
weights=np.zeros((no_of_chromosomes,dimensions))
for i in range(0,no_of_chromosomes):
    for j in range(0,dimensions):
        weights[i,j]=0;
        for k in range(0,bits):
            if random()<0.5:
                chromosome[i,j,k]=1
            else:
                chromosome[i,j,k]=0
            weights[i,j]=weights[i,j]+chromosome[i,j,k]*(2**(k-1));

weights = ((weights/(2**bits))*(max_weight-min_weight))-max_weight ;  
generation=0;
mse=np.zeros(max_generations)

while generation < max_generations:
    generation = generation +1
    
    no_offsprings=1;
    for i in range(0,no_of_chromosomes):
        cross_si=random()
        if cross_si> cr_probability:
            no_offsprings = no_offsprings +1
            a=i;
            b=np.floor(random()*no_of_chromosomes)
            while b==a:
                b=np.floor(random()*no_of_chromosomes)
        
        #print('chromosome ',i,' will have offdpring from', b)
        
        
            mask= np.array([1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1])
        
            offspring=np.zeros((no_offsprings,dimensions,bits));
            for j in range(0,bits):
                for k in range(0,dimensions):
                    if mask[j]==1:
                        offspring[no_offsprings-1,k,j]= chromosome[b,k,j];
                    else:
                        offspring[no_offsprings-1,k,j]=chromosome[i,k,j];
                    mutation_si=random()
                    if mutation_si< mut_probability:
                        offspring[no_offsprings-1,k,j]= abs(offspring[no_offsprings-1,k,j]-1)
        
        
    
    next_gen =np.concatenate( (chromosome , offspring) );
    next_gen_population = no_of_chromosomes + no_offsprings;  
    
    weights=np.zeros((next_gen_population,dimensions))
    for i in range(0,next_gen_population):
        for j in range(0,dimensions):
            weights[i,j]=0;
            for k in range(0,bits):
                    weights[i,j]=weights[i,j]+next_gen[i,j,k]*(2**(k-1))
    
    weights=((weights/(2**bits))*(max_weight-min_weight))-max_weight ; 
    
    mean_square_error= np.zeros((next_gen_population,2))
    for i in range(0,next_gen_population):
        current_weights= weights[i,:]
        f0=0;
        for k in range(0,dimensions):
            f0=f0+current_weights[k]**2;
        mean_square_error[i,0]=f0
        mean_square_error[i,1]=i
    
    
    
    for i in range(0,next_gen_population):
        for j in range(0,next_gen_population-i-1):
            if mean_square_error[j,0]>mean_square_error[j+1,0]:
                temp=mean_square_error[j,0]
                mean_square_error[j,0]=mean_square_error[j+1,0]
                mean_square_error[j+1,0]=temp
    
                temp2=mean_square_error[j,1]
                mean_square_error[j,1]=mean_square_error[j+1,1]
                mean_square_error[j+1,1]=temp2
        
    
    for i in range(0,no_of_chromosomes):
        chromosome[i,:,:]= next_gen[mean_square_error[i,1],:,:]

    mse[generation-1]= mean_square_error[0,0];
    print('Trial: ','Generation: ',generation,'Fitness: ',mse[generation-1])

"""      
fit=mse[generation-1];
mean_fitness=sum(fit)

print(mean_fitness)


"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
