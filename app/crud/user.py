from sqlalchemy.orm import Session

from app.db.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user_data: UserCreate):
    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=user_data.password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_id(db: Session, user_id: int):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )