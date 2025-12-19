from datetime import datetime, timedelta
from typing import Optional, Dict

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

# Secret for signing JWTs (in prod, use env var)
SECRET_KEY = "dev-secret-key-change-me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# In-memory user store for demo. Structure: email -> {name, email, hashed_password, role}
users_db: Dict[str, Dict] = {}


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(email: str, password: str):
    user = users_db.get(email)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = users_db.get(email)
    if user is None:
        raise credentials_exception
    return user


def require_role(role: str):
    def role_checker(current_user=Depends(get_current_user)):
        if current_user.get("role") != role:
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return current_user

    return role_checker


# Seeder: add a default admin and a demo student
def seed_users():
    if "admin@mergington.edu" not in users_db:
        users_db["admin@mergington.edu"] = {
            "name": "Admin User",
            "email": "admin@mergington.edu",
            "hashed_password": get_password_hash("adminpass"),
            "role": "admin",
        }
    if "student@mergington.edu" not in users_db:
        users_db["student@mergington.edu"] = {
            "name": "Demo Student",
            "email": "student@mergington.edu",
            "hashed_password": get_password_hash("studentpass"),
            "role": "student",
        }
