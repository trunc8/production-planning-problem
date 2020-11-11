#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	//Taking input
	int months;
	cin >> months;
	int D[months];
	int totalprod = 0; //The total number of carpets needed is written here
	for (int i=0; i<months; i++)
	{
		cin >> D[i];
		totalprod = totalprod + D[i];
	}
	int E,Hcost,Fcost,S,C,OTC,OTPrice,W;
	cin >> E;
	cin >> Hcost;
	cin >> Fcost;
	cin >> S;
	cin >> C;
	cin >> OTC;
	cin >> OTPrice;
	cin >> W;
	//cout<<max(int(totalprod/C)+1,E+1);
	
	//Defining variables and initializing to zero
	int v[months+1][max(totalprod,C)][max(int(totalprod/C)+1,E+1)]; //Each entry v[i][j][k] denotes min cost from months i to end, considering j carpets already produced and k employees already hired
	for (int i=0; i<months+1; i++)
	{
		for (int j=0; j<max(totalprod,C); j++)
		{
			for (int k=0; k<max(int(totalprod/C)+1,E+1); k++)
			{
				v[i][j][k] = 0;
			}			
		}
	}
	
	//Solving the recurrence
	for (int k=months-1; k>=0; k--) //k here represents the month number
	{
		for (int i=0; i<totalprod; i++) //This represents the number of carpets already manufactured and not sold before month k
		{
			for (int e=0; e<max(int(totalprod/C)+1,E+1); e++) //This represents the number of employees already there before month k
			{
				int x = INT_MAX/2;
				for (int h=-e; h<max(int(totalprod/C)+1,E+1)-e; h++) //Represents the number of employees hired or fired at the start of month k
				{
					for (int y=0; y<= OTC*(e+h); y++) //Represents the number of carpets produced in overtime
					{
						int hold_cost = 0; //Represents the hiring firing cost
						if (h<=0)
						{
							hold_cost = -h*Fcost; //If h<0, employees have been fired, each at Fcost
						}
						else
						{
							hold_cost = h*Hcost; //If h>0, employees have been hired, each at Hcost
						}
						int val=0;
						if (i+(e+h)*C+y-D[k]>=max(totalprod,C) || e+h >= max(int(totalprod/C)+1,E+1)) //Cases go beyond table so not feasible. Hence not considered.
							continue;
						else
						{
							val = v[k+1][i+(e+h)*C+y-D[k]][e+h]; //If cases don't go beyond table, value read from table.
						}
						if (i+(e+h)*C+y-D[k]>=0) //If the number of carpets meets demand then only consider
							if (k==(months-1)) //Considering the last month since there would be hiring firing cost to make final employees=E
							{
								int normcost = 0; //Hiring firing cost to make employees = E
								if (e+h>E)
									normcost = Fcost*(e+h-E); //If e+h>E, e+h-E employees need to be fired
								else
									normcost = Hcost*(E-e-h); //If e+h<E, E-e-h employees need to be hired
								//x = min(x,(e+h)*S+hold_cost+W*(i+(e+h)*C+y-D[k])+y*OTPrice+val+normcost);
								x = min(x,(e+h)*S+hold_cost+y*OTPrice+val+normcost); //Recurrence, described in more detail in the report
								//cout<<h<<" "<<y<<" "<<e<<" "<<(e+h)*S+hold_cost+W*(i+(e+h)*C+y-D[k])+y*OTPrice+val+normcost<<endl;
							}
							else
								x = min(x,(e+h)*S+hold_cost+W*(i+(e+h)*C+y-D[k])+y*OTPrice+val); //Recurrence, described in more detail in the report
						
					}
				}
				v[k][i][e] = x; //Updating entry
				//cout<<k<<" "<<i<<" "<<e<<" "<<x<<endl;
			}
		}
	}
	cout << v[0][0][E] << endl;

}
