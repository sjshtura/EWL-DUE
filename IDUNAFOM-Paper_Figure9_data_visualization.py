#%%

from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title
import pandas as pd
#names1 = ["Total_Co2_Emissions","Pol_Inst","Technologie","Shock","Lignite","Coal","CCGT","OCGT","Wind_Onshore","Wind_Offshore","Solar","LitIon","PSH","Total"]
data = pd.read_excel(r'Figures_Data_Preparation_9-12.xlsx', sheet_name = 'Figure 9-12', skiprows=[1])
#df = df.set_index([df.iloc[0], df.columns[0]])
data.head()

#%%
data.columns


#%%
data = data[['Total_CO2_Emissions', 'Pol_Inst', 'Technologie', 'Shock','Lignite', 'Coal', 'CCGT', 'OCGT', 'Wind_Onshore', 'Wind_Offshore',
       'Solar', 'LitIon', 'PSH', 'Total']]

data.head()


#%%

data2 = data.dropna()
capacity = data['Pol_Inst'].unique()
types = data['Technologie'].unique()
print(data2)


#%%

import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set(style="whitegrid")
ax = sns.boxplot(x="Pol_Inst", y="Mean_Quantity_El_Price_Enduser", data=data2)
ax.set(xlabel='', ylabel='Enduser Mean Electricity price [€/MWh]')

