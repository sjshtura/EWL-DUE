from bokeh.layouts import column
from bokeh.layouts import row
from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title
import pandas as pd

data = pd.read_excel(r'/Users/shakhawat_hossain_turag/Desktop/Uni/Energiewirtschaft /Copy of Figures_Data_Preparation.xlsx', sheet_name = 'Figure 6')
data1 = data.iloc[:,1:5]


capacity = data['Pol_Inst'].unique()
types = data['Technologie'].unique()
x1 = []
for x in capacity:
    if(x == 'CO2_Cap'):
        Lignite = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[0])]
        Gas = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[1])]
        Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[2])]
        Demand = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[3])]
        Solar = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[4])]
        Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[5])]
        Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[6])]
        No = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[9])]

        shock = Lignite.Shock
        lignite = Lignite.Total_CO2_Emissions

        shock1 = Gas.Shock
        gas = Gas.Total_CO2_Emissions

        shock2 = Hardcoal.Shock
        hardcoal = Hardcoal.Total_CO2_Emissions

        shock3 = Demand.Shock
        demand = Demand.Total_CO2_Emissions

        shock4 = Solar.Shock
        solar = Solar.Total_CO2_Emissions

        shock5 = Wind_Offshore.Shock
        wind_Offshore = Wind_Offshore.Total_CO2_Emissions

        shock6 = Lit_Ion.Shock
        lit_Ion = Lit_Ion.Total_CO2_Emissions

        shock7 = No.Shock
        no = No.Total_CO2_Emissions

        output_file("multiple.html")

        p = figure(plot_width=1000, plot_height=600)
        p.xaxis.formatter = NumeralTickFormatter(format='0 %')

# add both a line and circles on the same plot
        p.line(shock, lignite, line_width=3, legend = 'Lignite', color = '#9a7b5c')
        p.circle_cross(shock, lignite, fill_color="white", size=10)

        p.line(shock1, gas, line_width=3, legend = 'Gas', color = '#ADD8E6')
        p.diamond_cross(shock1, gas, fill_color="white", size=10)

        p.line(shock2, hardcoal, line_width=3, legend = 'Hardcoal', color = '#414141')
        p.diamond(shock2, hardcoal, fill_color="white", size=10)

        p.line(shock3, demand, line_width=3, legend = 'Demand', color = '#FFA500')
        p.diamond_cross(shock3, demand, fill_color="white", size=10)

        p.line(shock4, solar, line_width=3, legend = 'Solar', color = '#fff340')
        p.square_cross(shock4, solar, fill_color="white", size=10)

        p.line(shock5, wind_Offshore, line_width=3, legend = 'Wind_Offshore', color = '#00b8f2')
        p.triangle(shock5, wind_Offshore, fill_color="white", size=10)

        p.line(shock6, lit_Ion, line_width=3, legend = 'Li_Ion', color = '#C0C0C0')
        p.hex(shock6, lit_Ion, fill_color="white", size=10)

        p.circle(shock7, no, size =20, color = '#FF0000')
    #p.cross(shock7, no, fill_color="red", size=100)

        p.y_range.start = 500
        p.y_range.end = 2600
        p.legend.location = "bottom_right"
        p.legend.click_policy="hide"
        p.add_layout(Title(text="Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)", align="center"), "left")
        # p.add_layout(Title(text="Shock Strength", align="center"), "below")
        p.toolbar.logo = None
        p.toolbar_location = None
        x1.append(p)

for x in capacity:
    if(x == 'Min_RES_Quota'):
        Lignite = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[0])]
        Gas = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[1])]
        Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[2])]
        Demand = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[3])]
        Solar = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[4])]
        Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[5])]
        Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[6])]
        No = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[9])]

        shock = Lignite.Shock
        lignite = Lignite.Total_CO2_Emissions

        shock1 = Gas.Shock
        gas = Gas.Total_CO2_Emissions

        shock2 = Hardcoal.Shock
        hardcoal = Hardcoal.Total_CO2_Emissions

        shock3 = Demand.Shock
        demand = Demand.Total_CO2_Emissions

        shock4 = Solar.Shock
        solar = Solar.Total_CO2_Emissions

        shock5 = Wind_Offshore.Shock
        wind_Offshore = Wind_Offshore.Total_CO2_Emissions

        shock6 = Lit_Ion.Shock
        lit_Ion = Lit_Ion.Total_CO2_Emissions

        shock7 = No.Shock
        no = No.Total_CO2_Emissions

        output_file("multiple.html")

        p = figure(plot_width=1000, plot_height=600)
        p.xaxis.formatter = NumeralTickFormatter(format='0 %')

# add both a line and circles on the same plot
        p.line(shock, lignite, line_width=3, legend = 'Lignite', color = '#9a7b5c')
        p.circle_cross(shock, lignite, fill_color="white", size=10)

        p.line(shock1, gas, line_width=3, legend = 'Gas', color = '#ADD8E6')
        p.diamond_cross(shock1, gas, fill_color="white", size=10)

        p.line(shock2, hardcoal, line_width=3, legend = 'Hardcoal', color = '#414141')
        p.diamond(shock2, hardcoal, fill_color="white", size=10)

        p.line(shock3, demand, line_width=3, legend = 'Demand', color = '#FFA500')
        p.diamond_cross(shock3, demand, fill_color="white", size=10)

        p.line(shock4, solar, line_width=3, legend = 'Solar', color = '#fff340')
        p.square_cross(shock4, solar, fill_color="white", size=10)

        p.line(shock5, wind_Offshore, line_width=3, legend = 'Wind_Offshore', color = '#00b8f2')
        p.triangle(shock5, wind_Offshore, fill_color="white", size=10)

        p.line(shock6, lit_Ion, line_width=3, legend = 'Li_Ion', color = '#C0C0C0')
        p.hex(shock6, lit_Ion, fill_color="white", size=10)

        p.circle(shock7, no, size =20, color = '#FF0000')
    #p.cross(shock7, no, fill_color="red", size=100)

        p.y_range.start = 500
        p.y_range.end = 2600
        p.legend.location = "bottom_right"
        p.legend.click_policy="hide"
        p.add_layout(Title(text="Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)", align="center"), "left")
        p.add_layout(Title(text="Shock Strength", align="center"), "below")
        p.toolbar.logo = None
        p.toolbar_location = None
        x1.append(p)

for x in capacity:
    if(x == 'CO2_Tax'):
        Lignite = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[0])]
        Gas = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[1])]
        Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[2])]
        Demand = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[3])]
        Solar = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[4])]
        Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[5])]
        Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[6])]
        No = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[9])]

        shock = Lignite.Shock
        lignite = Lignite.Total_CO2_Emissions

        shock1 = Gas.Shock
        gas = Gas.Total_CO2_Emissions

        shock2 = Hardcoal.Shock
        hardcoal = Hardcoal.Total_CO2_Emissions

        shock3 = Demand.Shock
        demand = Demand.Total_CO2_Emissions

        shock4 = Solar.Shock
        solar = Solar.Total_CO2_Emissions

        shock5 = Wind_Offshore.Shock
        wind_Offshore = Wind_Offshore.Total_CO2_Emissions

        shock6 = Lit_Ion.Shock
        lit_Ion = Lit_Ion.Total_CO2_Emissions

        shock7 = No.Shock
        no = No.Total_CO2_Emissions

        output_file("multiple.html")

        p = figure(plot_width=1000, plot_height=600)
        p.xaxis.formatter = NumeralTickFormatter(format='0 %')

# add both a line and circles on the same plot
        p.line(shock, lignite, line_width=3, legend = 'Lignite', color = '#9a7b5c')
        p.circle_cross(shock, lignite, fill_color="white", size=10)

        p.line(shock1, gas, line_width=3, legend = 'Gas', color = '#ADD8E6')
        p.diamond_cross(shock1, gas, fill_color="white", size=10)

        p.line(shock2, hardcoal, line_width=3, legend = 'Hardcoal', color = '#414141')
        p.diamond(shock2, hardcoal, fill_color="white", size=10)

        p.line(shock3, demand, line_width=3, legend = 'Demand', color = '#FFA500')
        p.diamond_cross(shock3, demand, fill_color="white", size=10)

        p.line(shock4, solar, line_width=3, legend = 'Solar', color = '#fff340')
        p.square_cross(shock4, solar, fill_color="white", size=10)

        p.line(shock5, wind_Offshore, line_width=3, legend = 'Wind_Offshore', color = '#00b8f2')
        p.triangle(shock5, wind_Offshore, fill_color="white", size=10)

        p.line(shock6, lit_Ion, line_width=3, legend = 'Li_Ion', color = '#C0C0C0')
        p.hex(shock6, lit_Ion, fill_color="white", size=10)

        p.circle(shock7, no, size =20, color = '#FF0000')
    #p.cross(shock7, no, fill_color="red", size=100)

        p.y_range.start = 500
        p.y_range.end = 2600
        p.legend.location = "bottom_right"
        p.legend.click_policy="hide"
        # p.add_layout(Title(text="Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)", align="center"), "left")
        # p.add_layout(Title(text="Shock Strength", align="center"), "below")
        p.toolbar.logo = None
        p.toolbar_location = None
        x1.append(p)

for x in capacity:
    if(x == 'FIT'):
        Lignite = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[0])]
        Gas = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[1])]
        Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[2])]
        Demand = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[3])]
        Solar = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[4])]
        Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[5])]
        Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[6])]
        No = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[9])]

        shock = Lignite.Shock
        lignite = Lignite.Total_CO2_Emissions

        shock1 = Gas.Shock
        gas = Gas.Total_CO2_Emissions

        shock2 = Hardcoal.Shock
        hardcoal = Hardcoal.Total_CO2_Emissions

        shock3 = Demand.Shock
        demand = Demand.Total_CO2_Emissions

        shock4 = Solar.Shock
        solar = Solar.Total_CO2_Emissions

        shock5 = Wind_Offshore.Shock
        wind_Offshore = Wind_Offshore.Total_CO2_Emissions

        shock6 = Lit_Ion.Shock
        lit_Ion = Lit_Ion.Total_CO2_Emissions

        shock7 = No.Shock
        no = No.Total_CO2_Emissions

        output_file("multiple.html")

        p = figure(plot_width=1000, plot_height=600)
        p.xaxis.formatter = NumeralTickFormatter(format='0 %')

# add both a line and circles on the same plot
        p.line(shock, lignite, line_width=3, legend = 'Lignite', color = '#9a7b5c')
        p.circle_cross(shock, lignite, fill_color="white", size=10)

        p.line(shock1, gas, line_width=3, legend = 'Gas', color = '#ADD8E6')
        p.diamond_cross(shock1, gas, fill_color="white", size=10)

        p.line(shock2, hardcoal, line_width=3, legend = 'Hardcoal', color = '#414141')
        p.diamond(shock2, hardcoal, fill_color="white", size=10)

        p.line(shock3, demand, line_width=3, legend = 'Demand', color = '#FFA500')
        p.diamond_cross(shock3, demand, fill_color="white", size=10)

        p.line(shock4, solar, line_width=3, legend = 'Solar', color = '#fff340')
        p.square_cross(shock4, solar, fill_color="white", size=10)

        p.line(shock5, wind_Offshore, line_width=3, legend = 'Wind_Offshore', color = '#00b8f2')
        p.triangle(shock5, wind_Offshore, fill_color="white", size=10)

        p.line(shock6, lit_Ion, line_width=3, legend = 'Li_Ion', color = '#C0C0C0')
        p.hex(shock6, lit_Ion, fill_color="white", size=10)

        p.circle(shock7, no, size =20, color = '#FF0000')
    #p.cross(shock7, no, fill_color="red", size=100)

        p.y_range.start = 500
        p.y_range.end = 2600
        p.legend.location = "bottom_right"
        p.legend.click_policy="hide"
        # p.add_layout(Title(text="Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)", align="center"), "left")
        p.add_layout(Title(text="Shock Strength", align="center"), "below")
        p.toolbar.logo = None
        p.toolbar_location = None
        x1.append(p)

show(row(column(x1[0],x1[1]), row(column(x1[2],x1[3]))))

