#%%

from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title
import pandas as pd

data = pd.read_excel(r'/Users/shakhawat_hossain_turag/Desktop/Uni/Energiewirtschaft /Copy of Figures_Data_Preparation.xlsx', sheet_name = 'Figure 8')

data.head()

data1 = data[["Pol_Inst","Technologie","Mean_Quantity_El_Price_Enduser"]]
data2 = data1.dropna()
capacity = data['Pol_Inst'].unique()
types = data['Technologie'].unique()
print(data2)

#%%

import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set(style="whitegrid")
ax = sns.boxplot(x="Pol_Inst", y="Mean_Quantity_El_Price_Enduser", data=data2)
ax.set(xlabel='', ylabel='Enduser Mean Electricity price [€/MWh]')

