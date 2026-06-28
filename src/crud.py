from sqlalchemy.orm import Session
from passlib.context import CryptContext

from . import models, schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    profile = models.Profile(user_id=db_user.id)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return db_user


def create_user_profile(db: Session, user_id: int, profile_data: schemas.ProfileCreate):
    profile = db.query(models.Profile).filter(models.Profile.user_id == user_id).first()
    if not profile:
        profile = models.Profile(user_id=user_id)
        db.add(profile)
        db.commit()
        db.refresh(profile)

    for key, value in profile_data.dict(exclude_none=True).items():
        setattr(profile, key, value)

    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def get_user_profile(db: Session, user_id: int):
    return db.query(models.Profile).filter(models.Profile.user_id == user_id).first()
