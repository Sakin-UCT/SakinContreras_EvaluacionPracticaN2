from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///universidad.db')
Session = sessionmaker(bind=engine, expire_on_commit=False)