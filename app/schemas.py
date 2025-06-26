from pydantic import BaseModel
from datetime import date, datetime

# User 관련 스키마
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

# Expense 관련 스키마
class ExpenseCreate(BaseModel):
    user_id: int
    amount: float
    expense_date: date
    reason: str

class ExpenseResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    expense_date: date
    reason: str
    created_at: datetime

    class Config:
        orm_mode = True