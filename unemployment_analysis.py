# ==============================================================
#            CODEALPHA INTERNSHIP PROJECT
#          UNEMPLOYMENT ANALYSIS USING PYTHON
#                Developed by : Shaik Numaan
# ==============================================================
# ================= IMPORT LIBRARIES =================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# ================= LOAD DATASET =================
data = pd.read_csv("Unemployment in India.csv")
print("\n================================================")
print("              DATASET PREVIEW")
print("================================================\n")
print(data.head())
print("\n================================================")
print("             DATASET INFORMATION")
print("================================================\n")
print(data.info())
print("\n================================================")
print("              RANDOM SAMPLE DATA")
print("================================================\n")
print(data.sample(5))
# ================= RENAME COLUMNS =================
data.columns = [
    "Region",
    "Date",
    "Frequency",
    "Estimated_Unemployment_Rate",
    "Estimated_Employed",
    "Estimated_Labour_Participation_Rate",
    "Area"
]
# ================= REMOVE MISSING VALUES =================
data = data.dropna()
print("\n================================================")
print("               MISSING VALUES")
print("================================================\n")
print(data.isnull().sum())
# ================= CONVERT DATE =================
data["Date"] = pd.to_datetime(
    data["Date"],
    dayfirst=True
)
# ================= BASIC STATISTICS =================
print("\n================================================")
print("             STATISTICAL SUMMARY")
print("================================================\n")
print(data.describe())
# ==============================================================
# DIAGRAM 1 : UNEMPLOYMENT RATE DISTRIBUTION
# ==============================================================
plt.figure(figsize=(10,6))
plt.hist(
    data["Estimated_Unemployment_Rate"],
    bins=15
)
plt.xlabel("Unemployment Rate", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Distribution of Unemployment Rates", fontsize=15)
plt.grid(True)
plt.show()
# ==============================================================
# DIAGRAM 2 : TOP 10 REGIONS WITH HIGH UNEMPLOYMENT
# ==============================================================
top_regions = data.groupby("Region")[
    "Estimated_Unemployment_Rate"
].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
top_regions.plot(kind="bar")
plt.xlabel("Regions", fontsize=12)
plt.ylabel("Average Unemployment Rate", fontsize=12)
plt.title("Top 10 Regions with Highest Unemployment", fontsize=15)
plt.grid(True)
plt.show()
# ==============================================================
# DIAGRAM 3 : EMPLOYMENT ANALYSIS
# ==============================================================
top_employment = data.sort_values(
    by="Estimated_Employed",
    ascending=False
).head(10)
plt.figure(figsize=(12,6))
plt.bar(
    top_employment["Region"],
    top_employment["Estimated_Employed"]
)
plt.xticks(rotation=45)
plt.xlabel("Region", fontsize=12)
plt.ylabel("Estimated Employed", fontsize=12)
plt.title("Top Employment Regions", fontsize=15)
plt.grid(True)
plt.show()
# ==============================================================
# DIAGRAM 4 : LABOUR PARTICIPATION ANALYSIS
# ==============================================================
area_data = data.groupby("Area")[
    "Estimated_Labour_Participation_Rate"
].mean()
plt.figure(figsize=(8,6))
plt.pie(
    area_data,
    labels=area_data.index,
    autopct="%1.1f%%"
)
plt.title("Labour Participation Rate by Area", fontsize=15)
plt.show()
# ==============================================================
# DIAGRAM 5 : MONTHLY UNEMPLOYMENT TREND
# ==============================================================
monthly_data = data.groupby("Date")[
    "Estimated_Unemployment_Rate"
].mean()
plt.figure(figsize=(12,6))
plt.plot(
    monthly_data.index,
    monthly_data.values,
    linewidth=3
)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Average Unemployment Rate", fontsize=12)
plt.title("Monthly Unemployment Trend in India", fontsize=15)
plt.grid(True)
plt.show()
# ==============================================================
# FINAL INSIGHTS
# ==============================================================
print("\n================================================")
print("                PROJECT INSIGHTS")
print("================================================\n")
print("1. Unemployment rates changed across regions.")
print("2. Rural and Urban areas showed different trends.")
print("3. Labour participation varied significantly.")
print("4. Some regions had higher employment levels.")
print("5. Monthly unemployment trends changed over time.")
print("\n================================================")
print("       PROJECT EXECUTED SUCCESSFULLY")
print("================================================")