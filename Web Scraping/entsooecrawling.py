
from entsoe import EntsoePandasClient
import pandas as pd
import mysql.connector

client = EntsoePandasClient(api_key='c4d117a2-f140-492b-bc2b-d615ec5774f4')

start = pd.Timestamp('20171201', tz='Europe/Brussels')
end = pd.Timestamp('20180101', tz='Europe/Brussels')
country_code = 'BE'  # Belgium

# methods that return Pandas Series
client.query_day_ahead_prices(country_code, start=start,end=end)
client.query_load(country_code, start=start,end=end)
client.query_load_forecast(country_code, start=start,end=end)
client.query_generation_forecast(country_code, start=start,end=end)

# methods that return Pandas DataFrames
client.query_wind_and_solar_forecast(country_code, start=start,end=end, psr_type=None)
client.query_generation(country_code, start=start,end=end, psr_type=None)
client.query_installed_generation_capacity(country_code, start=start,end=end, psr_type=None)
client.query_crossborder_flows('DE', 'DK', start=start,end=end)
client.query_imbalance_prices(country_code, start=start,end=end, psr_type=None)
client.query_unavailability_of_generation_units(country_code, start=start,end=end, docstatus=None)
#client.query_withdrawn_unavailability_of_generation_units('DE', start=start,end=end)

ts = client.query_day_ahead_prices(country_code, start=start, end=end)


ts1 = ts.to_frame(name = "value")

ts1 = ts1.reset_index()
#print(ts1)
for col in ts1.columns:
    print(col)
#ts1.index = ts1.tz_convert('')
#print(ts1['index'])

from datetime import datetime
import numpy as np

#ts1['index'] = pd.to_datetime(ts1['index'], format='%Y%m%d %H:%M:%S', errors='coerce')
print(type(ts1['index']))




# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     passwd = "12345678",
#     database = "entsoedb"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute('''Drop Table IF Exists entsoedata''')
# mycursor.execute('''create table entsoedata (datedata Text , vals Text)''')
# mycursor.execute('''Insert Into  entsoedata VALUES (%s,%s)''', (ts1.index, ts1['value']))
# mydb.commit()

