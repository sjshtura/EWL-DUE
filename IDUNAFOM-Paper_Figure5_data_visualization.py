from bokeh.core.properties import value

from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row
from bokeh.models import Legend

output_file('stacked.html')

capacity = ['CO2_Cap', 'Min_RES_Quota', 'CO2_Tax', 'FIT']
types = ['Generation Capacity Investment', 'Fuel', 'Storage Capacity Investment', 'Storage Volume Investment', 'Lost Load', 'Emission Tax']
colors = ["#c9d9d3", "#718dbf", "#e84d60", "#FFA500", "#32CD32", '#00FFFF']

# maxload = [90.03467675, 90.03467675, 90.03467675, 90.03467675]
# Total_demand = [540.7686148, 540.7686148, 540.7686148, 540.7686148]


data = {'capacity' : capacity,
        'Generation Capacity Investment': [30.3949783, 42.4681283, 30.3921603, 48.0477212],
        'Fuel': [0.93016001, 2.28100832, 0.93107182, 1.41870756],
        'Storage Capacity Investment': [0.60875806, 3.05888709, 0.60772661, 0.66485247],
        'Storage Volume Investment': [11.2047388, 1.68108057, 11.2062415, 1.93524234],
        'Lost Load': [0, 0, 10.7381893, 0],
        'Emission Tax': [0.00308851, 0, 0.00308351, 0.08348272]
        }


s1 = figure(x_range=capacity, plot_height=450,plot_width=855, title="Costs (in B€)",
           toolbar_location='above')


s1.vbar_stack(types, x='capacity', width=0.5, color=colors, source=data,
             legend=[value(x) for x in types], hatch_pattern=['dot', 'spiral', 'vertical_wave', 'right_diagonal_line', 'vertical_dash', 'left_diagonal_line'])


s1.y_range.start = 0
s1.x_range.range_padding = 0.7
s1.xgrid.grid_line_color = None
s1.axis.minor_tick_line_color = None
s1.outline_line_color = None

# p.legend.location = "top_left"
# p.legend.orientation = "vertical"
s1.toolbar.logo = None
s1.toolbar_location = None
show(s1)

