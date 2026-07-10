from fastapi import FastAPI, HTTPException, status, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from models import Course, Student, Enrollment
from schemas import *
from database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Management API",
    description="FastAPI CRUD with Courses, Students, Enrollments",
    version="1.0.0"
)

# ---------------- Background Task ----------------
def send_confirmation_email(email: str):
    print(f"Sending confirmation to {email}")

# ---------------- COURSES ----------------

@app.post("/api/courses/", response_model=CourseResponse,
          status_code=status.HTTP_201_CREATED,
          tags=["Courses"])
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    obj = Course(**course.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/api/courses/", response_model=list[CourseResponse], tags=["Courses"])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()


@app.put("/api/courses/{id}", response_model=CourseResponse, tags=["Courses"])
def update_course(id: int, course: CourseCreate, db: Session = Depends(get_db)):
    obj = db.query(Course).filter(Course.id == id).first()
    if not obj:
        raise HTTPException(404, "Course not found")

    for k, v in course.dict().items():
        setattr(obj, k, v)

    db.commit()
    db.refresh(obj)
    return obj


@app.delete("/api/courses/{id}", status_code=204, tags=["Courses"])
def delete_course(id: int, db: Session = Depends(get_db)):
    obj = db.query(Course).filter(Course.id == id).first()
    if not obj:
        raise HTTPException(404, "Course not found")

    db.delete(obj)
    db.commit()
    return None

# ---------------- STUDENTS ----------------

@app.post("/api/students/", response_model=StudentResponse, tags=["Students"])
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    obj = Student(**student.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@app.get("/api/students/", response_model=list[StudentResponse], tags=["Students"])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# ---------------- ENROLLMENTS ----------------

@app.post("/api/enrollments/", status_code=201, tags=["Enrollments"])
def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    obj = Enrollment(**enrollment.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)

    student = db.query(Student).filter(Student.id == enrollment.student_id).first()

    background_tasks.add_task(send_confirmation_email, student.email)

    return obj


@app.get("/api/courses/{id}/students/", tags=["Courses"])
def get_course_students(id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == id).first()
    if not course:
        raise HTTPException(404, "Course not found")

    return db.query(Student).join(Enrollment).filter(
        Enrollment.course_id == id
    ).all()