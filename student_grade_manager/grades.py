student = {
    "Brian Kiprotich": 70,
    "Mary Muthuku": 60,
    "Stanley Oyoo": 82,
    "Brooks Buku": 90
}

# Calculate average
average_score = sum(student.values()) / len(student)
print(f"Average Score: {average_score:.2f}")

# Find top student
top_score = 0
top_student = ""

for name, score in student.items():
    if score > top_score:
        top_score = score
        top_student = name

# Convert name to uppercase
top_student = top_student.upper()

print(f"Top Student: {top_student} ({top_score})")