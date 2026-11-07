# Student Performance Analyzer

A small Data Science project that analyzes student marks using **Python, Pandas, and Matplotlib**.

## Features
- Calculates total and average marks for each student.
- Assigns Pass/Fail status (a student must score at least 50 in every subject to pass).
- Finds the class topper.
- Saves an analysis report as `student_report.csv`.
- Creates a bar chart named `average_marks.png`.

## Requirements
- Python 3.9+
- pandas
- matplotlib

Install the libraries:

```bash
pip install pandas matplotlib
```

## Run the project

```bash
python student_performance.py
```

On the first run, the program creates a sample `students.csv` file automatically.

## Use your own data

Edit `students.csv` and keep these column names:

```csv
Name,Math,English,Computer
Ali,85,78,92
Sara,95,88,96
```

Marks must be between 0 and 100.

## Project structure

```text
Student-Performance-Analyzer/
├── student_performance.py
├── README.md
└── .gitignore
```

The CSV report and chart are generated when you run the program.

## Skills demonstrated
Python • Pandas • Data Cleaning • Exploratory Data Analysis • Matplotlib • CSV Handling

## Author
QaisarKhan
