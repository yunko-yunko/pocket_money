from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db
import os

router = APIRouter()

# 템플릿 폴더는 app/templates 디렉토리로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "..", "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@router.post("/expenses", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)

@router.get("/expenses", response_class=HTMLResponse)
def view_expenses(request: Request, user_id: int, db: Session = Depends(get_db)):
    expenses = crud.get_expenses_by_user(db, user_id)
    return templates.TemplateResponse("expenses.html", {"request": request, "expenses": expenses})