from fastapi import Response
from models.student_model import CreateStudent, Student

students = []
next_id = 1


async def create_student_controller(student: CreateStudent, response: Response):
    global next_id

    try:
        new_student = Student(
            id=next_id,
            name=student.name,
            email=student.email,
            course=student.course,
            semester=student.semester
        )

        students.append(new_student)
        next_id += 1

        response.status_code = 201
        return {
            "status": "success",
            "message": "Student created successfully",
            "data": new_student
        }

    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "status": "error",
            "message": "Error creating student"
        }


async def get_students_controller(response: Response):
    try:
        response.status_code = 200
        return {
            "status": "success",
            "message": "Students retrieved successfully",
            "data": students
        }

    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "status": "error",
            "message": "Error retrieving students"
        }


async def get_student_by_id_controller(student_id: int, response: Response):
    try:
        for student in students:
            if student.id == student_id:
                response.status_code = 200
                return {
                    "status": "success",
                    "message": "Student retrieved successfully",
                    "data": student
                }

        response.status_code = 404
        return {
            "status": "error",
            "message": "Student not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "status": "error",
            "message": "Error retrieving student"
        }


async def update_student_controller(student_id: int, student: CreateStudent, response: Response):
    try:
        for i in range(len(students)):
            if students[i].id == student_id:
                updated_student = Student(
                    id=student_id,
                    name=student.name,
                    email=student.email,
                    course=student.course,
                    semester=student.semester
                )

                students[i] = updated_student

                response.status_code = 200
                return {
                    "status": "success",
                    "message": "Student updated successfully",
                    "data": updated_student
                }

        response.status_code = 404
        return {
            "status": "error",
            "message": "Student not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "status": "error",
            "message": "Error updating student"
        }


async def delete_student_controller(student_id: int, response: Response):
    try:
        for i in range(len(students)):
            if students[i].id == student_id:
                students.pop(i)

                response.status_code = 204
                return

        response.status_code = 404
        return {
            "status": "error",
            "message": "Student not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500
        return {
            "status": "error",
            "message": "Error deleting student"
        }