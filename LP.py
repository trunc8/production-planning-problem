import numpy as np

import sys 
import pulp as pl

Demand = []
# M = 5
# Demand.append(10)
# Demand.append(20)
# Demand.append(30)

# Demand.append(40)
# Demand.append(70)

# E = 5
# Hcost = 5
# Fcost = 5
# S = 10
# C = 2
# OTC = 1
# OTPrice = 100
# W = 3




M = int(input()) 

for i in range(0, M):  
    Demand.append(int(input()))  
      
print(Demand)
E = int(input())
Hcost = int(input())
Fcost = int(input())
S = int(input())
C = int(input())
OTC = int(input())
OTPrice = int(input())
W = int(input())

tot = 0
for i in range(M):
    tot = tot + Demand[i]

Total_Carpets = pl.LpVariable.dicts("Total_Carpets", range(M),lowBound=0,cat=pl.LpInteger)
Overtime_Carpets = pl.LpVariable.dicts("Overtime_Carpets", range(M),lowBound=0, cat=pl.LpInteger)
Unsold_carpets = pl.LpVariable.dicts("Unsold_carpets", range(M+1),lowBound=0,cat=pl.LpInteger)
Workers = pl.LpVariable.dicts("Workers", range(M+1),lowBound=0,cat=pl.LpInteger)
Hired = pl.LpVariable.dicts("Hired", range(M),lowBound=0,cat=pl.LpInteger)
Fired = pl.LpVariable.dicts("Fired", range(M),lowBound=0,cat=pl.LpInteger)

Unsold_carpets[0] = 0
Workers[0] = E
# Workers[M+1] = E

prob = pl.LpProblem("myProblem", pl.LpMinimize)
for i in range(M):
    prob += Total_Carpets[i] == C*Workers[i+1] + Overtime_Carpets[i]
for i in range(M):
    prob += Unsold_carpets[i+1] == Unsold_carpets[i] + Total_Carpets[i] - Demand[i]
for i in range(M):
    prob += Workers[i+1] == Workers[i] + Hired[i] - Fired[i]
for i in range(M):
    prob += Overtime_Carpets[i] <= OTC*Workers[i+1]    

prob += pl.lpSum(Total_Carpets[j] for j in range(M))>= tot   

x1= pl.lpSum(S*Workers[j+1] for j in range(M))
x2= pl.lpSum(Hcost*Hired[j] for j in range(M))
x3= pl.lpSum(Fcost*Fired[j] for j in range(M))
x4= pl.lpSum(W*Unsold_carpets[j+1] for j in range(M))
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
# for i in range(M):
#     print(pl.value(Unsold_carpets[i+1]))                

print(pl.value(prob.objective))
