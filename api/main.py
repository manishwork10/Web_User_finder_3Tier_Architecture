from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.model import SessionLocal, User
from api.schemas import UserCreate, UserOut

app = FastAPI(title="UserService")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def root():
    return {"message": "User-Service API. Visit /docs for interactive docs."}

@app.post("/users", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username.lower().strip(),
                   phonenumber=user.phonenumber.strip())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{username}", response_model=UserOut)
def read_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username.lower().strip()).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user