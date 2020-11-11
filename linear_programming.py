import numpy as np

import sys 
import pulp as pl

Demand = []
# M = 3
# Demand.append(50)
# Demand.append(40)
# Demand.append(70)

# # Demand.append(40)
# # Demand.append(70)

# E = 5
# Hcost = 32
# Fcost = 40
# S = 200
# C = 8
# OTC = 3
# OTPrice = 35
# W = 6




M = int(input()) 
K1=input()
K1 = K1.split()
for i in range(0, M):  
    Demand.append(int(K1[i]))  
      
# print(Demand)
K2 = input()
K2 = K2.split()
E = int(K2[0])
Hcost = int(K2[1])
Fcost = int(K2[2])
K3 = input()
K3 = K3.split()
S = int(K3[0])
C = int(K3[1])
K4 = input()
K4 = K4.split()
OTC = int(K4[0])
OTPrice = int(K4[1])
W = int(input())

tot = 0
for i in range(M):
    tot = tot + Demand[i]

Total_Carpets = pl.LpVariable.dicts("Total_Carpets", range(M),lowBound=0,cat=pl.LpInteger)
Overtime_Carpets = pl.LpVariable.dicts("Overtime_Carpets", range(M),lowBound=0, cat=pl.LpInteger)
Unsold_carpets = pl.LpVariable.dicts("Unsold_carpets", range(M+1),lowBound=0,cat=pl.LpInteger)
Workers = pl.LpVariable.dicts("Workers", range(M+2),lowBound=0,cat=pl.LpInteger)
Hired = pl.LpVariable.dicts("Hired", range(M+1),lowBound=0,cat=pl.LpInteger)
Fired = pl.LpVariable.dicts("Fired", range(M+1),lowBound=0,cat=pl.LpInteger)

Unsold_carpets[0] = 0
Workers[0] = E
Workers[M+1] = E

prob = pl.LpProblem("myProblem", pl.LpMinimize)
for i in range(M):
    prob += Total_Carpets[i] == C*Workers[i+1] + Overtime_Carpets[i]
for i in range(M):
    prob += Unsold_carpets[i+1] == Unsold_carpets[i] + Total_Carpets[i] - Demand[i]
for i in range(M+1):
    prob += Workers[i+1] == Workers[i] + Hired[i] - Fired[i]
for i in range(M):
    prob += Overtime_Carpets[i] <= OTC*Workers[i+1]    

prob += pl.lpSum(Total_Carpets[j] for j in range(M))>= tot   

x1= pl.lpSum(S*Workers[j+1] for j in range(M))
x2= pl.lpSum(Hcost*Hired[j] for j in range(M+1))
x3= pl.lpSum(Fcost*Fired[j] for j in range(M+1))
x4= pl.lpSum(W*Unsold_carpets[j+1] for j in range(M-1))
x5= pl.lpSum(OTPrice*Overtime_Carpets[j] for j in range(M))
prob += x1 + x2 + x3 + x4 + x5 
prob.solve(pl.PULP_CBC_CMD(msg=0))
# print("Workers per month")
# for i in range(M+1):
#     print(pl.value(Workers[i+1])) 
# print("Hired per month")    
# for i in range(M+1):
#     print(pl.value(Hired[i]))
# print("Fired per month") 
# for i in range(M+1):
#     print(pl.value(Fired[i])) 
# print("Total Carpets per month")    
# for i in range(M):
#     print(pl.value(Total_Carpets[i])) 
# print("Overtime")
# for i in range(M):
#     print(pl.value(Overtime_Carpets[i]))
# print("Unsold")    
# for i in range(M-1):
#     print(pl.value(Unsold_carpets[i+1]))                

print(pl.value(prob.objective))
