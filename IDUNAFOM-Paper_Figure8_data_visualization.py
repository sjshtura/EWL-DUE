#%%

from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title
import pandas as pd

data = pd.read_excel(r'Figures_Data_PreparationBB_new.xlsx', sheet_name = 'Figure 8')


data.head()

data1 = data[["Pol_Inst","Technologie","Mean_Quantity_El_Price_Enduser"]]
data2 = data1.dropna()
capacity = data['Pol_Inst'].unique()
types = data['Technologie'].unique()
print(data2)

#%%
capacity
types



#%%

import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set(style="whitegrid")
ax = sns.catplot(x="Pol_Inst", y="Mean_Quantity_El_Price_Enduser",hue = "Technologie", data=data2.query("Technologie != 'no'"))
sns.boxplot(x="Pol_Inst", y="Mean_Quantity_El_Price_Enduser", color ="k", data=data2.query("Technologie == 'no'"));
ax.set(xlabel='', ylabel='Enduser Mean Electricity price [€/MWh]')
