import numpy as np
import sys 
import pulp as pl
# Taking Inputs
Demand = []
M = int(input()) 
K1=input()
K1 = K1.split()
for i in range(0, M):  
    Demand.append(int(K1[i]))  
      
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
#Caclulating total demand
for i in range(M):
    tot = tot + Demand[i]

#Defining Variables, they are self explanatory by the name. Allvariables are integer
Total_Carpets = pl.LpVariable.dicts("Total_Carpets", range(M),lowBound=0,cat=pl.LpInteger)  #Total carpets made in a month i
Overtime_Carpets = pl.LpVariable.dicts("Overtime_Carpets", range(M),lowBound=0, cat=pl.LpInteger) #Overtime carpets made in a month i
Unsold_carpets = pl.LpVariable.dicts("Unsold_carpets", range(M+1),lowBound=0,cat=pl.LpInteger) #Unsold carptes till month i
Workers = pl.LpVariable.dicts("Workers", range(M+2),lowBound=0,cat=pl.LpInteger) #Total workers working in a month i
Hired = pl.LpVariable.dicts("Hired", range(M+1),lowBound=0,cat=pl.LpInteger) #Total hired workers in a month i
Fired = pl.LpVariable.dicts("Fired", range(M+1),lowBound=0,cat=pl.LpInteger) #Total fired workers in a month i

Unsold_carpets[0] = 0 #Starting number of carpets
Workers[0] = E #Starting number of workers
Workers[M+1] = E #Ensuring that final employees stay equal to initial employees
#Defining the problem as minimiization objetive
prob = pl.LpProblem("myProblem", pl.LpMinimize)
#Defining the constraints
for i in range(M):
    prob += Total_Carpets[i] == C*Workers[i+1] + Overtime_Carpets[i]
for i in range(M):
    prob += Unsold_carpets[i+1] == Unsold_carpets[i] + Total_Carpets[i] - Demand[i]
for i in range(M+1):
    prob += Workers[i+1] == Workers[i] + Hired[i] - Fired[i]
for i in range(M):
    prob += Overtime_Carpets[i] <= OTC*Workers[i+1]    

#To ensure the total demand is satisfied
prob += pl.lpSum(Total_Carpets[j] for j in range(M))>= tot   

#Putting final variables to be minimized in the cost equation
x1= pl.lpSum(S*Workers[j+1] for j in range(M))
x2= pl.lpSum(Hcost*Hired[j] for j in range(M+1))
x3= pl.lpSum(Fcost*Fired[j] for j in range(M+1))
x4= pl.lpSum(W*Unsold_carpets[j+1] for j in range(M-1))
x5= pl.lpSum(OTPrice*Overtime_Carpets[j] for j in range(M))
prob += x1 + x2 + x3 + x4 + x5 
prob.solve(pl.PULP_CBC_CMD(msg=0))
#Comment out the below print statements to know the planning and variable values for each month

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

#print the final cost value which is minimized
print(pl.value(prob.objective))
