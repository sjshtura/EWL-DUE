
from bokeh.core.properties import value
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row
from bokeh.models import Legend
from bokeh.layouts import column
output_file('stacked.html')

capacity = ['CO2_Cap', 'Min_RES_Quota', 'CO2_Tax', 'FIT']
types = ['Li-Ion', 'PSH']
colors = ["#FF0000", "#0000FF"]

# maxload = [90.03467675, 90.03467675, 90.03467675, 90.03467675]
# Total_demand = [540.7686148, 540.7686148, 540.7686148, 540.7686148]


data = {'capacity' : capacity,
        'Li-Ion'   : [6.679838997, 4.634989823, 6.662090027, 2.767248123],
        'PSH'   : [13.74249003, 35.57488525, 13.75983893, 22.14477819]
        }

data1 = {'capacity' : capacity,
        'Li-Ion'   : [21.56012255, 13.20917061, 21.46477519, 9.243699164],
        'PSH'   : [240.5969273, 1997.715258, 240.6769677, 381.3648777]
        }

s1 = figure(x_range=capacity, plot_height=450,plot_width=655, title="Capacity (in GW)",
           toolbar_location='above')
s2 = figure(x_range=capacity, plot_height=450,plot_width=655, title="Volume (in GWh)",
           toolbar_location='above')

s1.vbar_stack(types, x='capacity', width=0.3, color=colors, source=data,
             legend=[value(x) for x in types], hatch_pattern=['dot', 'spiral'])
# s1.line(x = capacity, y = maxload, color="red", line_width=3, legend_label = "max_load")

s2.vbar_stack(types, x='capacity', width=0.3, color=colors, source=data1,
             legend=[value(x) for x in types], hatch_pattern=['dot', 'spiral'])
# s2.line(x = capacity, y = Total_demand, color="blue", line_width=3, legend_label = "max_load")


s1.y_range.start = 0
s1.x_range.range_padding = 0.1
s1.xgrid.grid_line_color = None
s1.axis.minor_tick_line_color = None
s1.outline_line_color = None
s1.toolbar.logo = None
s1.toolbar_location = None

s2.y_range.start = 0
s2.x_range.range_padding = 0.1
s2.xgrid.grid_line_color = None
s2.axis.minor_tick_line_color = None
s2.outline_line_color = None
# p.legend.location = "top_left"
# p.legend.orientation = "vertical"
s2.toolbar.logo = None
s2.toolbar_location = None
show(row(s1,s2))