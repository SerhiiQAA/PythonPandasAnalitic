import os

project_name = "csv_pandas_project"
os.makedirs(project_name, exist_ok=True)

files = {
    f"{project_name}/data.csv": "name,age,score\nAlice,30,85\nBob,25,90\nCharlie,35,78\nDiana,28,92\n",
    f"{project_name}/analysis.py": """import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("data.csv")

    print("📊 First rows:")
    print(df.head())

    print("\\n📈 Descriptive statistics:")
    print(df.describe())

    print("\\n🧩 Missing values:")
    print(df.isnull().sum())

    high_scores = df[df["score"] > 85]
    print("\\n🏅 Participants with score > 85:")
    print(high_scores)

    sorted_df = df.sort_values(by="score", ascending=False)
    print("\\n🔽 Sorted by score (descending):")
    print(sorted_df)

    sorted_df.to_csv("sorted_results.csv", index=False)
    print("\\n💾 Saved to 'sorted_results.csv'")

    plt.bar(df["name"], df["score"], color="skyblue")
    plt.title("Participant Scores")
    plt.xlabel("Name")
    plt.ylabel("Score")
    plt.tight_layout()
    plt.savefig("score_chart.png")
    plt.show()

if __name__ == "__main__":
    main()
""",
    f"{project_name}/requirements.txt": "pandas\nmatplotlib\n",
    f"{project_name}/README.md": "# CSV Analysis Project\n\nBasic analysis using Pandas and Matplotlib.\n\nRun with:\n\n```bash\npython analysis.py\n```"
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Project '{project_name}' has been created successfully.")