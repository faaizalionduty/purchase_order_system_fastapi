from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.users import User
from app.config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def access_token(data: dict, expired_to: timedelta = timedelta(hours=1)):
    to_expired = data.copy()
    expire = datetime.utcnow() + expired_to
    to_expired.update({"exp": expire})
    return jwt.encode(to_expired, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise credentials_exception

    return user

def require_admin(current_user = Depends(get_current_user)):
    if current_user.role != "admin" and current_user.role != "lab_staff":
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return current_user

def require_roles(*roles):
    def checker(user=Depends(get_current_user)):
        if user["role"] not in roles:
            raise HTTPException(status_code=403, detail="Access denied")
        return user
    return checker
