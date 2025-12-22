from sqlalchemy.orm import Session
from app.models.users import User
from app.schemas.users import *
from fastapi import APIRouter, HTTPException, status, Depends
from app.utils.jwt_handler import *

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user:LoginCreate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Invalid email or password")
    
    token = access_token({"sub":db_user.email})
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/register", response_model=UserOut)
def register(user:UserCreate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Email Already Exists")
    
    if not user.email.endswith("@gmail.com"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Email Must be Ends with @gmail.com")
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/me", response_model=UserOut)
def exact_user(current_user:User = Depends(get_current_user)):
    return current_user