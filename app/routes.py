from fastapi import APIRouter, HTTPException, Depends
from app.models import User, LoginModel, LinkIDModel
from app.database import db
from pydantic import BaseModel
from bson import ObjectId
from passlib.context import CryptContext

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserIn(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register", response_model=User)
async def register_user(user_in: UserIn):
    user_in.password = pwd_context.hash(user_in.password)
    user_dict = user_in.dict()
    user_dict["_id"] = str(ObjectId())
    db.users.insert_one(user_dict)
    return User(**user_dict)

@router.post("/login")
async def login_user(login: LoginModel):
    user = db.users.find_one({"email": login.email})
    if not user or not pwd_context.verify(login.password, user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful", "user": User(**user)}

@router.post("/link_id")
async def link_id(link_id_model: LinkIDModel):
    result = db.users.update_one(
        {"_id": link_id_model.user_id},
        {"$set": {"linked_id": link_id_model.linked_id}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "ID linked successfully"}

@router.get("/user_with_linked_id/{user_id}")
async def get_user_with_linked_id(user_id: str):
    user = db.users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    linked_data = db.linked_data.find_one({"linked_id": user.get("linked_id")})
    if not linked_data:
        raise HTTPException(status_code=404, detail="Linked data not found")
    
    return {"user": user, "linked_data": linked_data}

@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: str):
    user = db.users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    linked_id = user.get("linked_id")
    if linked_id:
        db.linked_data.delete_one({"linked_id": linked_id})
    
    db.users.delete_one({"_id": user_id})
    return {"message": "User and associated data deleted successfully"}

