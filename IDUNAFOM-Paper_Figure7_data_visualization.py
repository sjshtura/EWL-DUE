
from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title
import pandas as pd
import plotly.express as px

data = pd.read_excel(r'/Users/shakhawat_hossain_turag/Desktop/Uni/Energiewirtschaft /Copy of Figures_Data_Preparation.xlsx', sheet_name = 'Figure 7')
data1 = data[["Total_CO2_Emissions","Pol_Inst","Technologie","Total_System_Cost"]]
data2 = data1.dropna()

data2 = data2.loc[data2["Technologie"] != "no"]

capacity = data2['Pol_Inst'].unique()
types = data2['Technologie'].unique()

Lignite1 = pd.DataFrame()
Gas1 = pd.DataFrame()
Hardcoal1 = pd.DataFrame()
Demand1 = pd.DataFrame()
Solar1 = pd.DataFrame()
Wind_Onshore1 = pd.DataFrame()
Wind_Offshore1 = pd.DataFrame()
Lit_Ion1 = pd.DataFrame()
PSH1 = pd.DataFrame()
for x in capacity:
    Lignite = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[0])]
    Gas = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[1])]
    Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[2])]
    Demand = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[3])]
    Solar = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[4])]
    Wind_Onshore = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[5])]
    Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[6])]
    Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[7])]
    PSH = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[8])]
    Lignite1 = Lignite1.append(Lignite)
    Gas1 = Gas1.append(Gas)
    Hardcoal1 = Hardcoal1.append(Hardcoal)
    Demand1 = Demand1.append(Demand)
    Solar1 = Solar1.append(Solar)
    Wind_Offshore1 = Wind_Offshore1.append(Wind_Offshore)
    Wind_Onshore1 = Wind_Onshore1.append(Wind_Onshore)
    Lit_Ion1 = Lit_Ion1.append(Lit_Ion)
    PSH1 = PSH1.append(PSH)
print(Lignite1)

from plotly.subplots import make_subplots
fig = make_subplots(rows=2)

fig.add_scatter(

)
fig = px.scatter(data2, x = "Total_System_Cost", y= "Total_CO2_Emissions",
                            color="Pol_Inst", symbol="Pol_Inst",
                            facet_col='Technologie',facet_col_wrap=3,width=1000, height=800)

#fig.write_image("images/gg2.png")
fig.update_traces(marker=dict(size=10,
                              line=dict(width=1)))
fig.write_image("images/Figure7.png")





