from asyncio.windows_events import NULL
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
df = pd.read_csv(r"C:\Users\yakup\Desktop\Data Science\Proje-1\Turnstile_Usage_Data__2021.csv")
df.drop(["Unit","SCP", "C/A"] ,axis=1, inplace= True)
df.info()
station_entries = df.Station.value_counts()
plt.show(block = True)
plt.show.hist(station_entries)

