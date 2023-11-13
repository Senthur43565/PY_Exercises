student1 = {
    'name': 'Alice',
    'grades': {
        'math': 90,
        'history': 85,
        'science': 88
    }
}

def calculate_average_grade(student):
    total = 0
    count = 0

    for subject, grade in student['grades'].items():
        total += grade
        count += 1

    if count == 0:
        return 0  # To avoid division by zero if there are no grades

    return total / count

average = calculate_average_grade(student1)
print(f"The average grade for {student1['name']} is {average:.4f}")
