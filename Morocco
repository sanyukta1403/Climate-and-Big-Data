import pandas as pd 

df = pd.read_csv('/Users/sanyuktasingh/Desktop/climate data class/EM-DAT Custom Request Feb 17 2026.csv')

df = df[df["Disaster Group"] == "Natural"]
morocco = df[df["Country"] == "Morocco"]
morocco = morocco[["Start Year", "Disaster Type"]]

total_events = len(morocco)
print("Total natural disaster events:", total_events)

type_counts = morocco["Disaster Type"].value_counts()
print(type_counts)

type_percent = morocco["Disaster Type"].value_counts(normalize=True) * 100
print(type_percent)

events_per_year = morocco.groupby(["Start Year", "Disaster Type"]).size().reset_index(name="Count")

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

for disaster in morocco["Disaster Type"].unique():
    subset = events_per_year[events_per_year["Disaster Type"] == disaster]
    
    plt.figure()
    plt.plot(subset["Start Year"], subset["Count"])
    plt.title(f"{disaster} in Morocco Over Time")
    plt.xlabel("Year")
    plt.ylabel("Number of Events")
    
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.show()