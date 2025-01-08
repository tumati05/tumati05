import pandas as pd
import matplotlib.pyplot as plt


x = pd.read_csv("C:/Users/admin/OneDrive/Vegetable.csv")
print(x)
print(x[x.Location=='Guntur'].Seller)
totalquantity=x.groupby(x.Location)['Quantity(kg)'].sum()
print(totalquantity)
totalavg=x.groupby(x.Vegetable)['Price(perkg)'].mean()
print(totalavg)
highestquantity=x.sort_values('Quantity(kg)',ascending=False).head(1)
print(highestquantity.Vegetable)
plt.bar(x['Vegetable'], x['Quantity(kg)'])
plt.xlabel('vegetables')
plt.ylabel('quantity')
plt.xticks(rotation=45)
plt.show()

