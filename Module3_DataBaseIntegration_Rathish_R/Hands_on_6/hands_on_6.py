from models import Course, Department, Enrollment, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

DATABASE_URL = "postgresql+psycopg2://postgres:{your_password}@localhost/college_db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# TASK 1 : INSERT DATA

cs = Department(
    dept_name="Computer Science",
    head_of_dept="Dr Kumar",
    budget=900000
)

ece = Department(
    dept_name="Electronics",
    head_of_dept="Dr Priya",
    budget=600000
)

session.add_all([cs, ece])
session.commit()

students = [
    Student(
        first_name="Rahul",
        last_name="Kumar",
        email="rahul@gmail.com",
        enrollment_year=2022,
        department=cs
    ),
    Student(
        first_name="Anu",
        last_name="Sharma",
        email="anu@gmail.com",
        enrollment_year=2023,
        department=cs
    ),
    Student(
        first_name="Vijay",
        last_name="Raj",
        email="vijay@gmail.com",
        enrollment_year=2022,
        department=ece
    )
]

session.add_all(students)
session.commit()

courses = [
    Course(
        course_name="Database Management System",
        course_code="CS201",
        credits=4
    ),
    Course(
        course_name="Operating System",
        course_code="CS202",
        credits=3
    )
]

session.add_all(courses)
session.commit()

enrollments = [
    Enrollment(
        student_id=1,
        course_id=1,
        grade="A"
    ),
    Enrollment(
        student_id=2,
        course_id=1,
        grade="B"
    ),
    Enrollment(
        student_id=3,
        course_id=2,
        grade="A"
    )
]

session.add_all(enrollments)
session.commit()

print("Inserted Successfully")

# TASK 2 : READ USING ORM

enrollments = session.query(Enrollment).all()

for e in enrollments:
    print(
        e.student.first_name,
        e.student.last_name,
        e.course.course_name
    )

# TASK 3 : UPDATE

student = session.query(Student).filter(
    Student.email == "rahul@gmail.com"
).first()

student.enrollment_year = 2024

session.commit()

print("Updated Successfully")

# TASK 4 : DELETE

enrollment = session.query(Enrollment).first()

session.delete(enrollment)

session.commit()

print("Deleted Successfully")

# TASK 5 : N+1 PROBLEM SOLUTION USING JOINEDLOAD

enrollments = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for e in enrollments:
    print(
        e.student.first_name,
        e.student.last_name,
        e.course.course_name
    )

"""
N+1 ANALYSIS

Without joinedload:

1 query fetches enrollments
N queries fetch students
N queries fetch courses

Example:

10000 enrollments:

1 + 10000 + 10000
= 20001 queries

After joinedload:

Only 1 optimized query runs.

Benefits:
- Removes N+1 problem
- Faster execution
- Less database requests
- Better performance
"""

session.close()
