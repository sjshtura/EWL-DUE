
from entsoe import EntsoePandasClient
import pandas as pd

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
print(ts1)
for col in ts1.columns:
    print(col)
print(ts1.index)
print(ts1.value)

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456",
    database = "entsoe"
)

mycursor = mydb.cursor()

mycursor.execute('''Drop Table IF Exists entsoedata''')
mycursor.execute('''create table entsoedata(datedata datet , vals text )''')
mycursor.execute('''Insert Into  entsoedata VALUES (%s,%s)''', (ts1.index[0], ts1['value'][0]))
mydb.commit()

