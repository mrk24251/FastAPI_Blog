from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = os.environ['DATABASE_URL']

# postgresql+psycopg2://punish:punish@127.0.0.1:5432
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"postgresql+psycopg2cffi://user:password@host:port/dbname[?key=value&key=value...]
SQLALCHEMY_DATABASE_URL = "postgres://rajehszfyqtaij:f9f9a72c98d295a74adfe2caf907d5bcc9724279eaac0589a52f6eee99dac14e@ec2-54-86-57-171.compute-1.amazonaws.com:5432/d2kbn16cmavq03"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
