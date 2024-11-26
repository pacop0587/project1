from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from app.v1.utils.db import engine, get_db
from app.v1.schema.user_schemas import UserResponse
from app.v1.model import user_model
from app.v1.model.user_model import User

app = FastAPI()

user_model.Base.metadata.create_all(bind=engine)

@app.get('/')
def home():
    return {"message": "Hello, World!"} 

@app.get('/users', status_code = status.HTTP_200_OK, response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    all_users = db.query(User).all()
    return all_users