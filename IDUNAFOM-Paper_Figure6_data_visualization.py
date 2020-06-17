from bokeh.core.properties import value
from bokeh.plotting import figure, show, output_file
from bokeh.layouts import row
from bokeh.models import Legend
import pandas as pd

# output_file('stacked.html')

# capacity = ['CO2_Cap', 'Min_RES_Quota', 'CO2_Tax', 'FIT']
# types = ['Costs_K_G', 'Costs_K_S_ch', 'Costs_V_S', 'Costs_op_fu_G_C', 'Costs_op_em_G_C', 'Costs_VolL']
# colors = ["#c9d9d3", "#718dbf", "#e84d60", "#FFA500", "#32CD32", '#00FFFF']

# maxload = [90.03467675, 90.03467675, 90.03467675, 90.03467675]
# Total_demand = [540.7686148, 540.7686148, 540.7686148, 540.7686148]


data = pd.read_csv(r'/Users/shakhawat_hossain_turag/Desktop/Uni/Energiewirtschaft /Copy of Figures_Data_Preparation.xlsx', sheet_name = 'Figure 6')


s1 = figure(x_range=capacity, plot_height=450,plot_width=855, title="Costs (in B€)",
           toolbar_location='above')


s1.vbar_stack(types, x='capacity', width=0.3, color=colors, source=data,
             legend=[value(x) for x in types], hatch_pattern=['dot', 'spiral', 'vertical_wave', 'right_diagonal_line', 'vertical_dash', 'left_diagonal_line'])


s1.y_range.start = 0
s1.x_range.range_padding = 0.1
s1.xgrid.grid_line_color = None
s1.axis.minor_tick_line_color = None
s1.outline_line_color = None

# p.legend.location = "top_left"
# p.legend.orientation = "vertical"
p = row(s1)
show(p)