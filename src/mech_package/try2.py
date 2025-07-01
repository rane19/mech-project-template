import pandas as pd
import matplotlib.pyplot as plt

# Sample DDD data
data = {
    "Year": [2020, 2021, 2022, 2023, 2024] * 2,
    "Country": ["Japan"] * 5 + ["Germany"] * 5,
    "DDD_per_1000_inhabitants_day": [11.2, 10.8, 10.1, 9.6, 9.0, 17.5, 16.8, 16.0, 15.2, 14.0]
}

df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(10, 6))
for country in df["Country"].unique():
    subset = df[df["Country"] == country]
    plt.plot(subset["Year"], subset["DDD_per_1000_inhabitants_day"], label=country)

plt.title("Antibiotic Consumption Trend (DDD per 1000 inhabitants/day)")
plt.xlabel("Year")
plt.ylabel("DDD/1000 inhabitants/day")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
