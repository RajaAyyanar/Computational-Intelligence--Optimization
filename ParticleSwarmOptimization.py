# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 22:28:10 2017

@author: Raja Ayyanar
"""

import numpy as np
from random import randint
from random import random

PopulationSize=20;
Dimensions = 2;
Xmin = -5.2;
Xmax = 5.2;
Vmin = -5.1;
Vmax = 5.1;
c1= 2;
c2= 2;
w = 0.5;
MaxIterations = 200;

Positions_X= Xmin + (Xmax-Xmin)*np.random.uniform(0,1,(PopulationSize,Dimensions));
Velocities_V= Vmin + (Vmax-Vmin)*np.random.uniform(0,1,(PopulationSize,Dimensions));

PBestFitnesses=np.zeros(PopulationSize);
PBestPositions = Positions_X;
for Particle in range(0,PopulationSize):
    PBestFitnesses[Particle]= sum(Positions_X[Particle,:]**2);

GBestFitness=min(PBestFitnesses)
GBestIndex=np.argmin(PBestFitnesses)
GBestPosition= PBestPositions[GBestIndex,:]
BestFitness=np.zeros(MaxIterations)
for Iteration in range(0,MaxIterations):
    w=0.9-0.8* Iteration/MaxIterations;
    for Particle in range(0,PopulationSize):
        Inertia = w*Velocities_V[Particle,:];
        CogAcc= -c1* random()*(Positions_X[Particle,:]+ PBestPositions[Particle,:])
        SoAcc= -c2* random()* (Positions_X[Particle,:]+ GBestPosition)
        Velocities_V[Particle,:]= Inertia + CogAcc + SoAcc
        CurrentParticleVelocity= Velocities_V[Particle,:]
    
        CurrentParticleVelocity[CurrentParticleVelocity > Vmax]= Vmax
        CurrentParticleVelocity[CurrentParticleVelocity < Vmin]= Vmin
        Velocities_V[Particle,:]= CurrentParticleVelocity

        CurrentPosition= Positions_X[Particle,:]
        NewPosition= CurrentPosition + Velocities_V[Particle,:]
        NewPosition[NewPosition>Xmax] = Xmax
        NewPosition[NewPosition<Xmin] =Xmin
        Positions_X[Particle,:]=NewPosition;

        Newfitness = sum(NewPosition**2)
        if Newfitness < PBestFitnesses[Particle]:
            PBestFitnesses[Particle]=Newfitness;
            PBestPositions[Particle,:]=NewPosition;
        if Newfitness < GBestFitness:
            GBestFitness = Newfitness;
            GBestPosition = NewPosition;
            
    print('\n Iteration: ',Iteration, 'BestFitness: ',GBestFitness)
    BestFitness[Iteration]=GBestFitness;

print(GBestPosition)

        