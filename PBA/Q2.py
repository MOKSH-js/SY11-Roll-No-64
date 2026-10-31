import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

print("Average Temperature:", df["Temperature"].mean())
print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())

day = df.loc[df["Temperature"].idxmax(), "Date"]
print("Highest Temperature Day:", day)

plt.plot(df["Date"], df["Temperature"], marker="o")
plt.title("Daily Temperature Changes")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.show()

plt.hist(df["Temperature"], bins=5)
plt.title("Temperature Distribution")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["Humidity"], df["Temperature"])
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature")
plt.show()
