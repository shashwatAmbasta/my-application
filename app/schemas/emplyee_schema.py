from pydantic import BaseModel, ConfigDict, EmailStr, Field


class EmployeeRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    department: str = Field(..., min_length=1, max_length=100)
    salary: float = Field(..., gt=0)


class EmployeeResponseModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    department: str
    salary: float
