import sqlite3
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
db_path = project_dir / "data" / "university.db"
schema_path = project_dir / "data" / "schema.sql"

conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON")

with open(schema_path, "r", encoding="utf-8") as file:
    conn.executescript(file.read())

# Students data
students = [
    (1, "Maya Hassan", 19, "Computer Science"),
    (2, "Omar Nasser", 21, "Engineering"),
    (3, "Lina Saleh", 20, "Biology"),
    (4, "Karim Farouk", 22, "Business"),
    (5, "Nour Hassan", 18, "Mathematics"),
    (6, "Youssef Adel", 23, "Physics"),
    (7, "Salma Ibrahim", 20, "English"),
    (8, "Adam Mahmoud", 19, "Computer Science"),
    (9, "Farah Nasser", 21, "Chemistry"),
    (10, "Ziad Mostafa", 24, "Engineering"),
    (11, "Jana Khalil", 18, "Biology"),
    (12, "Amir Saad", 22, "Economics"),
    (13, "Hana Fawzy", 20, "Mathematics"),
    (14, "Tarek Amin", 23, "History"),
    (15, "Mariam Hassan", 19, "Computer Science"),
    (16, "Ali Mansour", 21, "Physics"),
    (17, "Dina Samir", 20, "Business"),
    (18, "Seif Galal", 22, "Chemistry"),
    (19, "Rana Younis", 18, "English"),
    (20, "Fady Kamal", 24, "Engineering"),
    (21, "Leila Nasser", 19, "Biology"),
    (22, "Hassan Taha", 21, "Economics"),
    (23, "Mina George", 20, "Mathematics"),
    (24, "Yara Reda", 23, "History"),
    (25, "Bassem Lotfy", 22, "Computer Science"),
    (26, "Nada Ibrahim", 18, "Physics"),
    (27, "Ehab Shaker", 24, "Business"),
    (28, "Reem Ashraf", 20, "Chemistry"),
    (29, "Khaled Sameh", 21, "English"),
    (30, "Aya Medhat", 19, "Engineering"),
    (31, "Peter Nabil", 20, "Biology"),
    (32, "Mona Ezzat", 22, "Economics"),
    (33, "Sherif Wael", 18, "Mathematics"),
    (34, "Dalia Rami", 23, "History"),
    (35, "Hadi Emad", 21, "Computer Science"),
]

# Courses data
courses = [
    (1, "Introduction to Programming", 3),
    (2, "Data Structures", 4),
    (3, "General Biology", 3),
    (4, "Principles of Economics", 3),
    (5, "Calculus I", 4),
    (6, "Classical Mechanics", 4),
    (7, "Academic Writing", 2),
    (8, "Organic Chemistry", 4),
    (9, "Marketing Fundamentals", 3),
    (10, "World History", 3),
    (11, "Database Systems", 3),
    (12, "Electrical Circuits", 4),
    (13, "Genetics", 3),
    (14, "Business Statistics", 3),
    (15, "Linear Algebra", 3),
    (16, "Modern Physics", 4),
    (17, "Literature and Society", 3),
    (18, "Environmental Chemistry", 3),
    (19, "Financial Accounting", 3),
    (20, "Modern Middle East", 3),
    (21, "Web Development", 3),
    (22, "Microeconomics", 3),
    (23, "Probability", 3),
    (24, "Cell Biology", 3),
    (25, "Digital Logic", 4),
    (26, "Professional Communication", 2),
    (27, "Entrepreneurship", 3),
    (28, "Statistics for Science", 3),
    (29, "Ethics in Technology", 2),
    (30, "Research Methods", 3),
    (31, "Calculus II", 4),
    (32, "Thermodynamics", 4),
    (33, "Introduction to Psychology", 3),
    (34, "Public Speaking", 2),
    (35, "Project Management", 3),
]

# Enrollment -> (student_id, course_id) -> 40
pairs = [
    (1, 1), (1, 2), (2, 1), (2, 11), (3, 3), (3, 13),
    (4, 4), (4, 19), (5, 5), (5, 15), (6, 6), (6, 16),
    (7, 7), (7, 17), (8, 1), (8, 21), (9, 8), (9, 18),
    (10, 12), (10, 25), (11, 3), (11, 24), (12, 22), (12, 14),
    (13, 5), (13, 23), (14, 10), (14, 20), (15, 2), (15, 29),
    (16, 6), (16, 32), (17, 9), (17, 27), (18, 8), (18, 28),
    (19, 7), (19, 26), (20, 12), (20, 35),
]

enrollments = [
    (i, student, course, f"2026-{(i % 8) + 1:02d}-15")
    for i, (student, course) in enumerate(pairs, 1)
]

# Grades values for the enrolled students, with some None values to represent missing grades
values = [88.5, 76.0, 91.5, 83.0, None, 72.5, 95.0, 68.0, 87.0, 79.5]

grades = []
for i in range(1, 41):
    grade = values[(i - 1) % len(values)]
    grades.append((i, i, grade)) # (grade_id, enrollment_id, grade)


# Insert data into tables
conn.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", students)
conn.executemany("INSERT INTO courses VALUES (?, ?, ?)", courses)
conn.executemany("INSERT INTO enrollments VALUES (?, ?, ?, ?)", enrollments)
conn.executemany("INSERT INTO grades VALUES (?, ?, ?)", grades)

conn.commit()
conn.close()

print("Database created successfully!")
