"""
DATASET FROM KAGGLE.COM
"""


H0="The means of stolen property and recovered property have no significant difference."
H1="The means of stolen property and recovered property have a significant difference."


import pandas as pd
from scipy import stats
import math

data=pd.read_csv("10_Property_stolen_and_recovered.csv")

#assuming a 0.05 level of significance
recovered = data["Cases_Property_Recovered"]
clean_recovered = recovered.dropna()

stolen = data["Cases_Property_Stolen"]
clean_stolen = stolen.dropna()


x1 = data["Cases_Property_Recovered"].mean()
x2 = data["Cases_Property_Stolen"].mean()

s1 = data["Cases_Property_Recovered"].std()
s2 = data["Cases_Property_Stolen"].std()

n1 = len(data["Cases_Property_Recovered"])
n2 = len(data["Cases_Property_Stolen"])


z = abs(((x1-x2)/math.sqrt((s1**2/n1)+(s2**2/n2))))
print("n1=",n1)#all details
print("Calculated Z value=", z)

z_table_value = 1.96

if z<z_table_value:
  print("Failed to reject H0, as z value is",z, "and table value of z is ", z_table_value,"\nConclusion:",H0)

else:
  print("Reject H0 and accept H1, as z value is",z, "and table value of z is ", z_table_value,"\nConclusion:",H1)

print("\nProof:",data[["Cases_Property_Recovered","Cases_Property_Stolen"]].describe())
