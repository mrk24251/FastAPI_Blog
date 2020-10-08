from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cloudinary

# SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

# postgresql+psycopg2://punish:punish@127.0.0.1:5432
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"postgresql+psycopg2cffi://user:password@host:port/dbname[?key=value&key=value...]
cloudinary.config(
  cloud_name = "dt0x3ff8y",
  api_key = "842463339847471",
  api_secret = "d4CUuUKhO4JSVfy9DA41a4KhGGw"
)
SQLALCHEMY_DATABASE_URL = "postgres://xthanqepblpwgp:4405c48dd5b1862b5dac59e379061229e93ae906edd3885d604402dbf0cbd978@ec2-23-23-36-227.compute-1.amazonaws.com:5432/dc8lq8trdj44in"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
