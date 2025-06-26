from sqlalchemy.orm import Session
from app import models, schemas

# User 관련 함수
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Expense 관련 함수
def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(
        user_id=expense.user_id,
        amount=expense.amount,
        expense_date=expense.expense_date,
        reason=expense.reason
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses_by_user(db: Session, user_id: int):
    return db.query(models.Expense).filter(models.Expense.user_id == user_id).all()