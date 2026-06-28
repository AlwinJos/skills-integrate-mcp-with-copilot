from pydantic import BaseModel, EmailStr
from typing import Optional


class ProfileBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: Optional[str] = "Member"
    github_username: Optional[str] = None
    gitlab_username: Optional[str] = None
    telegram_username: Optional[str] = None
    discord_username: Optional[str] = None
    twitter_username: Optional[str] = None
    bio: Optional[str] = None
    skills: Optional[str] = None
    work_experience: Optional[str] = None
    education: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    profile: Optional[Profile] = None

    class Config:
        orm_mode = True
