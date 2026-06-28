from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from .db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    profile = relationship("Profile", back_populates="user", uselist=False)


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    role = Column(String, default="Member")
    github_username = Column(String, nullable=True)
    gitlab_username = Column(String, nullable=True)
    telegram_username = Column(String, nullable=True)
    discord_username = Column(String, nullable=True)
    twitter_username = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    skills = Column(Text, nullable=True)
    work_experience = Column(Text, nullable=True)
    education = Column(Text, nullable=True)
    resume_path = Column(String, nullable=True)
    profile_image_path = Column(String, nullable=True)
    cover_image_path = Column(String, nullable=True)

    user = relationship("User", back_populates="profile")
