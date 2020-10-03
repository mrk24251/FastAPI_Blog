from typing import List,Optional
from datetime import datetime, timedelta
from fastapi import FastAPI,HTTPException,Depends, status
# from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
# @app.post("/punishes/", response_model=schemas.Punish)
# def create_punish(punish: schemas.PunishCreate, db: Session = Depends(get_db)):
#     return crud.create_punish(db=db, punish= punish)
#
# @app.get("/punishes/", response_model=List[schemas.Punish])
# def read_punish_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     punishes = crud.get_punishes(db, skip=skip, limit=limit)
#     return punishes
#
#
# @app.get("/punishes/{punish_id}", response_model=schemas.Punish)
# def read_punish(punish_id: int, db: Session = Depends(get_db)):
#     db_punish = crud.get_punish(db, punish_id=punish_id)
#     if db_punish is None:
#         raise HTTPException(status_code=404, detail="Punish not found")
#     return db_punish
#
# @app.post("/punish_by_value/", response_model=List[schemas.Punish])
# def read_punish_by_value(punish: schemas.PunishValue, db: Session = Depends(get_db)):
#     db_punish = crud.get_punish_by_value(db, value=punish.value)
#     return db_punish



# @app.post("/punishes/{punish_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items


## authentication and authorization
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# fake_users_db = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }

# @app.post("/punishes/", response_model=schemas.Punish)
# def create_punish(punish: schemas.PunishCreate, db: Session = Depends(get_db)):
#     return crud.create_punish(db=db, punish= punish)

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db=db,user=user)
    return db_user

@app.get("/posts/", response_model=List[schemas.Post])
def read_posts(db: Session = Depends(get_db)):
    items = crud.get_posts(db)
    return items

@app.get("/posts/{post_id}")
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    comments = db.query(models.Comment).filter(models.Comment.post_id == post_id)
    active_comments = comments.filter(models.Comment.is_active == True).all()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"db_post":db_post,"active_comments":active_comments}

@app.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(db: Session = Depends(get_db),token = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, crud.SECRET_KEY, algorithms=[crud.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = username
    except JWTError:
        raise credentials_exception
    user = crud.get_user(db, username=token_data)
    if user is None:
        raise credentials_exception
    return user

@app.post("/users/posts/", response_model=schemas.Post)
def create_post_for_user(
    post: schemas.PostCreate, db: Session = Depends(get_db) ,current_user = Depends(get_current_user)
):
    user_id = current_user.id
    return crud.create_user_post(db=db, post=post, user_id=user_id)

@app.post("/posts/{post_id}", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentBase , post_id: int, db: Session = Depends(get_db)):
    db_comment = crud.create_post_comment(db,comment= comment , post_id=post_id)

    return db_comment

@app.get("/users/me/",response_model=schemas.User)
async def read_users_me(current_user = Depends(get_current_user)):
    return current_user
