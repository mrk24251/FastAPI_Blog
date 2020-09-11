from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

# postgresql+psycopg2://punish:punish@127.0.0.1:5432
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"postgresql+psycopg2cffi://user:password@host:port/dbname[?key=value&key=value...]
SQLALCHEMY_DATABASE_URL = "postgres://lifdpiiqaqlivu:fa4b5d7373b3d3f7c878be6acc5dab7fdf57ae9b7fabb574294ca3799491d8e9@ec2-3-214-46-194.compute-1.amazonaws.com:5432/db19g1r4671b9a"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
