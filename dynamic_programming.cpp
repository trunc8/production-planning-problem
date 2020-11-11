#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	//Taking input
	int months;
	cin >> months;
	int D[months];
	int totalprod = 0;
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
	int v[months+1][max(totalprod,C)][max(int(totalprod/C)+1,E+1)];
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
	for (int k=months-1; k>=0; k--)
	{
		for (int i=0; i<totalprod; i++)
		{
			for (int e=0; e<max(int(totalprod/C)+1,E+1); e++)
			{
				int x = INT_MAX/2;
				for (int h=-e; h<max(int(totalprod/C)+1,E+1)-e; h++)
				{
					for (int y=0; y<= OTC*(e+h); y++)
					{
						int hold_cost = 0;
						if (h<=0)
						{
							hold_cost = -h*Fcost;
						}
						else
						{
							hold_cost = h*Hcost;
						}
						int val=0;
						if (i+(e+h)*C+y-D[k]>=max(totalprod,C) || e+h >= max(int(totalprod/C)+1,E+1))
							val = INT_MAX/2;
						else
						{
							val = v[k+1][i+(e+h)*C+y-D[k]][e+h];
						}
						if (i+(e+h)*C+y-D[k]>=0)
							if (k==(months-1))
							{
								int normcost = 0;
								if (e+h>E)
									normcost = Fcost*(e+h-E);
								else
									normcost = Hcost*(E-e-h);
								//x = min(x,(e+h)*S+hold_cost+W*(i+(e+h)*C+y-D[k])+y*OTPrice+val+normcost);
								x = min(x,(e+h)*S+hold_cost+y*OTPrice+val+normcost);
								//cout<<h<<" "<<y<<" "<<e<<" "<<(e+h)*S+hold_cost+W*(i+(e+h)*C+y-D[k])+y*OTPrice+val+normcost<<endl;
							}
							else
								x = min(x,(e+h)*S+hold_cost+W*(i+(e+h)*C+y-D[k])+y*OTPrice+val);
						
					}
				}
				v[k][i][e] = x;
				//cout<<k<<" "<<i<<" "<<e<<" "<<x<<endl;
			}
		}
	}
	cout << v[0][0][E];

}