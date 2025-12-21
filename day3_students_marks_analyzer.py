def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >=80:
        return "A"
    elif avg >=70:
        return "B"
    elif avg >=60:
        return "C"
    elif avg >=50:
        return "D"
    else:
        return "F"

students = []

n = int(input("Enter number of students :"))

for i in range(n):
    print(f"\nStudent {i+1}")
    name = input("Enter name: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for j in range(subjects):
        mark = float(input(f"Enter marks for subject {j+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total/subjects
    grade = calculate_grade(average)

    students.append({
        "name":name,
        "marks":marks,
        "total":total,
        "average":average,
        "grade":grade,
    })

print("\n--- Student Performance Report ---")
for s in students:
    print(f"\nName: {s['name']}")
    print(f"\nMarks: {s['marks']}")
    print(f"\nTotal: {s['total']}")
    print(f"\nAverage: {s['average']}")
    print(f"\nGrade: {s['grade']}")

averages = [s["average"] for s in students]
print("\nClass Statistics:")
print("Highes Average:",max(averages))
print("Lowest Average:",min(averages))
print("Class Average:",sum(averages)/len(averages))
