from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.database import get_db
from app.models import Course
from app.schemas import CourseCreate

router = APIRouter(prefix="/api/courses", tags=["Courses"])


@router.post("/")
async def create_course(course: CourseCreate, db: AsyncSession = Depends(get_db)):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    return new_course


@router.get("/")
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: int | None = None,
    db: AsyncSession = Depends(get_db)
):
    query = select(Course)

    if department_id:
        query = query.where(Course.department_id == department_id)

    result = await db.execute(query.offset(skip).limit(limit))

    return result.scalars().all()


@router.get("/{course_id}")
async def get_course(course_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    return result.scalar_one_or_none()