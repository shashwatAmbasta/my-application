from sqlalchemy.orm import Session
from app.services.employee_service import get_employee

def get_employee_controller(db:Session):
    employee=get_employee(db)
    return employee