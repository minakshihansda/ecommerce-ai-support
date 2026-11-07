from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username="postgres",
    password="maino006@",
    host="localhost",
    port=5432,
    database="ecommerce_db"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)