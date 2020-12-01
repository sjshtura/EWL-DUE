from tzlocal import get_localzone  # tzlocal needs to be extra installed
import pandas as pd


df = pd.read_csv(r"/Users/shakhawat_hossain_turag/PycharmProjects/EWL-DUE/outfile.csv")
df.head()