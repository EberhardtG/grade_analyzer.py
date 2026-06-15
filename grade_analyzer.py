# Grade Analyzer
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

print("===Grade Analyzer===")
# Calculate basic statistics
total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)
passing = sum(1 for score in scores if score >= 60)
failing = sum(1 for score in scores if score < 60)

print(f"Total Scores: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Passing Scores: {passing}")
print(f"Failing Scores: {failing}")

grade_distribution = {
    "A": sum(1 for score in scores if score >= 90),
    "B": sum(1 for score in scores if 80 <= score < 90),
    "C": sum(1 for score in scores if 70 <= score < 80),
    "D": sum(1 for score in scores if 60 <= score < 70),
    "F": sum(1 for score in scores if score < 60)
}

print("Grade Distribution:")
for grade, count in grade_distribution.items():
    print(f"  {grade}: {count} students")


if input("would you like to add a new score? (y/n): ").lower() == "y":
    new_score = int(input("Enter the new score: "))
    scores.append(new_score)
    print("Score added successfully!")
    print(f"New score added: {new_score}")
    print(f"Updated average: {sum(scores) / len(scores):.1f}")
else:  print("No score added.")
print(f"Final average: {sum(scores) / len(scores):.1f}")


while True:
        if input("Would you like to add another score? (y/n): ").lower() == "y":
            new_score = int(input("Enter the new score: "))
            scores.append(new_score)
            print("Score added successfully!")
            print(f"New score added: {new_score}")
            print(f"Updated average: {sum(scores) / len(scores):.1f}")
        else:
            print("No more scores to add.")
            print(f"Final average: {sum(scores) / len(scores):.1f}")
            break
        