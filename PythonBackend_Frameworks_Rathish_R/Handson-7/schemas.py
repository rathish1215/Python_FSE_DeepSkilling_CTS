from pydantic import BaseModel

class CourseCreate(BaseModel):
    name: str
    description: str

class CourseResponse(CourseCreate):
    id: int
    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    name: str
    email: str

class StudentResponse(StudentCreate):
    id: int
    class Config:
        orm_mode = True


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int