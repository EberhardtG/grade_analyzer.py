# 📊 Grade Analyzer

A command-line Grade Analyzer built with Python that calculates key academic statistics, categorizes student performance, and allows users to add new scores dynamically while updating results in real time.

This project demonstrates fundamental Python programming concepts including lists, loops, conditional logic, user input validation, and data analysis techniques.

---

# 📌 Overview

The Grade Analyzer processes a collection of student scores and provides useful insights such as:

- Total number of scores
- Class average
- Highest and lowest scores
- Passing and failing counts with percentages
- Grade distribution by letter grade
- Dynamic score entry with real-time updates
- Input validation and error handling

The project was created as a practice exercise focused on Python control flow using loops and conditional statements.

---

# 🚀 Features

## 📈 Statistical Analysis

Calculates:

- Total number of scores
- Average score
- Highest score
- Lowest score

Example:

```text
Total Scores: 15
Average Score: 74.7
Highest Score: 100
Lowest Score: 38
```

---

## ✅ Pass / Fail Analysis

Scores are evaluated using a passing threshold of 60.

Displays:

- Number of passing scores
- Number of failing scores
- Passing percentage
- Failing percentage

Example:

```text
Passing: 12 (80.0%)
Failing: 3 (20.0%)
```

---

## 🏆 Grade Distribution

Scores are categorized into traditional letter grades using a for loop and an if/elif decision structure.

| Grade | Score Range |
| ------- | ------- |
| A | 90-100 |
| B | 80-89 |
| C | 70-79 |
| D | 60-69 |
| F | Below 60 |

Example Output:

```text
Grade Distribution:
A: 4 students
B: 3 students
C: 3 students
D: 2 students
F: 3 students
```

---

## ➕ Dynamic Score Entry

Users can continuously add scores until they enter `done`.

Features:

- Adds scores to the existing list
- Updates averages immediately
- Validates score ranges
- Prevents crashes from invalid input

Example:

```text
--- Add More Scores ---

Enter a score (or 'done' to finish): 95

Score added successfully!
Updated average: 76.0
```

---

## 🛡️ Input Validation

The program uses exception handling to prevent crashes from invalid entries.

Examples:

```text
Enter a score (or 'done' to finish): abc
Invalid input. Please enter a number or 'done'.
```

```text
Enter a score (or 'done' to finish): 150
Score must be between 0 and 100.
```

---

# 🧠 Concepts Demonstrated

## Data Structures

- Lists

## Built-In Functions

- `sum()`
- `max()`
- `min()`
- `len()`

## Control Flow

- `if`
- `elif`
- `else`
- `for` loops
- `while` loops

## User Input

- `input()`
- Dynamic data updates

## Error Handling

- `try`
- `except ValueError`

## Data Analysis

- Aggregation
- Categorization
- Percentage calculations
- Performance analysis

---

# 🏗️ Project Structure

```text
grade_analyzer.py
README.md
```

---

# ⚙️ How It Works

## Step 1: Load Scores

The application begins with a predefined list of student scores.

```python
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
```

---

## Step 2: Calculate Statistics

The program calculates basic metrics.

```python
score_sum = sum(scores)
average = score_sum / len(scores)
highest = max(scores)
lowest = min(scores)
```

---

## Step 3: Categorize Scores

A single loop evaluates each score and places it into the appropriate letter-grade category.

```python
for score in scores:
    if score >= 90:
        a_count += 1
    elif score >= 80:
        b_count += 1
    elif score >= 70:
        c_count += 1
    elif score >= 60:
        d_count += 1
    else:
        f_count += 1
```

---

## Step 4: Add Additional Scores

The user may continue entering scores until typing:

```text
done
```

Each valid entry:

- Adds the score to the list
- Updates the average
- Provides immediate feedback

---

# ▶️ How to Run

## Run the Program

```bash
python grade_analyzer.py
```

---

# 📋 Example Output

```text
=== Grade Analyzer ===

Total Scores: 15
Average Score: 74.7
Highest Score: 100
Lowest Score: 38

Passing: 12 (80.0%)
Failing: 3 (20.0%)

Grade Distribution:
A: 4 students
B: 3 students
C: 3 students
D: 2 students
F: 3 students

--- Add More Scores ---

Enter a score (or 'done' to finish): 96

Score added successfully!
Updated average: 76.0

Enter a score (or 'done' to finish): done

Final Average: 76.0
Program complete.
```

---

# 🔮 Future Enhancements

Potential improvements:

- Median and mode calculations
- Score removal functionality
- Student names associated with grades
- GPA conversion
- Import scores from CSV files
- Export reports to CSV or Excel
- Data visualization with charts
- Object-Oriented Programming (OOP) implementation

---

# 👨‍💻 Author

**Grant Eberhardt**

Aspiring Software Developer focused on building practical Python applications while strengthening skills in problem solving, data analysis, APIs, automation, and software development best practices.

---

# 📈 Skills Demonstrated

- Python Programming
- Control Flow Logic
- Loops and Conditionals
- Input Validation
- Exception Handling
- Data Analysis Fundamentals
- User Interaction Design
- Program Organization

This project demonstrates the ability to analyze data, implement control flow structures, validate user input, and build an interactive command-line application using Python.
