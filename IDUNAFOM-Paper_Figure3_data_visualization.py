from bokeh.core.properties import value
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row
from bokeh.models import Legend
from bokeh.io import export_svgs

output_file('stacked.html')

capacity = ['CO2_Cap', 'Min_RES_Quota', 'CO2_Tax', 'FIT']
types = ['Lignite', 'Coal', 'CCGT', 'OCGT','Wind Onshore', 'Wind Offshore', 'Solar']
colors = ["#c9d9d3", "#718dbf", "#e84d60", "#FFA500", "#32CD32",'#00FFFF', '#FAEBD7']

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

data1 = {'capacity' : capacity,
        'Lignite'   : [0,88.2252938,0,85.90146504],
        'Coal'   : [0, 0, 0,0],
        'CCGT'   : [218.8212912, 0.250079171, 218.8516421, 9.432063474],
        'OCGT'   : [2.066936184, 12.32389683, 2.066549459, 9.832265967],
        'Wind Onshore': [163.1994313, 139.1204674, 163.2362101, 155.4670635],
        'Wind Offshore': [84.91148221, 188.748113, 84.8808838, 210.9261432],
        'Solar' : [81.10978468, 143.4283459, 81.0738607, 160.2811406]
        }


s1 = figure(x_range=capacity, plot_height=450,plot_width=655, title="Capacity (in [GW])",
           toolbar_location='above')
s2 = figure(x_range=capacity, plot_height=450,plot_width=655, title="Generation (in [GW])",
           toolbar_location='above')

s1.vbar_stack(types, x='capacity', width=0.3, color=colors, source=data,
             legend=[value(x) for x in types], hatch_pattern=['dot', 'spiral', 'vertical_wave', 'right_diagonal_line', 'vertical_dash', 'left_diagonal_line', 'ring'])
s1.line(x = capacity, y = maxload, color="red", line_width=3, legend_label = "max_load")

s2.vbar_stack(types, x='capacity', width=0.3, color=colors, source=data1,
             legend=[value(x) for x in types], hatch_pattern=['dot', 'spiral', 'vertical_wave', 'right_diagonal_line', 'vertical_dash', 'left_diagonal_line', 'ring'])
s2.line(x = capacity, y = Total_demand, color="blue", line_width=3, legend_label = "max_load")


s1.y_range.start = 0
s1.x_range.range_padding = 0.1
s1.xgrid.grid_line_color = None
s1.axis.minor_tick_line_color = None
s1.outline_line_color = None

s2.y_range.start = 0
s2.x_range.range_padding = 0.1
s2.xgrid.grid_line_color = None
s2.axis.minor_tick_line_color = None
s2.outline_line_color = None
# p.legend.location = "top_left"
# p.legend.orientation = "vertical"
p = row(s1, s2)
p.output_backend = "svg"
export_svgs(p, filename="plot.svg")
show(p)