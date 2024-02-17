from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# import MySQLdb

SQL_ALCHEMY_DATABASE_URL = "mysql+pymysql://root:password%404869@localhost:3306/blogs"
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, bind = engine)
Base = declarative_base()