#crud operation
from sqlalchemy.orm import Session
from app.models.employee import Employee

def get_employee(db:Session):
    employee=db.query(Employee).all()
    return employee