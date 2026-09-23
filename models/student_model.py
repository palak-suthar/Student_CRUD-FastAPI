from pydantic import BaseModel, EmailStr

class CreateStudent(BaseModel):
    name: str
    email: EmailStr
    course: str
    semester: int

class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
    course: str
    semester: int