from bokeh.plotting import figure, output_file, show
from bokeh.models import Title
from bokeh.core.properties import value
from bokeh.layouts import row
from bokeh.models import Legend
from bokeh.io import export_svgs
from bokeh.models import LinearAxis, Range1d
from bokeh.layouts import column
output_file('stacked.html')

capacity = ['CO2_Cap', 'Min_RES_Quota', 'CO2_Tax', 'FIT']
types = ['Lignite', 'Coal', 'CCGT', 'OCGT','Wind Onshore', 'Wind Offshore', 'Solar']
colors = ["#9a7b5c", "#414141", "#c7dada", "#c7dada", "#5a67ff",'#00b8f2', '#fff340']

maxload = [90.03467675, 90.03467675, 90.03467675, 90.03467675]
Total_demand = [540.7686148, 540.7686148, 540.7686148, 540.7686148]


data = {'capacity' : capacity,
        'Lignite'   : [0,22.28330605,0,25.76575924],
        'Coal'   : [0, 0, 0,0],
        'CCGT'   : [52.12309276, 0.209356135, 52.12598273, 6.416971663],
        'OCGT'   : [10.1753325,20.35167058,10.1729694,22.18142626],
        'Wind Onshore': [90.66714923, 77.28982927, 90.6875821, 86.3713515],
        'Wind Offshore': [24.26075426, 53.92876756, 24.25201174, 60.265434],
        'Solar' : [90.1174063, 159.3567357, 90.0774928, 178.0811123]
        }

s1 = figure(x_range=capacity, plot_height=450,plot_width=755,
            title="Capacity (in GW)")


s1.vbar_stack(types, x='capacity', width=0.5, color=colors, source=data,
             legend=[value(x) for x in types], hatch_pattern=['dot', 'spiral', 'vertical_wave', 'right_diagonal_line', 'vertical_dash', 'left_diagonal_line', 'ring'])

s1.ray(x=[-1], y = maxload, color="red", line_width=3, legend_label = "max_load")

s1.y_range.start = 0
s1.x_range.range_padding = 0.7
s1.legend.location = "top_right"
s1.legend.click_policy="hide"
# s1.add_layout(Title(text="Capacity (in GW) "), "left")



#show(s1)

#%%

data1 = {'capacity' : capacity,
        'Lignite'   : [0,88.2252938,0,85.90146504],
        'Coal'   : [0, 0, 0,0],
        'CCGT'   : [218.8212912, 0.250079171, 218.8516421, 9.432063474],
        'OCGT'   : [2.066936184, 12.32389683, 2.066549459, 9.832265967],
        'Wind Onshore': [163.1994313, 139.1204674, 163.2362101, 155.4670635],
        'Wind Offshore': [84.91148221, 188.748113, 84.8808838, 210.9261432],
        'Solar' : [81.10978468, 143.4283459, 81.0738607, 160.2811406]
        }

s2 = figure(x_range=capacity, plot_height=450,plot_width=755,
            title="Power Generation (in TWh)")
s2.vbar_stack(types, x='capacity', width=0.5, color=colors, source=data1,
             legend=[value(x) for x in types], hatch_pattern=['dot', 'spiral', 'vertical_wave', 'right_diagonal_line', 'vertical_dash', 'left_diagonal_line', 'ring'])
s2.ray(x = [-1], y = Total_demand, color="blue", line_width=3, legend_label = "Total Demand")

s2.y_range.start = 0
s2.x_range.range_padding = 0.7
s2.legend.location = "top_right"
s2.legend.click_policy="hide"
show(column(s1,s2))

