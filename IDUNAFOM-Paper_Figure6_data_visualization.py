from bokeh.layouts import column
from bokeh.layouts import row
from bokeh.models import NumeralTickFormatter
from bokeh.plotting import figure, output_file, show
from bokeh.models import Title
import pandas as pd

data = pd.read_excel(r'Copy of Figures_Data_Preparation.xlsx', sheet_name = 'Figure 6')
data1 = data.iloc[:,1:5]


capacity = data['Pol_Inst'].unique()
types = data['Technologie'].unique()
x1 = []
for x in capacity:
    if(x == 'CO2_Cap'):
        Lignite = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[0]) | (data1['Technologie'] == types[9]))]
        Gas = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[1]) | (data1['Technologie'] == types[9]))]
        Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[2]) | (data1['Technologie'] == types[9]))]
        Demand = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[3]) | (data1['Technologie'] == types[9]))]
        Solar = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[4]) | (data1['Technologie'] == types[9]))]
        Wind_Onshore = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[5]) | (data1['Technologie'] == types[9]))]
        Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[6]) | (data1['Technologie'] == types[9]))]
        Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[7]) | (data1['Technologie'] == types[9]))]
        PSH = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[8]) | (data1['Technologie'] == types[9]))]
        #No = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[9])]

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

        shock5 = Wind_Onshore.Shock
        wind_Onshore = Wind_Onshore.Total_CO2_Emissions

        shock6 = Wind_Offshore.Shock
        wind_Offshore = Wind_Offshore.Total_CO2_Emissions

        #shock7 = No.Shock
        #no = No.Total_CO2_Emissions

        shock7 = Lit_Ion.Shock
        lit_Ion = Lit_Ion.Total_CO2_Emissions

        shock8 = PSH.Shock
        PSH = PSH.Total_CO2_Emissions

        output_file("multiple.html")

        p = figure(plot_width=400, plot_height=400)
        p.xaxis.formatter = NumeralTickFormatter(format='0 %')

# add both a line and circles on the same plot
        p.line(shock, lignite, line_width=5, color = '#9a7b5c')
        p.circle_cross(shock, lignite, fill_color="#9a7b5c", size=15)

        p.line(shock1, gas, line_width=5, color = '#ADD8E6')
        p.diamond_cross(shock1, gas, fill_color="#ADD8E6", size=20)

        p.line(shock2, hardcoal, line_width=5, color = '#414141')
        p.diamond(shock2, hardcoal, fill_color="#414141", size=20)

        p.line(shock3, demand, line_width=5, color = '#FFA500')
        p.diamond_cross(shock3, demand, fill_color="#FFA500", size=20)

        p.line(shock4, solar, line_width=5, color = '#fff340')
        p.square_cross(shock4, solar, fill_color="#fff340", size=15)

        p.line(shock5, wind_Onshore, line_width=5, color = '#00b8f2')
        p.triangle(shock5, wind_Onshore, fill_color="#00b8f2", size=15)

        p.line(shock6, Wind_Offshore, line_width=5, color = '#a19595')
        p.hex(shock6, Wind_Offshore, fill_color="#a19595", size=15)

        p.line(shock7, lit_Ion, line_width=5, color = '#f23333')
        p.square_dot(shock7, lit_Ion, fill_color="#f23333", size=15)

        p.line(shock8, PSH, line_width=5, color = '#2397fc')
        p.plus(shock8, PSH, fill_color="#2397fc", size=15)

        #p.circle(shock7, no, size =20, color = '#FF0000')
    #p.cross(shock7, no, fill_color="red", size=100)

        p.y_range.start = 500
        p.y_range.end = 2600
        #p.legend.location = "bottom_right"
        #p.legend.click_policy="hide"
        #p.add_layout(Title(text="Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)", text_line_height = 2, align="center"), "left")
        # p.add_layout(Title(text="Shock Strength", align="center"), "below")
        p.yaxis.axis_label = 'Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)'
        p.yaxis.axis_label_text_font_size = "15pt"
        p.axis.axis_label_text_font_style = 'bold'
        p.xaxis.visible = False
        p.toolbar.logo = None
        p.toolbar_location = None
        x1.append(p)

for x in capacity:
    if(x == 'Min_RES_Quota'):
        Lignite = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[0]) | (data1['Technologie'] == types[9]))]
        Gas = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[1]) | (data1['Technologie'] == types[9]))]
        Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[2]) | (data1['Technologie'] == types[9]))]
        Demand = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[3]) | (data1['Technologie'] == types[9]))]
        Solar = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[4]) | (data1['Technologie'] == types[9]))]
        Wind_Onshore = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[5]) | (data1['Technologie'] == types[9]))]
        Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[6]) | (data1['Technologie'] == types[9]))]
        Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[7]) | (data1['Technologie'] == types[9]))]
        PSH = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[8]) | (data1['Technologie'] == types[9]))]
        #No = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[9])]

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

        shock5 = Wind_Onshore.Shock
        wind_Onshore = Wind_Onshore.Total_CO2_Emissions

        shock6 = Wind_Offshore.Shock
        wind_Offshore = Wind_Offshore.Total_CO2_Emissions

        #shock7 = No.Shock
        #no = No.Total_CO2_Emissions

        shock7 = Lit_Ion.Shock
        lit_Ion = Lit_Ion.Total_CO2_Emissions

        shock8 = PSH.Shock
        PSH = PSH.Total_CO2_Emissions

        #shock7 = No.Shock
        #no = No.Total_CO2_Emissions

        output_file("multiple.html")

        p = figure(plot_width=400, plot_height=400)
        p.xaxis.formatter = NumeralTickFormatter(format='0 %')

# add both a line and circles on the same plot
        p.line(shock, lignite, line_width=5, color = '#9a7b5c')
        p.circle_cross(shock, lignite, fill_color="#9a7b5c", size=15)

        p.line(shock1, gas, line_width=5, color = '#ADD8E6')
        p.diamond_cross(shock1, gas, fill_color="#ADD8E6", size=20)

        p.line(shock2, hardcoal, line_width=5, color = '#414141')
        p.diamond(shock2, hardcoal, fill_color="#414141", size=20)

        p.line(shock3, demand, line_width=5, color = '#FFA500')
        p.diamond_cross(shock3, demand, fill_color="#FFA500", size=20)

        p.line(shock4, solar, line_width=5, color = '#fff340')
        p.square_cross(shock4, solar, fill_color="#fff340", size=15)

        p.line(shock5, wind_Onshore, line_width=5, color = '#00b8f2')
        p.triangle(shock5, wind_Onshore, fill_color="#00b8f2", size=15)

        p.line(shock6, Wind_Offshore, line_width=5, color = '#a19595')
        p.hex(shock6, Wind_Offshore, fill_color="#a19595", size=15)

        p.line(shock7, lit_Ion, line_width=5, color = '#f23333')
        p.square_dot(shock7, lit_Ion, fill_color="#f23333", size=15)

        p.line(shock8, PSH, line_width=5, color = '#2397fc')
        p.plus(shock8, PSH, fill_color="#2397fc", size=15)

        #p.circle(shock7, no, size =20, color = '#FF0000')
    #p.cross(shock7, no, fill_color="red", size=100)

        p.y_range.start = 500
        p.y_range.end = 2600
        #p.legend.location = "bottom_right"
        #p.legend.click_policy="hide"
        #p.add_layout(Title(text="Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)", text_line_height = 2, align="center"), "left")
        #p.add_layout(Title(text="Shock Strength", align="center", text_line_height = 2), "below")
        p.xaxis.axis_label = 'Shock Strength'
        p.xaxis.axis_label_text_font_size = "15pt"
        p.axis.axis_label_text_font_style = 'bold'
        p.yaxis.axis_label = 'Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)'
        p.yaxis.axis_label_text_font_size = "15pt"
        p.axis.axis_label_text_font_style = 'bold'

        p.toolbar.logo = None
        p.toolbar_location = None
        x1.append(p)

for x in capacity:
    if(x == 'CO2_Tax'):
        Lignite = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[0]) | (data1['Technologie'] == types[9]))]
        Gas = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[1]) | (data1['Technologie'] == types[9]))]
        Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[2]) | (data1['Technologie'] == types[9]))]
        Demand = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[3]) | (data1['Technologie'] == types[9]))]
        Solar = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[4]) | (data1['Technologie'] == types[9]))]
        Wind_Onshore = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[5]) | (data1['Technologie'] == types[9]))]
        Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[6]) | (data1['Technologie'] == types[9]))]
        Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[7]) | (data1['Technologie'] == types[9]))]
        PSH = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[8]) | (data1['Technologie'] == types[9]))]
        #No = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[9])]

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

        shock5 = Wind_Onshore.Shock
        wind_Onshore = Wind_Onshore.Total_CO2_Emissions

        shock6 = Wind_Offshore.Shock
        wind_Offshore = Wind_Offshore.Total_CO2_Emissions

        #shock7 = No.Shock
        #no = No.Total_CO2_Emissions

        shock7 = Lit_Ion.Shock
        lit_Ion = Lit_Ion.Total_CO2_Emissions

        shock8 = PSH.Shock
        PSH = PSH.Total_CO2_Emissions

        #shock7 = No.Shock
        #no = No.Total_CO2_Emissions

        output_file("multiple.html")
        p = figure(plot_width=600, plot_height=400)
        p.xaxis.formatter = NumeralTickFormatter(format='0 %')


        p.line(shock, lignite, line_width=5, legend ="Lignite", color = '#9a7b5c')
        p.circle_cross(shock, lignite, fill_color="#9a7b5c", size=15)

        p.line(shock1, gas, line_width=5, legend ="Gas", color = '#ADD8E6')
        p.diamond_cross(shock1, gas, fill_color="#ADD8E6", size=20)

        p.line(shock2, hardcoal, line_width=5, legend ="Hardcoal", color = '#414141')
        p.diamond(shock2, hardcoal, fill_color="#414141", size=20)

        p.line(shock3, demand, line_width=5, legend ="Demand", color = '#FFA500')
        p.diamond_cross(shock3, demand, fill_color="#FFA500", size=20)

        p.line(shock4, solar, line_width=5, legend ="PV", color = '#fff340')
        p.square_cross(shock4, solar, fill_color="#fff340", size=15)

        p.line(shock5, wind_Onshore, line_width=5, legend ="Wind Onshore", color = '#00b8f2')
        p.triangle(shock5, wind_Onshore, fill_color="#00b8f2", size=15)

        p.line(shock6, Wind_Offshore, line_width=5, legend ="Wind Offshore", color = '#a19595')
        p.hex(shock6, Wind_Offshore, fill_color="#a19595", size=15)

        p.line(shock7, lit_Ion, line_width=5, legend ="Li-Ion", color = '#f23333')
        p.square_dot(shock7, lit_Ion, fill_color="#f23333", size=15)

        p.line(shock8, PSH, line_width=5, legend ="PSH", color = '#2397fc')
        p.plus(shock8, PSH, fill_color="#2397fc", size=15)

        #p.circle(shock7, no, size =20, color = '#FF0000')
    #p.cross(shock7, no, fill_color="red", size=100)

        p.y_range.start = 500
        p.y_range.end = 2600
        #p.legend.location = "bottom_right"
        #p.legend.click_policy="hide"

        # p.add_layout(Title(text="Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)", align="center"), "left")
        # p.add_layout(Title(text="Shock Strength", align="center"), "below")
        p.add_layout(p.legend[0], 'right')
        p.legend.label_text_font_size = '18pt'
        p.xaxis.visible = False
        p.yaxis.visible = False
        p.toolbar.logo = None
        p.toolbar_location = None
        x1.append(p)

for x in capacity:
    if(x == 'FIT'):
        Lignite = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[0]) | (data1['Technologie'] == types[9]))]
        Gas = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[1]) | (data1['Technologie'] == types[9]))]
        Hardcoal = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[2]) | (data1['Technologie'] == types[9]))]
        Demand = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[3]) | (data1['Technologie'] == types[9]))]
        Solar = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[4]) | (data1['Technologie'] == types[9]))]
        Wind_Onshore = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[5]) | (data1['Technologie'] == types[9]))]
        Wind_Offshore = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[6]) | (data1['Technologie'] == types[9]))]
        Lit_Ion = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[7]) | (data1['Technologie'] == types[9]))]
        PSH = data1.loc[(data1['Pol_Inst'] == x) & ((data1['Technologie'] == types[8]) | (data1['Technologie'] == types[9]))]
        #No = data1.loc[(data1['Pol_Inst'] == x) & (data1['Technologie'] == types[9])]

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

        shock5 = Wind_Onshore.Shock
        wind_Onshore = Wind_Onshore.Total_CO2_Emissions

        shock6 = Wind_Offshore.Shock
        wind_Offshore = Wind_Offshore.Total_CO2_Emissions

        #shock7 = No.Shock
        #no = No.Total_CO2_Emissions

        shock7 = Lit_Ion.Shock
        lit_Ion = Lit_Ion.Total_CO2_Emissions

        shock8 = PSH.Shock
        PSH = PSH.Total_CO2_Emissions

        #shock7 = No.Shock
        #no = No.Total_CO2_Emissions

        output_file("multiple.html")

        p = figure(plot_width=600, plot_height=400)
        p.xaxis.formatter = NumeralTickFormatter(format='0 %')

# add both a line and circles on the same plot
        p.line(shock, lignite, line_width=5, color = '#9a7b5c')
        p.circle_cross(shock, lignite, fill_color="#9a7b5c", size=15)

        p.line(shock1, gas, line_width=5, color = '#ADD8E6')
        p.diamond_cross(shock1, gas, fill_color="#ADD8E6", size=20)

        p.line(shock2, hardcoal, line_width=5, color = '#414141')
        p.diamond(shock2, hardcoal, fill_color="#414141", size=20)

        p.line(shock3, demand, line_width=5, color = '#FFA500')
        p.diamond_cross(shock3, demand, fill_color="#FFA500", size=20)

        p.line(shock4, solar, line_width=5, color = '#fff340')
        p.square_cross(shock4, solar, fill_color="#fff340", size=15)

        p.line(shock5, wind_Onshore, line_width=5, color = '#00b8f2')
        p.triangle(shock5, wind_Onshore, fill_color="#00b8f2", size=15)

        p.line(shock6, Wind_Offshore, line_width=5, color = '#a19595')
        p.hex(shock6, Wind_Offshore, fill_color="#a19595", size=15)

        p.line(shock7, lit_Ion, line_width=5, color = '#f23333')
        p.square_dot(shock7, lit_Ion, fill_color="#f23333", size=15)

        p.line(shock8, PSH, line_width=5, color = '#2397fc')
        p.plus(shock8, PSH, fill_color="#2397fc", size=15)

        #p.circle(shock7, no, size =20, color = '#FF0000')
    #p.cross(shock7, no, fill_color="red", size=100)

        p.y_range.start = 500
        p.y_range.end = 2600
        #p.legend.location = "bottom_right"
        #p.legend.click_policy="hide"
        # p.add_layout(Title(text="Total CO\N{SUBSCRIPT TWO} Emissions (in 10\N{SUPERSCRIPT SIX}t)", align="center"), "left")
        p.xaxis.axis_label = 'Shock Strength'
        p.xaxis.axis_label_text_font_size = "15pt"
        p.axis.axis_label_text_font_style = 'bold'
        p.yaxis.visible = False
        #p.add_layout(Title(text="Shock Strength", align="center", text_line_height = 2), "below")
        #p.title.text_font_size = "25px"
        p.toolbar.logo = None
        p.toolbar_location = None#

        x1.append(p)

x = row(column(x1[0],x1[1]), row(column(x1[2],x1[3])))

from bokeh.io import export_png

import geckodriver_autoinstaller



export_png(x, filename="plot.png")

show(x)