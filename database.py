from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL database connection URL
# Format: mysql+mysqlconnector://<username>:<password>@<host>/<database>
DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/product_db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for model definitions
Base = declarative_base()
