from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    name : str = "godxritik" # setting default value for name field
    age: Optional[int] = None
    email: EmailStr    # we can also validate email using pydantic
    cgpa: float = Field(gt=0, le=10)

new_student = {"name" : "Ritik", "age" : "33", "email" : "xyz@example.in", "cgpa" : 10}

student = Student(**new_student)

print(student)
print(dict(student))
print(student.model_dump_json())
