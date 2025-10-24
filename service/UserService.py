from models.User import User
from db.Database import SessionLocal


def save_user(name, email):
    session = SessionLocal()
    try:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        print(f"✅ Saved user: {user}")
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
    finally:
        session.close()
