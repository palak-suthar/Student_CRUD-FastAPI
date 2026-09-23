from fastapi import APIRouter, Response
from models.student_model import CreateStudent
from controllers.student_controller import (
    create_student_controller,
    get_students_controller,
    get_student_by_id_controller,
    update_student_controller,
    delete_student_controller
)

router = APIRouter()


@router.post("/students")
async def create_student(student: CreateStudent, response: Response):
    return await create_student_controller(student, response)


@router.get("/students")
async def get_students(response: Response):
    return await get_students_controller(response)


@router.get("/students/{student_id}")
async def get_student_by_id(student_id: int, response: Response):
    return await get_student_by_id_controller(student_id, response)


@router.put("/students/{student_id}")
async def update_student(student_id: int, student: CreateStudent, response: Response):
    return await update_student_controller(student_id, student, response)


@router.delete("/students/{student_id}")
async def delete_student(student_id: int, response: Response):
    return await delete_student_controller(student_id, response)