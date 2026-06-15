# 📊 Grade Analyzer

A command-line Grade Analyzer built with Python that calculates key academic statistics, evaluates student performance, and allows users to add new scores dynamically while updating results in real time.

This project demonstrates core Python programming concepts including lists, loops, conditional logic, dictionaries, user input handling, and basic data analysis.

---

## 📌 Overview

The Grade Analyzer processes a collection of student scores and provides useful insights such as:

* Total score accumulation
* Class average
* Highest and lowest scores
* Number of passing and failing grades
* Grade distribution by letter grade
* Dynamic score entry and recalculation

The application serves as a practical example of how Python can be used to analyze and summarize data.

---

## 🚀 Features

### 📈 Statistical Analysis

Calculates:

* Total of all scores
* Average score
* Highest score
* Lowest score

Example:

```text
Total Scores: 1126
Average: 75.1
Highest: 100
Lowest: 38
```

---

### ✅ Pass / Fail Analysis

Categorizes student performance based on a passing score of 60.

Displays:

* Number of passing students
* Number of failing students

Example:

```text
Passing Scores: 12
Failing Scores: 3
```

---

### 🏆 Grade Distribution

Groups scores into traditional letter grades:

| Grade | Range    |
| ----- | -------- |
| A     | 90–100   |
| B     | 80–89    |
| C     | 70–79    |
| D     | 60–69    |
| F     | Below 60 |

Example output:

```text
Grade Distribution:
A: 4 students
B: 4 students
C: 3 students
D: 2 students
F: 2 students
```

---

### ➕ Dynamic Score Entry

Users can:

* Add new scores
* View updated averages immediately
* Continue entering scores until finished

Example:

```text
Would you like to add a new score? (y/n): y
Enter the new score: 95

Score added successfully!
Updated average: 76.4
```

---

## 🧠 Concepts Demonstrated

This project reinforces several foundational Python concepts:

### Data Structures

* Lists
* Dictionaries

### Built-In Functions

* `sum()`
* `max()`
* `min()`
* `len()`

### Control Flow

* `if / else`
* `while` loops

### User Input

* `input()`
* Dynamic data updates

### Iteration

* `for` loops
* Dictionary iteration with `.items()`

### Data Analysis

* Aggregation
* Categorization
* Statistical calculations

---

## 🏗️ Project Structure

```text
grade_analyzer.py
```

---

## ⚙️ How It Works

### Step 1: Load Scores

The program begins with a predefined list of scores.

```python
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
```

---

### Step 2: Calculate Statistics

The application calculates:

```python
total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)
```

---

### Step 3: Build Grade Distribution

A dictionary is used to count students in each grade category.

```python
grade_distribution = {
    "A": ...,
    "B": ...,
    "C": ...,
    "D": ...,
    "F": ...
}
```

---

### Step 4: Accept New Scores

Users can continuously add scores.

Each new score:

* Updates the list
* Recalculates the average
* Provides immediate feedback

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone https://github.com/yourusername/grade-analyzer.git
```

### Navigate to the Project Folder

```bash
cd grade-analyzer
```

### Run the Program

```bash
python grade_analyzer.py
```

---

## 📋 Example Output

```text
=== Grade Analyzer ===

Total Scores: 1126
Average: 75.1
Highest: 100
Lowest: 38
Passing Scores: 12
Failing Scores: 3

Grade Distribution:
A: 4 students
B: 3 students
C: 3 students
D: 2 students
F: 3 students

Would you like to add a new score? (y/n): y
Enter the new score: 96

Score added successfully!
Updated average: 76.4
```

---

## 🔮 Future Enhancements

Potential improvements include:

* Input validation using `try/except`
* Score removal functionality
* Student names associated with grades
* Median and mode calculations
* GPA conversion
* Data persistence using JSON or CSV files
* Graphical charts and visualizations
* Export reports to Excel or PDF
* Class-based (OOP) implementation

---

## 👨‍💻 Author

**Grant Eberhardt**

Software Engineer focused on building practical projects with Python, JavaScript, Git, and REST APIs while developing solutions that demonstrate problem-solving, data processing, and application design skills.

---

## 📈 Skills Demonstrated

* Python Programming
* Data Analysis Fundamentals
* User Input Handling
* Data Structures
* Control Flow Logic
* Statistical Calculations
* Program Design and Organization

This project highlights the ability to transform raw data into meaningful insights while creating an interactive user experience through Python.
