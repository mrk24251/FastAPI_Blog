from typing import List,Optional
from datetime import datetime, timedelta
from fastapi import FastAPI,HTTPException,Depends, status
# from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

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


# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(fake_users_db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}
#
#
# @app.get("/users/me")
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user