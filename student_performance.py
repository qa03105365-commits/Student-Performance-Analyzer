"""
Student Performance Analyzer
A small Data Science project using Python, Pandas, and Matplotlib.

Install dependencies:
    pip install pandas matplotlib

Run:
    python student_performance.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path("students.csv")
OUTPUT_FILE = Path("student_report.csv")
CHART_FILE = Path("average_marks.png")

# Sample dataset: replace or extend these records with your own data.
SAMPLE_DATA = [
    {"Name": "Ali", "Math": 85, "English": 78, "Computer": 92},
    {"Name": "Sara", "Math": 95, "English": 88, "Computer": 96},
    {"Name": "Ahmed", "Math": 62, "English": 70, "Computer": 68},
    {"Name": "Ayesha", "Math": 76, "English": 82, "Computer": 89},
    {"Name": "Bilal", "Math": 48, "English": 55, "Computer": 60},
]


def load_data() -> pd.DataFrame:
    """Load student data from CSV, or create a sample CSV on first run."""
    if not DATA_FILE.exists():
        pd.DataFrame(SAMPLE_DATA).to_csv(DATA_FILE, index=False)
        print(f"Created sample dataset: {DATA_FILE}")
    return pd.read_csv(DATA_FILE)


def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total, average, and pass/fail for each student."""
    subjects = ["Math", "English", "Computer"]

    required_columns = ["Name"] + subjects
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required CSV columns: {', '.join(missing)}")

    for subject in subjects:
        df[subject] = pd.to_numeric(df[subject], errors="raise")

    if df[subjects].isna().any().any():
        raise ValueError("Marks cannot be empty.")
    if ((df[subjects] < 0) | (df[subjects] > 100)).any().any():
        raise ValueError("Marks must be between 0 and 100.")

    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = df[subjects].mean(axis=1).round(2)
    df["Status"] = df[subjects].ge(50).all(axis=1).map(
        {True: "Pass", False: "Fail"}
    )
    return df


def create_chart(df: pd.DataFrame) -> None:
    """Save a bar chart showing each student's average marks."""
    plt.figure(figsize=(8, 5))
    plt.bar(df["Name"], df["Average"])
    plt.title("Student Average Marks")
    plt.xlabel("Student")
    plt.ylabel("Average Marks (%)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    plt.close()


def main() -> None:
    try:
        students = analyze_data(load_data())
        students.to_csv(OUTPUT_FILE, index=False)
        create_chart(students)

        topper = students.loc[students["Average"].idxmax()]
        print("\n=== Student Performance Report ===")
        print(students[["Name", "Total", "Average", "Status"]].to_string(index=False))
        print(f"\nClass topper: {topper['Name']} ({topper['Average']}%)")
        print(f"Pass count: {(students['Status'] == 'Pass').sum()}")
        print(f"Fail count: {(students['Status'] == 'Fail').sum()}")
        print(f"\nSaved report: {OUTPUT_FILE}")
        print(f"Saved chart:  {CHART_FILE}")
    except (ValueError, KeyError) as error:
        print(f"Could not analyze the data: {error}")


if __name__ == "__main__":
    main()
