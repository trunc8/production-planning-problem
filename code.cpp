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

	//Defining variables and initializing to zero
	int v[months+1][totalprod][int(totalprod/C)+1];
	for (int i=0; i<months+1; i++)
	{
		for (int j=0; j<totalprod; j++)
		{
			for (int k=0; k<int(totalprod/C)+1; k++)
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
			for (int e=0; e<int(totalprod/C)+1; e++)
			{
				int x = INT_MAX/2;
				for (int h=-e; h<=int(totalprod/C)-e; h++)
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
						if (i+(e+h)*C+y-D[k]>=totalprod || e+h >= int(totalprod/C)+1)
							val = 0;
						else
						{
							val = v[k+1][i+(e+h)*C+y-D[k]][e+h];
							//cout<<h<<" "<<e<<" "<<val<<endl;
						}
						if (i+(e+h)*C+y-D[k]>=0)
							if (k==(months-1))
							{
								int normcost = 0;
								if (e+h>E)
									normcost = Fcost*(e+h-E);
								else
									normcost = Hcost*(E-e-h);
								x = min(x,(e+h)*S+hold_cost+W*(i+(e+h)*C+y-D[k])+y*OTPrice+val+normcost);
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