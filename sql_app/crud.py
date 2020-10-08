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

SECRET_KEY = "cdca8fd40b869304cbeeefda374eb43e80da654536996e5b5c802c308005f0ae"
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

def create_user_post(db: Session, user_id: int, url:str, title:str, body: str,):
    db_post = models.Post(title= title, body= body, owner_id=user_id,url=url)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db,username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    return user

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
# async def get_current_active_user(current_user = Depends(get_current_user)):
#     return current_user.username

#comment
# def create_post_comment(db: Session, comment: schemas.CommentBase, user_id: int):
#     db_post = models.Post(**post.dict(), owner_id=user_id)
#     db.add(db_post)
#     db.commit()
#     db.refresh(db_post)
#     return db_post

def create_post_comment(db: Session, comment: schemas.CommentBase, post_id: int):
    db_comment = models.Comment(**comment.dict(), post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment