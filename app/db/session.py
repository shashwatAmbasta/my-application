from sqlalchemy.orm import sessionmaker,declarative_base

from app.db.database import engine

sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

