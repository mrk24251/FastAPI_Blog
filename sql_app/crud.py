from . import models,schemas
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from fastapi import FastAPI,HTTPException,Depends, status
from sqlalchemy.orm import Session

# def get_punish(db: Session, punish_id: int):
#     return db.query(models.Punish).filter(models.Punish.id == punish_id).first()
#
# def get_punish_by_value(db: Session, value: int):
#     punish_size = value
#     punish_set =[]
#     while punish_size >0:
#         length = len(db.query(models.Punish).filter(models.Punish.value <= punish_size).all())
#         i = randrange(length)
#         rand_punish=db.query(models.Punish).filter(models.Punish.value <= punish_size)[i]
#         punish_set.append(rand_punish)
#         punish_size -= rand_punish.value
#
#     return punish_set
#
#
# def get_punishes(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Punish).offset(skip).limit(limit).all()
#
#
# def create_punish(db: Session, punish: schemas.PunishCreate):
#     db_punish = models.Punish(task=punish.task, value=punish.value)
#     db.add(db_punish)
#     db.commit()
#     db.refresh(db_punish)
#     return db_punish


# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

#Authentication & Authorization
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

SECRET_KEY = "65a204161686f1adcc2742b262d75d1c9db70cafc2a4340489fcca460e687a64"
ALGORITHM = "HS256"

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_posts(db: Session):
    return db.query(models.Post).all()

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def create_user_post(db: Session, post: schemas.PostCreate, user_id: int):
    db_post = models.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return schemas.UserInDB(**user_dict)


#
def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
#
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(db: Session,token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(db, token)
    return user
#
async def get_current_user(db: Session,token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
