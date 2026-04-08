def get_grade(average):
    """Return grade based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"


def calculate_average(marks):
    """Calculate average from a list of marks."""
    if len(marks) != 5:
        raise ValueError("Exactly 5 subject marks are required.")
    if any(m < 0 or m > 100 for m in marks):
        raise ValueError("Marks must be between 0 and 100.")
    return sum(marks) / len(marks)


def main():
    print("=== Student Grade Calculator ===\n")
    subjects = ["Maths", "Science", "English", "History", "Computer Science"]
    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("  ⚠ Please enter a value between 0 and 100.")
            except ValueError:
                print("  ⚠ Invalid input. Please enter a number.")

    average = calculate_average(marks)
    grade = get_grade(average)

    print("\n--- Result ---")
    print(f"Average Marks : {average:.2f}")
    print(f"Grade         : {grade}")


if __name__ == "__main__":
    main()
