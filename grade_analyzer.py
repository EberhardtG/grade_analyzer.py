# Grade Analyzer

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

print("=== Grade Analyzer ===")

# Calculate basic statistics
score_sum = sum(scores)
average = score_sum / len(scores)
highest = max(scores)
lowest = min(scores)

# Grade category counters
a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

passing = 0
failing = 0

# Single loop for categorizing scores
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

    if score >= 60:
        passing += 1
    else:
        failing += 1

# Percentages
passing_percent = (passing / len(scores)) * 100
failing_percent = (failing / len(scores)) * 100

# Output statistics
print(f"Total Scores: {len(scores)}")
print(f"Average Score: {average:.1f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")

print(f"Passing Scores: {passing} ({passing_percent:.1f}%)")
print(f"Failing Scores: {failing} ({failing_percent:.1f}%)")

print("\nGrade Distribution:")
print(f"A: {a_count} students")
print(f"B: {b_count} students")
print(f"C: {c_count} students")
print(f"D: {d_count} students")
print(f"F: {f_count} students")

print("\n--- Add More Scores ---")

while True:
    user_input = input("Enter a score (or 'done' to finish): ").lower()

    if user_input == "done":
        break

    try:
        new_score = int(user_input)

        if 0 <= new_score <= 100:
            scores.append(new_score)
            print("Score added successfully!")
            print(f"Updated average: {sum(scores) / len(scores):.1f}")
        else:
            print("Please enter a score between 0 and 100.")

    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

print(f"\nFinal Average: {sum(scores) / len(scores):.1f}")
print("Program complete.")
