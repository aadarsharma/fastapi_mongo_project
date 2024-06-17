from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema):
        schema.update(type='string')

class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: str
    password: str

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}

class LoginModel(BaseModel):
    email: str
    password: str

class LinkIDModel(BaseModel):
    user_id: str
    linked_id: str
