from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.controllers.employee_controller import get_employee_controller
from app.db.session import get_db
from app.schemas.emplyee_schema import EmployeeResponseModel

router = APIRouter()


@router.get("/employee", response_model=list[EmployeeResponseModel])
def get_employee(db: Session = Depends(get_db)):
    return get_employee_controller(db)
