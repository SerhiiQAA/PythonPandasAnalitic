import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Ensure charts folder exists
os.makedirs("charts", exist_ok=True)

# Load data
df = pd.read_csv("dou_data.csv")

# Basic info
print("📊 First rows:")
print(df.head())

print("\n📈 Descriptive statistics:")
print(df.describe())

# Top 10 companies by Overall rating
top10 = df.sort_values(by="Overall", ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x="Overall", y="Company", data=top10, palette="crest")
plt.title("🏆 Top 10 IT Employers in Ukraine (DOU Rating)")
plt.xlabel("Overall Rating")
plt.ylabel("Company")
plt.tight_layout()
plt.savefig("charts/top10_overall.png")
plt.close()

# Correlation heatmap
plt.figure(figsize=(10, 8))
corr = df.iloc[:, 3:].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("📊 Correlation Between Rating Categories")
plt.tight_layout()
plt.savefig("charts/category_correlation.png")
plt.close()

# Surveys vs Overall rating
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Surveys", y="Overall", hue="Group", data=df, palette="Set2", s=100)
plt.title("📈 Surveys vs Overall Rating")
plt.xlabel("Number of Surveys")
plt.ylabel("Overall Rating")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/surveys_vs_rating.png")
plt.close()

# Radar chart for a selected company
def plot_radar(company_name):
    company = df[df["Company"] == company_name].iloc[0]
    categories = ["Compensation", "Conditions", "Career", "Project", "CompanyScore", "Responsibility"]
    values = [company[cat] for cat in categories]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, color="blue", linewidth=2)
    ax.fill(angles, values, color="skyblue", alpha=0.4)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title(f"📌 {company_name} Rating Profile", y=1.1)
    ax.set_ylim(0, 100)
    plt.tight_layout()
    plt.savefig(f"charts/{company_name.lower().replace(' ', '_')}_radar.png")
    plt.close()

# Example: Genesis
plot_radar("Genesis")

print("✅ Analysis complete. Charts saved in 'charts/' folder.")
