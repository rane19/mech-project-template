import pandas as pd

# Sample prescriptions
data = [
    {"Patient_ID": 1, "Drug_Name": "Metformin", "Fill_Date": "2024-01-10"},
    {"Patient_ID": 1, "Drug_Name": "Insulin", "Fill_Date": "2024-04-01"},
    {"Patient_ID": 2, "Drug_Name": "Metformin", "Fill_Date": "2024-02-01"},
    {"Patient_ID": 2, "Drug_Name": "Glipizide", "Fill_Date": "2024-05-15"},
    {"Patient_ID": 3, "Drug_Name": "Metformin", "Fill_Date": "2024-01-01"},
    {"Patient_ID": 3, "Drug_Name": "Insulin", "Fill_Date": "2024-09-01"},  # too late
]

df = pd.DataFrame(data)
df["Fill_Date"] = pd.to_datetime(df["Fill_Date"])

# Identify Metformin start dates
metformin = df[df["Drug_Name"] == "Metformin"].rename(columns={"Fill_Date": "Metformin_Date"})

# Merge back to find later drugs
merged = df.merge(metformin[["Patient_ID", "Metformin_Date"]], on="Patient_ID")
merged = merged[merged["Fill_Date"] > merged["Metformin_Date"]]

# Calculate time difference
merged["Days_Later"] = (merged["Fill_Date"] - merged["Metformin_Date"]).dt.days

# Filter those who switched to Insulin within 180 days
switched = merged[(merged["Drug_Name"] == "Insulin") & (merged["Days_Later"] <= 180)]


print("Patients who switched from Metformin to Insulin within 180 days:")
print(switched[["Patient_ID", "Metformin_Date", "Fill_Date", "Days_Later"]])
