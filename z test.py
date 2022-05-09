

"""
DATASET FROM KAGGLE.COM
"""


H0="The means of stolen property and recovered property have no significant difference."
H1="The means of stolen property and recovered property have a significant difference."


import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import math

def ztest(x1,x2,s1,s2,n1,n2):
  z = abs(((x1-x2)/math.sqrt((s1**2/n1)+(s2**2/n2))))
  return z

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

z = ztest(x1,x2,s1,s2,n1,n2)
print("When x1=",x1,"\nx2=",x2,"\ns1=",s1,"\ns2=",s2,"\nn1=",n1,"\nn2=",n2)#all details
print("\nCalculated Z value=", z)

z_table_value = 1.96

if z<z_table_value:
  print("Failed to reject H0, as z value is",z, "and table value of z is ", z_table_value,"\nConclusion:",H0)

else:
  print("Reject H0 and accept H1, as z value is",z, "and table value of z is ", z_table_value,"\nConclusion:",H1)

print("\nProof:",data[["Cases_Property_Recovered","Cases_Property_Stolen"]].describe())


plt.plot(data["Cases_Property_Stolen"],data["Area_Name"])
plt.xlabel("Stolen")
plt.ylabel("Area")

plt.figure()

plt.plot(data["Cases_Property_Recovered"],data["Area_Name"])
plt.xlabel("Recovered")
plt.ylabel("Area")
